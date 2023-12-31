#!/usr/bin/env python3
import rospy
import numpy as np
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64MultiArray, String, Float64, MultiArrayDimension, Bool
from summer_project.msg import limo_info, limo_info_array, QP_solution
from simple_pid import PID
import geom_util as geom
import time
from pylimo import limo
from collections import deque
# from robot import signed_dist
from calc import signed_dist
# import QP
# my_robot = QP.Robot(-0.3, 0.3, 0.18, 0.18, 0.1, 0, 1)

from lane_poly import *
#using waypoints
RT_WPTS_A = WPTS['R_A']
LT_WPTS_A = WPTS['L_A']
ST_WPTS_A = WPTS['S_A']
RT_WPTS_B = WPTS['R_B']
LT_WPTS_B = WPTS['L_B']
ST_WPTS_B = WPTS['S_B']
RT_WPTS_C = WPTS['R_C']
LT_WPTS_C = WPTS['L_C']
ST_WPTS_C = WPTS['S_C']
RT_WPTS_D = WPTS['R_D']
LT_WPTS_D = WPTS['L_D']
ST_WPTS_D = WPTS['S_D']

def setup_path(task_str):
    global TST_PATH, ST_PT, END_PT, path_string
    if task_str == "RA":
        TST_PATH = RT_WPTS_A # used by loop
        path_string = "right_A"
    elif task_str == "LA":
        TST_PATH = LT_WPTS_A # used by loop
        path_string = "left_A"
    elif task_str == "SA":
        TST_PATH = ST_WPTS_A # used by loop
        path_string = "straight_A"

    elif task_str == "RB":
        TST_PATH = RT_WPTS_B # used by loop
        path_string = "right_B"
    elif task_str == "LB":
        TST_PATH = LT_WPTS_B # used by loop
        path_string = "left_B"
    elif task_str == "SB":
        TST_PATH = ST_WPTS_B # used by loop
        path_string = "straight_B"

    elif task_str == "RC":
        TST_PATH = RT_WPTS_C # used by loop
        path_string = "right_C"
    elif task_str == "LC":
        TST_PATH = LT_WPTS_C # used by loop
        path_string = "left_C"
    elif task_str == "SC":
        TST_PATH = ST_WPTS_C # used by loop
        path_string = "straight_C"

    elif task_str == "RD":
        TST_PATH = RT_WPTS_D # used by loop
        path_string = "right_D"
    elif task_str == "LD":
        TST_PATH = LT_WPTS_D # used by loop
        path_string = "left_D"
    elif task_str == "SD":
        TST_PATH = ST_WPTS_D # used by loop
        path_string = "straight_D"


    # path_string = "straight_A"
    #path_string = "straight_A"
    ST_PT = TST_PATH[0]
    END_PT = TST_PATH[-1]
setup_path("RA")

# TST_PATH = RT_WPTS_A # used by loop
# # path_string = "straight_A"
# path_string = "right_A"
# #path_string = "straight_A"
# ST_PT = TST_PATH[0]
# END_PT = TST_PATH[-1]

limo = limo.LIMO()
limo.EnableCommand()

ns = rospy.get_namespace()
if len(ns) > 1:
    print("=======\n{}\n=======".format(ns))
ns = '/' + ns.strip('/')

proj_topic_name = '/limo_info'
QP_solition_topic_name = '/qp_solution'
error_topic = '/lat_error'

task_topic = '/task'
start_stop_topic = '/start_stop'

mocap_topic_name = '/vrpn_client_node' + ns + '/pose'

v_setpoint_topic = '/v_setpoint'

PROJ_NODE_DATA = limo_info()#Float64MultiArray()
PROJ_NODE_DATA.ID.data = int(ns[-3:])


#PID stuff
v = 0#.6

right_kp = 0.002
right_ki = 0.00020
right_kd = 0.0007

# right_kp = 0.0016
# right_ki = 0.00020
# right_kd = 0.0007

left_kp = 0.0016
left_ki = 0.00020
left_kd = 0.0007

straight_kp = 0.00095
straight_ki = 0.00#0001#5
straight_kd = 0.00095#1#9#1


straight_pid = PID(straight_kp,straight_ki,straight_kd, setpoint=0)
left_pid = PID(left_kp,left_ki,left_kd, setpoint=0)
right_pid = PID(right_kp,right_ki,right_kd, setpoint=0)

MAX_STEER = 0.99#np.pi/8
MAX_SPEED = 0.8 if "789" in ns else 1
MIN_SPEED = 0#- MAX_SPEED
r = 1
# bot_pos = [0,0]
class project_node:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.u = 0
        self.v = 0#1 if "770" in ns else 0
        self.active = False
        self.u_t = rospy.get_time()
        self.u_t_last = self.u_t
        self.v_set_pub = rospy.Publisher(ns + v_setpoint_topic, Float64, queue_size=1)
        self.info_sub = rospy.Subscriber(ns + proj_topic_name, limo_info, self.info_callb, queue_size=10)
        self.QP_soln_sub = rospy.Subscriber(ns + QP_solition_topic_name, QP_solution, self.QP_soln_callb, queue_size=10)
        self.error_pub = rospy.Publisher(ns + error_topic, Float64, queue_size=10)
        self.start_stop_sub = rospy.Subscriber(start_stop_topic, Bool, self.start_stop_callb, queue_size=1)
        self.task_sub = rospy.Subscriber(ns+ task_topic,String, self.task_callb, queue_size=10)
        self.mocap_sub = rospy.Subscriber(mocap_topic_name, PoseStamped, self.mocap_callb, queue_size=10)
        self.PATH_READY = False
        # self.u = 0
    def mocap_callb(self, pose_st_msg):
        self.x = -pose_st_msg.pose.position.x
        self.y = -pose_st_msg.pose.position.y
    def task_callb(self, task_msg):
        global TST_PATH, ST_PT, END_PT, path_string
        self.PATH_READY = True
        setup_path(task_msg.data)
    def start_stop_callb(self, b_msg):
        self.active = b_msg.data
    def info_callb(self, info_msg):
        global PROJ_NODE_DATA
        PROJ_NODE_DATA = info_msg
    def cmd_vel(self, v, th):
        limo.SetMotionCommand(v, 0, 0, th)
    def QP_soln_callb(self, qp_msg):
        # if not self.active:
        #     return
        self.u = qp_msg.u.data
        # self.u_t = rospy.get_time()
        # dt = self.u_t - self.u_t_last
        # self.u_t_last = self.u_t
        # self.v += dt * self.u# * 0.2
        # self.v = min(MAX_SPEED, max(MIN_SPEED, self.v))
        # self.a = qp_msg.a.data

