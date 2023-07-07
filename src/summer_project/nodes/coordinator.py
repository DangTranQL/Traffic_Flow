#!/usr/bin/env python3
import rospy
import numpy as np
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64MultiArray, String, Float64, MultiArrayDimension
from summer_project.msg import limo_info, limo_info_array

ns = rospy.get_namespace()
if len(ns) > 1:
    print("=======\n{}\n======".format(ns))
ns = '/' + ns.strip('/')

LIMO_IDs = [789, 155]

limo_sub_topics = {}#ID:"LIMO_000{}/limo_info".format(ID) for ID in LIMO_IDs}
limo_pub_topics = {}#ID:"LIMO_000{}/MP_info".format(ID) for ID in LIMO_IDs}
for ID in LIMO_IDs:
    limo_sub_topics[ID] = "LIMO_000{}/limo_info".format(ID)
    limo_pub_topics[ID] = "LIMO_000{}/MP_info".format(ID)

LIMO_INFOS = {}
LIMO_OUTFOS = { # ID : LIST_OF_IDs
        #i.e.  robot : info needed by robot
    789:[789,155],
    155:[155, 789]
}

class coordinator_node:
    def __init__(self):
        self.limo_info_subs = {}
        self.limo_infos_pubs = {}
        for ID in LIMO_IDs:
            self.limo_info_subs[ID] = rospy.Subscriber(limo_sub_topics[ID], limo_info, self.limo_info_callb, queue_size=10)# for ID in LIMO_IDs]
            self.limo_infos_pubs[ID] = rospy.Publisher(limo_pub_topics[ID], limo_info_array, queue_size = 10)# for ID in LIMO_IDs]
    def limo_info_callb(self, msg):
        #called by each subscriber
        global LIMO_INFOS
        id = msg.ID.data
        LIMO_INFOS[id] = msg
        #msg contains ID and also other data...
        #each LIMO will need a set of limo_info datas, (i assume i'll know how to decide which)
        for targ_id in LIMO_OUTFOS.keys():
            out_msg = limo_info_array()
            out_msg.limo_infos = []
            for limo_id in LIMO_OUTFOS[targ_id]:
                if limo_id in LIMO_INFOS.keys():
                    out_msg.limo_infos.append(LIMO_INFOS[limo_id])
            self.limo_infos_pubs[targ_id].publish(out_msg)
if __name__ == '__main__':
    rospy.init_node('coordinator')
    coord = coordinator_node()
    rospy.spin()
