#!/usr/bin/env python3
import rospy
import numpy as np
from std_msgs.msg import Bool

start_stop_topic = '/start_stop'

class node:
    def __init__(self):
        self.start_stop_pub = rospy.Publisher(start_stop_topic, Bool, queue_size=1)
    def run(self):
        while not rospy.is_shutdown():
            inp = input("0/1 stop/start ->")
            # if inp == '0':
            msg = Bool()
            msg.data = inp=='1'
            self.start_stop_pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node("start_stop")
    n = node()
    n.run()
    print("exited")
