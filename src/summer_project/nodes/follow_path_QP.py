#!/usr/bin/env python3
import rospy
import numpy as np
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64MultiArray, String, Float64, MultiArrayDimension
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

TST_PATH = RT_WPTS_A # used by loop
# path_string = "straight_A"
path_string = "right_A"
#path_string = "straight_A"
ST_PT = TST_PATH[0]
END_PT = TST_PATH[-1]


limo = limo.LIMO()
limo.EnableCommand()

ns = rospy.get_namespace()
if len(ns) > 1:
    print("=======\n{}\n=======".format(ns))
ns = '/' + ns.strip('/')

proj_topic_name = '/limo_info'
QP_solition_topic_name = '/qp_solution'
error_topic = '/lat_error'

PROJ_NODE_DATA = limo_info()#Float64MultiArray()
PROJ_NODE_DATA.ID.data = int(ns[-3:])


#PID stuff
v = 0.6

right_kp = 0.0016
right_ki = 0.00020
right_kd = 0.0007

left_kp = 0.0016
left_ki = 0.00020
left_kd = 0.0007

# curved_kp = 0.0016
# curved_ki = 0.00008
# curved_kd = 0.0009

# curved_kp = 0.0016
# curved_ki = 0.0000
# curved_kd = 0.00102

# curved_kp = 0.0011#was 285
# curved_ki = 0.0000#2#2#3#0001#5
# curved_kd = 0.00095#1#9#1

# curved_kp = 0.015#was 285
# curved_ki = 0.0002#2#3#0001#5
# curved_kd = 0.003#1#9#1

# #FOR TURNING
# curved_kp = 0.00285#was 25
# curved_ki = 0.00002#3#0001#5
# curved_kd = 0.002#1#9#1

# curved_kp = 0.000195
# curved_ki = 0.000002#3#0001#5
# curved_kd = 0.00034#1#9#1

# straight_kp = 0.0007
# straight_ki = 0.00#0001#5
# straight_kd = 0.00055#1#9#1

straight_kp = 0.00095
straight_ki = 0.00#0001#5
straight_kd = 0.00095#1#9#1

# straight_kp = 0.00095
# straight_ki = 0.00#0001#5
# straight_kd = 0.00097#1#9#1

straight_pid = PID(straight_kp,straight_ki,straight_kd, setpoint=0)
left_pid = PID(left_kp,left_ki,left_kd, setpoint=0)
right_pid = PID(right_kp,right_ki,right_kd, setpoint=0)

MAX_STEER = 0.99#np.pi/8

r = 1
# bot_pos = [0,0]
class project_node:
    def __init__(self):
        self.info_sub = rospy.Subscriber(ns + proj_topic_name, limo_info, self.info_callb, queue_size=10)
        self.QP_soln_sub = rospy.Subscriber(ns + QP_solition_topic_name, QP_solution, self.QP_soln_callb, queue_size=10)
        self.error_pub = rospy.Publisher(ns + error_topic, Float64, queue_size=10)
        self.v = 0
        self.a = 0
    def info_callb(self, info_msg):
        global PROJ_NODE_DATA
        PROJ_NODE_DATA = info_msg
    def cmd_vel(self, v, th):
        limo.SetMotionCommand(v, 0, 0, th)
    def QP_soln_callb(self, qp_msg):
        self.v = qp_msg.v.data
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
    while not rospy.is_shutdown():
        cur_t = rospy.get_time()
        dt = cur_t - last_t
        last_t = cur_t
        bot_pos = [PROJ_NODE_DATA.x.data, PROJ_NODE_DATA.y.data]
        st_d = geom.dist(bot_pos, ST_PT)
        # total_d = geom.dist(ST_PT, END_PT)
        # end_d = geom.dist(bot_pos,END_PT)
        # v = max(0.2, min(1, 1 - (end_d / total_d)))
        larger = max(st_d, end_d)
        smaller = min(st_d, end_d)
        ratio = smaller / larger
        v = max(0.2, ratio)



        e, mp_d, should_stop, gain_string = signed_dist(bot_pos, path_string)
        # e, mp_d, should_stop, gain_string = signed_dist(TST_PATH, bot_pos)

        # e, mp_d = signed_dist(bot_pos, path_string) # Dang's code

        e *= 1000
        if left_pid._integral  > 50:
            left_pid._integral = 0 #= PID(curved_kp,curved_ki,curved_kd, setpoint=0)
        if right_pid._integral  > 50:
            right_pid._integral = 0 #= PID(curved_kp,curved_ki,curved_kd, setpoint=0)
        if straight_pid._integral  > 50:
            straight_pid._integral = 0 #= PID(curved_kp,curved_ki,curved_kd, setpoint=0)

        node.error_pub.publish(e)
        rospy.loginfo("| {:^-9.4f} | {:^-9.4f} | {:^9b} | {:^9s} | {:^-9.4f} |".format(dt, e, should_stop, gain_string, mp_d))
        # rospy.loginfo("| {:^-9.4f} | {:^-9.4f} | {:^-9.4f} |".format(dt, e, v))

        # #=========================CONTROL with PID================
        if geom.dist(bot_pos, TST_PATH[-1]) < 0.2 or should_stop:
        # # if geom.dist(bot_pos, end_p) < 0.6:
            node.cmd_vel(0, 0)
            input("press enter")
        else:
            # straight_u = -straight_pid(e)
            # u = straight_u
            if "straight" in gain_string.lower():
                u = - straight_pid(e, dt=dt)
                left_pid(e, dt=dt)
                right_pid(e, dt=dt)
            elif "left" in gain_string.lower():
                u = - left_pid(e, dt=dt)
                straight_pid(e, dt=dt)
                right_pid(e, dt=dt)
                # rospy.loginfo("")
            elif "right" in gain_string.lower():
                u = -right_pid(e, dt=dt)
                left_pid(e, dt=dt)
                straight_pid(e, dt=dt)
            theta = min(MAX_STEER, max(-MAX_STEER, u))
            node.cmd_vel(v, theta)
        # #=========================END CONTROL with PID============
    # except KeyboardInterrupt:
    node.cmd_vel(0, 0)
    print("exitting loop")
