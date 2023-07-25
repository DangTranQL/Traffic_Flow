#!/usr/bin/env python3
import rospy
import numpy as np
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64MultiArray, String, Float64, MultiArrayDimension
from summer_project.msg import limo_info, limo_info_array
import geom_util as geom
import time

ns = rospy.get_namespace()
if len(ns) > 1:
    print("=======\n{}\n=======".format(ns))
ns = '/' + ns.strip('/')
proj_topic_name = '/limo_info'
odom_topic_name = '/odom'
imu_topic_name = '/imu'
mocap_topic_name = '/mocap_pose'

PROJ_NODE_DATA = limo_info()#Float64MultiArray()
PROJ_NODE_DATA.ID.data = int(ns[-3:])


class project_node:
    def __init__(self):
        #print("\n\n=====\n",ns + odom_topic_name, "\n=====\n\n")
        self.info_pub = rospy.Publisher(ns + proj_topic_name, limo_info, queue_size=10)

        self.odom_sub = rospy.Subscriber(ns + odom_topic_name, Odometry, self.odom_callb, queue_size=10)
        self.imu_sub = rospy.Subscriber(ns + imu_topic_name, Imu, self.imu_callb, queue_size=10)
        self.mocap_sub = rospy.Subscriber(ns + mocap_topic_name, PoseStamped, self.mocap_callb, queue_size=10)

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
    rospy.init_node("limo_info")
    node = project_node()
    rospy.spin()

    print("exitting loop")
