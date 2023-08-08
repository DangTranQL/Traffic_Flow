#!/usr/bin/env python3
import rospy
import numpy as np
from std_msgs.msg import String

task_topic = '/task'

tasks = {
    789: "SA",
    770: "LB"
    # 155: "LC"#,
    # 799: "RD"
}

class node:
    def __init__(self):
        self.task_pubs = {}
        print("setting up tasks")
        for k in tasks.keys():
            print("\tLIMO_000"+str(k) + " -> " + tasks[k])
            self.task_pubs[k] = rospy.Publisher("/LIMO_000"+str(k) + task_topic, String, queue_size=1)
    def run(self):
        hz = 20
        print(f"sending tasks at {hz} hz")
        while not rospy.is_shutdown():
            for k in tasks.keys():
                msg = String(tasks[k])
                self.task_pubs[k].publish(msg)
            rospy.Rate(hz)
        #     inp = input("0/1 stop/start ->")
        #     # if inp == '0':
        #     msg = Bool()
        #     msg.data = inp=='1'
        #     self.start_stop_pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node("task_designator")
    n = node()
    n.run()
    print("exited")