if __name__ == '__main__':
    rospy.init_node("QP_path_follower")
    node = project_node()
    node.cmd_vel(0, 0)
    time.sleep(0.15)

    last_t = rospy.get_time()
    dts = deque(maxlen=8)
    # rospy.loginfo("| {:^9s} | {:^9s} | {:^9s} |".format("dt", "position", "velocity"))
    # rospy.loginfo("| {:^9s} | {:^9s} |".format("dt", "error"))#, "velocity"))
    loop_cnt = 0
    rt = [0,1]
    vd = 0
    a = True
    u = 0
    while not node.PATH_READY:
        rospy.Rate(100)
    while not rospy.is_shutdown():
        bot_pos = [node.x, node.y]
        cur_t = rospy.get_time()
        dt = cur_t - last_t
        last_t = cur_t
        st_d = geom.dist(bot_pos, ST_PT)
        end_d = geom.dist(bot_pos,END_PT)
        # bot_pos = [PROJ_NODE_DATA.x.data, PROJ_NODE_DATA.y.data]
        # total_d = geom.dist(ST_PT, END_PT)
        # v = max(0.2, min(1, 1 - (end_d / total_d)))
        larger = max(st_d, end_d)
        smaller = min(st_d, end_d)
        ratio = smaller / larger
        # v = min(1, max(0.2, ratio))#      V RAMPING
        # e, mp_d, should_stop, gain_string = signed_dist(bot_pos, path_string)
        e, mp_d, path_dist, should_stop, gain_string = signed_dist(bot_pos, path_string, v=PROJ_NODE_DATA.vel.data)
        # e, mp_d, should_stop, gain_string = signed_dist(TST_PATH, bot_pos)
        # e, mp_d = signed_dist(bot_pos, path_string) # Dang's code

        e *= 1000
        # rospy.loginfo("| {:^-9.4f} | {:^-9.4f} | {:^3b} | {:^9s} | {:^-9.4f} | {:^-5.3f} | {:^-5.3f} |".format(dt, e, should_stop, gain_string, mp_d, node.x, node.y))
        # rospy.loginfo("| {:^-9.4f} | {:^-9.4f} | {:^-9.4f} | {:^-5.3f} | {:^-5.3f} | {:^-9.4f} |".format(dt, mp_d, path_dist, node.x, node.y, e))

        if node.active:
            a = True
            node.v += node.u * dt
            node.v_set_pub.publish(Float64(node.v))
            # node.v = min()

            node.v = min(MAX_SPEED, max(MIN_SPEED, node.v))
            v = node.v
            # v = node.v
            if left_pid._integral  > 50:
                left_pid.reset()#_integral = 0 #= PID(curved_kp,curved_ki,curved_kd, setpoint=0)
            if right_pid._integral  > 50:
                right_pid.reset()#_integral = 0 #= PID(curved_kp,curved_ki,curved_kd, setpoint=0)
            if straight_pid._integral  > 50:
                straight_pid.reset()#_integral = 0 #= PID(curved_kp,curved_ki,curved_kd, setpoint=0)
            node.error_pub.publish(e)
            # rospy.loginfo("| {:^-9.4f} | {:^-9.4f} | {:^-9.4f} |".format(dt, e, v))

            # #=========================CONTROL with PID================
            if geom.dist(bot_pos, TST_PATH[-1]) < 0.2 or should_stop:
            # # if geom.dist(bot_pos, end_p) < 0.6:
                node.cmd_vel(0, 0)
                node.active = False
                # input("press enter")
            else:
                # straight_u = -straight_pid(e)
                # u = straight_u
                if "straight" in gain_string.lower():
                    u = - straight_pid(e, dt=dt)
                    # left_pid(e, dt=dt)
                    # right_pid(e, dt=dt)
                    left_pid.reset()
                    right_pid.reset()
                elif "left" in gain_string.lower():
                    u = - left_pid(e, dt=dt)
                    # straight_pid(e, dt=dt)
                    # right_pid(e, dt=dt)
                    straight_pid.reset()
                    right_pid.reset()
                    # rospy.loginfo("")
                elif "right" in gain_string.lower():
                    u = -right_pid(e, dt=dt)
                    # left_pid(e, dt=dt)
                    # straight_pid(e, dt=dt)
                    left_pid.reset()
                    straight_pid.reset()
                theta = min(MAX_STEER, max(-MAX_STEER, u))
                node.cmd_vel(v, theta)
        else:
            if a:
                node.cmd_vel(0,0)
                a = False
            left_pid.reset()
            straight_pid.reset()
            right_pid.reset()
            # #=========================END CONTROL with PID============
    # except KeyboardInterrupt:
    node.cmd_vel(0, 0)
    print("exitting PID loop")
