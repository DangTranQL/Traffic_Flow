#!/usr/bin/env python3
import rospy
import numpy as np
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64MultiArray, String, Float64, MultiArrayDimension
from summer_project.msg import limo_info, limo_info_array
from simple_pid import PID
import geom_util as geom
import time
from pylimo import limo
from collections import deque
from robot import signed_dist
import QP

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

my_robot = QP.Robot(-0.3, 0.3, 0.18, 0.18, 0.1, 0, 1)





#using optimizer
# RT_COEFFS = COEFFS['R']
# LT_COEFFS = COEFFS['L']
# ST_COEFFS = COEFFS['S']
#
# RT_POLYS = POLYS['R']
# LT_POLYS = POLYS['L']
# ST_POLYS = POLYS['S']
#
# TST_POLYS = ST_POLYS
# TST_PATH_COEFFS = ST_COEFFS



# end_p = [TST_POLY(1) for TST_POLY in TST_POLYS]

limo = limo.LIMO()
limo.EnableCommand()

ns = rospy.get_namespace()
if len(ns) > 1:
    print("=======\n{}\n=======".format(ns))
ns = '/' + ns.strip('/')
proj_topic_name = '/limo_info'
odom_topic_name = '/odom'
imu_topic_name = '/imu'
mocap_topic_name = '/mocap_pose'

cmd_vel_topic = '/cmd_vel'

error_topic = '/lat_error'

PROJ_NODE_DATA = limo_info()#Float64MultiArray()
PROJ_NODE_DATA.ID.data = int(ns[-3:])


#PID stuff
v = 0.6

straight_kp = 0.00285#was 25
straight_ki = 0.00002#3#0001#5
straight_kd = 0.002#1#9#1
# #FOR TURNING LEFT
# straight_kp = 0.000195
# straight_ki = 0.000002#3#0001#5
# straight_kd = 0.00034#1#9#1

#
# straight_kp = 0.00035
# straight_ki = 0.00#0001#5
# straight_kd = 0.00037#1#9#1

# #REALLY GOOD
# straight_kp = 0.00035
# straight_ki = 0.00#0001#5
# straight_kd = 0.00037#1#9#1

straight_pid = PID(straight_kp,straight_ki,straight_kd, setpoint=0)

MAX_STEER = 0.99#np.pi/8

r = 1
# bot_pos = [0,0]
class project_node:
    def __init__(self):
        self.info_sub = rospy.Subscriber(ns + proj_topic_name, limo_info, self.info_callb, queue_size=10)
        self.error_pub = rospy.Publisher(ns + error_topic, Float64, queue_size=10)
    def info_callb(self, info_msg):
        global PROJ_NODE_DATA
        PROJ_NODE_DATA = info_msg
    def cmd_vel(self, v, th):
        limo.SetMotionCommand(v, 0, 0, th)

if __name__ == '__main__':
    rospy.init_node("QP_path_follower")
    node = project_node()
    node.cmd_vel(0, 0)
    time.sleep(0.15)

    last_t = rospy.get_time()
    dts = deque(maxlen=8)
    rospy.loginfo("| {:^9s} | {:^9s} | {:^9s} |".format("dt", "position", "velocity"))

    while not rospy.is_shutdown():
        #get lateral distance
        cur_t = rospy.get_time()
        dt = cur_t - last_t
        dts.append(dt)
        avg_dt = np.average(np.array(dts))
        last_t = cur_t
        #commment this out later pls
        # rospy.loginfo(avg_dt)
        bot_pos = [PROJ_NODE_DATA.x.data, PROJ_NODE_DATA.y.data]
        # print(bot_pos)
        # pos_e = r - geom.dist_2_line(P0,P1, bot_pos)
        # e = signed_error(TST_PATH, bot_pos)*1000
        e = signed_dist(bot_pos, path_string) * 1000 # Dang's code
        node.error_pub.publish(e)
        # try:
        rt, vd = my_robot.OCBF_SecondOrderDynamics(1, np.array([
                    [-1, -1, -1, -1],
                    [-1, -1, -1, -1],
                    [-1, -1, -1, -1],
                    ]),
                    [0.503779, 0.5, 0.2898, 1.061228]
                )
        rospy.loginfo("| {:^-9.4f} | {:^-9.4f} | {:^-9.4f} | {:^-9.4f} |".format(dt, rt[0], rt[1], vd))
        # except TypeEr,ror:
        #     rospy.loginfo("INFEASIBLE")
        # rospy.loginfo("| {:^-9.4f} |".format(dt))#, rt[0], rt[1]))
        # #=========================++CONTROL with PID=============
        if geom.dist(bot_pos, TST_PATH[-1]) < 0.6:
        # # if geom.dist(bot_pos, end_p) < 0.6:
            node.cmd_vel(0, 0)
            input("press enter")
        #     # if len(TST_PATH) > 2:
        #     #     TMP = TST_PATH
        #     #     TST_PATH = [TST_PATH[-1], TST_PATH[0]]
        #     #     try:
        #     #         start_t = rospy.get_time()
        #     #         while rospy.get_time() - start_t < 1.5:
        #     #             node.cmd_vel(0.4, 0.6)
        #     #             if rospy.is_shutdown():
        #     #                 break
        #     #             # time.sleep(0.0001)
        #     #         node.cmd_vel(0, -0.6)
        #     #         time.sleep(0.2)
        #     #         start_t = rospy.get_time()
        #     #         # time.sleep(0.01)
        #     #         while rospy.get_time() - start_t < 2.2:
        #     #             node.cmd_vel(-0.4, -0.6)
        #     #             if rospy.is_shutdown():
        #     #                 break
        #     #             # time.sleep(0.0001)
        #     #         node.cmd_vel(0, 0)
        #     #     except KeyboardInterrupt:
        #     #         break
        #     #     time.sleep(0.1)
        #     # else:
        #     #     input("press enter")
        #     #     TST_PATH = TMP
        #
        #     # input("press enter to continue")
        #     # break
        #     # path reversal:
        #
        #     # TST_PATH = list(reversed(TST_PATH))
        else:
        #     #=============CONTROL PART===========
        #     # e = poly_signed_error(TST_PATH_COEFFS, bot_pos) * 1000
        #     # e *= abs(e)
        #     # print(e)
            straight_u = -straight_pid(e)
        #     # rospy.loginfo("{:^-8.3f}\t{:^-8.3f}\t{:^3d}".format(e, straight_u, limo.GetErrorCode()))
        #     rospy.loginfo("{:^-8.3f}\t{:^-8.3f}\t{:^-8.6f}".format(e, straight_u, avg_dt))#, limo.GetErrorCode()))
        #     # rospy.loginfo(limo.GetErrorCode())
        #
            u = straight_u
        #
            theta = min(MAX_STEER, max(-MAX_STEER, u))
            node.cmd_vel(v, theta)
        # #=========================END CONTROL with PID=============
    # except KeyboardInterrupt:
    node.cmd_vel(0, 0)
    print("exitting loop")
