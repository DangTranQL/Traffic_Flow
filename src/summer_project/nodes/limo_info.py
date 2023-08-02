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
from calc import *

ns = rospy.get_namespace()
if len(ns) > 1:
    print("=======\n{}\n=======".format(ns))
ns = '/' + ns.strip('/')
proj_topic_name = '/limo_info'
odom_topic_name = '/odom'
imu_topic_name = '/imu'
task_topic = '/task'

mocap_topic_name = '/vrpn_client_node' + ns + '/pose'
PROJ_NODE_DATA = limo_info()#Float64MultiArray()
PROJ_NODE_DATA.ID.data = int(ns[-3:])


class project_node:
    def __init__(self):
        #print("\n\n=====\n",ns + odom_topic_name, "\n=====\n\n")
        self.info_pub = rospy.Publisher(ns + proj_topic_name, limo_info, queue_size=10)

        self.odom_sub = rospy.Subscriber(ns + odom_topic_name, Odometry, self.odom_callb, queue_size=10)
        # self.imu_sub = rospy.Subscriber(ns + imu_topic_name, Imu, self.imu_callb, queue_size=10)
        # print("inside INIT")
        # print("MOCAP TOPIC:" + mocap_topic_name)
        self.mocap_sub = rospy.Subscriber(mocap_topic_name, PoseStamped, self.mocap_callb, queue_size=10)
        self.task_sub = rospy.Subscriber(ns + task_topic, String, self.task_callb, queue_size=1)
        # self.prev_pos = [0,0]
        self.path_string = 'NONE'
    def task_callb(self, s_msg):
        global PROJ_NODE_DATA
        # msg = String()
        path_string = ""
        path = s_msg.data
        lane_s = path[1]
        turn_s = path[0]
        if turn_s.lower() == 'l':
            path_string = 'left'
        elif turn_s.lower() == 'r':
            path_string = 'right'
        elif turn_s.lower() == 's':
            path_string = 'straight'
        path_string += "_" + lane_s
        self.path_string = path_string
        # self.path_str =
        PROJ_NODE_DATA.path = String(path_string)
        self.pub_msg()

    def pub_msg(self):
        self.info_pub.publish(PROJ_NODE_DATA)
    def odom_callb(self, msg):
        global PROJ_NODE_DATA
        PROJ_NODE_DATA.vel.data = msg.twist.twist.linear.x # CHECK IF x IS RIGHT!!
        self.pub_msg()
    # def imu_callb(self, msg):
    #     global PROJ_NODE_DATA
    #     ang_v = msg.angular_velocity
    #     lin_acc = msg.linear_acceleration
    #     PROJ_NODE_DATA.acc.data = lin_acc.x # CHECK IF x IS RIGHT!!
    #     self.pub_msg()
    #     #PROJ_NODE_DATA.accel.angular
    def mocap_callb(self, msg):
        global PROJ_NODE_DATA
        if self.path_string == "NONE":
            return
        #PROJ_NODE_DATA.pose.data[0] = msg.pose.position.x    #CHECK THESE TOO!!!
        #PROJ_NODE_DATA.pose.data[1] = msg.pose.position.y
        p = msg.pose.position
        pos = [-p.x,-p.y]
        path = self.path_string
        # rospy.loginfo("{}\t{}".format(p.x,p.y))
        # PROJ_NODE_DATA.x.data = - p.x # TO BE REPLACED WITH SOMEHTING BETTER!!! #TODO
        # PROJ_NODE_DATA.y.data = - p.y
        # PROJ_NODE_DATA.x = merging_dst(pos, path)
        lat, mp_d, dist, stop_bool, turn_sect = signed_dist(pos, path, v=PROJ_NODE_DATA.vel.data)
        PROJ_NODE_DATA.mp_dist.data = mp_d
        PROJ_NODE_DATA.origin_dist.data = dist
        self.pub_msg()


if __name__ == '__main__':
    rospy.init_node("limo_info")
    node = project_node()
    rospy.spin()

    print("exitting loop")
