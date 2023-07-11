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


ns = rospy.get_namespace()
if len(ns) > 1:
    print("=======\n{}\n=======".format(ns))
ns = '/' + ns.strip('/')
proj_topic_name = '/limo_info'
odom_topic_name = '/odom'
imu_topic_name = '/imu'
mocap_topic_name = '/mocap_pose'

cmd_vel_topic = '/cmd_vel'

PROJ_NODE_DATA = limo_info()#Float64MultiArray()
PROJ_NODE_DATA.ID.data = int(ns[-3:])


#PID stuff
v = 0.25

pos_kp = 0.9
pos_ki = 0.009
pos_kd = 0.85

pos_pid = PID(pos_kp,pos_ki,pos_kd, setpoint=0)


head_kp = 0.9
head_ki = 0.009
head_kd = 0.75

head_pid = PID(head_kp,head_ki,head_kd, setpoint=0)



DUMMY_DIST_ERR = 1
MAX_STEER = 1#np.pi/8

# P0 = np.array([1308, 1345]) * 1e-3
P0 = np.array([-686, 1070]) * 1e-3
P1 = np.array([-715, 4648]) * 1e-3

r = 1
# bot_pos = [0,0]
class project_node:
    def __init__(self):
        #print("\n\n=====\n",ns + odom_topic_name, "\n=====\n\n")
        self.cmd_vel_pub = rospy.Publisher(ns + cmd_vel_topic, Twist, queue_size=10)
        self.info_pub = rospy.Publisher(ns + proj_topic_name, limo_info, queue_size=10)

        self.odom_sub = rospy.Subscriber(ns + odom_topic_name, Odometry, self.odom_callb, queue_size=10)
        self.imu_sub = rospy.Subscriber(ns + imu_topic_name, Imu, self.imu_callb, queue_size=10)
        self.mocap_sub = rospy.Subscriber(ns + mocap_topic_name, PoseStamped, self.mocap_callb, queue_size=10)
    def cmd_vel(self, v, th):
        msg = Twist()
        msg.linear.x = v
        msg.angular.z = th
        self.cmd_vel_pub.publish(msg)
    def pub_msg(self):
        self.info_pub.publish(PROJ_NODE_DATA)
    def odom_callb(self, msg):
        global PROJ_NODE_DATA
        PROJ_NODE_DATA.vel.data = msg.twist.twist.linear.x # CHECK IF x IS RIGHT!!
        self.pub_msg()
    def imu_callb(self, msg):
        global PROJ_NODE_DATA
        ang_v = msg.angular_velocity
        lin_acc = msg.linear_acceleration
        PROJ_NODE_DATA.acc.data = lin_acc.x # CHECK IF x IS RIGHT!!
        self.pub_msg()
        #PROJ_NODE_DATA.accel.angular
    def mocap_callb(self, msg):
        global PROJ_NODE_DATA
        #PROJ_NODE_DATA.pose.data[0] = msg.pose.position.x    #CHECK THESE TOO!!!
        #PROJ_NODE_DATA.pose.data[1] = msg.pose.position.y
        p = msg.pose.position
        PROJ_NODE_DATA.x.data = - p.x
        PROJ_NODE_DATA.y.data = - p.y
        self.pub_msg()


if __name__ == '__main__':
    rospy.init_node("project_node")
    node = project_node()
    # rospy.spin()
    while not rospy.is_shutdown():
        #get lateral distance
        bot_pos = [PROJ_NODE_DATA.x.data, PROJ_NODE_DATA.y.data]
        pos_e = r - geom.dist_2_line(P0,P1, bot_pos)
        pos_e *= abs(pos_e) * 10
        # print(e)
        pos_c = pos_pid(pos_e)

        #

        c = pos_c

        theta = min(MAX_STEER, max(-MAX_STEER, c))
        # v = 0.4
        # print(theta)
        node.cmd_vel(v, theta)
