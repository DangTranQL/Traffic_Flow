#!/usr/bin/env python3
import rospy
import numpy as np
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64MultiArray, String, Float64, MultiArrayDimension
from summer_project.msg import limo_info, limo_info_array

from calc import common_merge#, d2_d1
import copy
ns = rospy.get_namespace()
if len(ns) > 1:
    print("=======\n{}\n======".format(ns))
ns = '/' + ns.strip('/')

LIMO_IDs = [789, 770]#[789, 155, 799, 770, 815]
# TODO: PUT THIS IN IT'S OWN TOPIC!!

MPs = []

limo_sub_topics = {}#ID:"LIMO_000{}/limo_info".format(ID) for ID in LIMO_IDs}
limo_pub_topics = {}#ID:"LIMO_000{}/MP_info".format(ID) for ID in LIMO_IDs}
task_subs = []
# mocap_sub_topics = {}
for ID in LIMO_IDs:
    limo_sub_topics[ID] = "LIMO_000{}/limo_info".format(ID)
    limo_pub_topics[ID] = "LIMO_000{}/MP_info".format(ID)
    # mocap_sub_topics[ID] = "vrpn_client_node/LIMO_000{}/pose".format(ID)

# LIMO_POSES = {}

LIMO_INFOS = {} # dict {ID : limo_info()}
LIMO_OUTFOS = {
    # target :   [ID_0, ..., ID_n]
    789   :   [],
    770   :   [789]
}

out_datas = {
    789: limo_info_array(),
    770: limo_info_array()
}
for targ in LIMO_OUTFOS.keys():
    for val in LIMO_OUTFOS[targ]:
        out_datas[targ].limo_infos.append(limo_info())

class coordinator_node:
    def __init__(self):
        self.limo_info_subs = {}
        self.limo_infos_pubs = {}
        self.mocap_subs = {}
        for ID in LIMO_IDs:
            # self.mocap_subs[ID] = rospy.Subscriber(mocap_sub_topics[ID], PoseStamped, self.mocap_callb, queue_size=10)
            self.limo_info_subs[ID] = rospy.Subscriber(limo_sub_topics[ID], limo_info, self.limo_info_callb, queue_size=10)# for ID in LIMO_IDs]
            self.limo_infos_pubs[ID] = rospy.Publisher(limo_pub_topics[ID], limo_info_array, queue_size = 10)# for ID in LIMO_IDs]
    def limo_info_callb(self, msg):
        #called by each subscriber
        global LIMO_INFOS
        global out_datas
        id = msg.ID.data
        LIMO_INFOS[id] = msg
        #msg contains ID and also other data...
        #each LIMO will need a set of limo_info datas, (i assume i'll know how to decide which)
        # rospy.loginfo("---")
        # rospy.loginfo(len(LIMO_OUTFOS.keys()))
        # rospy.loginfo(len(LIMO_INFOS.keys()))
        if len(LIMO_OUTFOS.keys()) == 0 or len(LIMO_INFOS.keys()) == 0:
            return
        for targ_id in LIMO_OUTFOS.keys():
            # out_msg = limo_info_array()
            # out_msg.limo_infos = []
            num_out = len(LIMO_OUTFOS[targ_id])
            c = 0
            try:
                main_arg = [
                    LIMO_INFOS[targ_id].path.data,
                    LIMO_INFOS[targ_id].ID.data,
                    [LIMO_INFOS[targ_id].x.data, LIMO_INFOS[targ_id].y.data],
                    LIMO_INFOS[targ_id].vel.data
                ]
            except KeyError:
                return
            others_arg = []
            for limo_id in LIMO_OUTFOS[targ_id]:
                if limo_id in list(LIMO_INFOS.keys()):
                    # out_msg.limo_infos.append(LIMO_INFOS[limo_id])
                    # out_datas[targ_id].limo_infos.append(LIMO_INFOS[limo_id])
                    others_arg.append([
                        LIMO_INFOS[limo_id].path.data,
                        LIMO_INFOS[limo_id].ID.data,
                        [LIMO_INFOS[limo_id].x.data, LIMO_INFOS[limo_id].y.data],
                        LIMO_INFOS[limo_id].vel.data
                    ])
                    # LIMO_INFOS[limo_id].d1.data = ???
                    # LIMO_INFOS[limo_id].d2.data = ???

                    out_datas[targ_id].limo_infos[c] = copy.deepcopy(LIMO_INFOS[limo_id])
                    #MOVE COMMON_MERGE HERE!!!!!!!!!!!!!
                    # out_datas[targ_id].limo_infos[c].d1 = 0
                    # out_datas[targ_id].limo_infos[c].d2 = 0
                    c += 1
            # try:
            if len(main_arg[0]) == 0:
                return
            common_merge_info = common_merge(main_arg, others_arg)
            # except:
            #     # print(__name__)
            # print("---")
            # print(targ_id)
            # print("main:")
            # print(main_arg)
            # print("other")
            # print(others_arg)
            # print("output:")
            # print(common_merge_info)
            # print()
            # print("---")
            # print(targ_id)
            for i, dummy_variable in enumerate(common_merge_info):
            # dummy_variable = common_merge_info[0]
                # for merge_info in enumerate(dummy_variable):
                merge_info = dummy_variable[0]
                # print(merge_info)
                out_datas[targ_id].limo_infos[i].d1.data = merge_info[2]
                out_datas[targ_id].limo_infos[i].d2.data = merge_info[1]
            # print()

            # self.limo_infos_pubs[targ_id].publish(out_msg)
            self.limo_infos_pubs[targ_id].publish(out_datas[targ_id])
if __name__ == '__main__':
    rospy.init_node('coordinator')
    coord = coordinator_node()
    rospy.spin()

    # while not rospy.is_shutdown():
    #     rospy.Rate(20)#                     run at 20 hz
    #     num_IDs = len(LIMO_IDs)
    #     num_infos = len(LIMO_INFOS.keys())
    #     if num_IDs != num_infos:
    #         continue
    #     for ID_1 in LIMO_IDs:
    #         path_1 = LIMO_INFOS[ID_1].path.data
    #         pos_1 = [LIMO_INFOS[ID_1].x.data, LIMO_INFOS[ID_1].y.data]
    #         v_1 = LIMO_INFOS[ID_1].vel.data
    #         my_data = [path_1, ID_1, pos_1, v_1]
    #         other_data = []
    #         for ID_2 in LIMO_IDs:
    #             if ID_2 == ID_1:
    #                 continue
    #             path_2 = LIMO_INFOS[ID_2].path.data
    #             pos_2 = [LIMO_INFOS[ID_2].x.data, LIMO_INFOS[ID_2].y.data]
    #             v_2 = LIMO_INFOS[ID_2].vel.data
    #             other_data.append([path_2, ID_2, pos_2, v_2])
    #         common_merge_data = common_merge(my_data, other_data)
    #         my_targs = []
    #         # rospy.loginfo(str(ID_1))
    #         for data in common_merge_data:
    #             for other_bot_data in data:
    #                 my_targs.append(other_bot_data[0])
    #                 # rospy.loginfo("\t" + str(other_bot_data[0]))
    #
    #         LIMO_OUTFOS[ID_1] = my_targs

        # # PRINT INFO ABOUT THE MESSAGE DICT
        # p_str = "| {:^5d} "
        # f_str = ''
        # rospy.loginfo("------------------")
        # # # rospy.loginfo
        # for k in LIMO_OUTFOS.keys():
        # #     # p_data = [k]
        #     # f_str += p_str.format(k)
        #     rospy.loginfo(str(k))
        #     for t in LIMO_OUTFOS[k]:
        #         rospy.loginfo("\t" + str(t))
                # f_str += p_str.format(t)
                # p_data.append(t)
            # rospy.loginfo(f_str+'|')
            # rospy.loginfo((f_str+'|').format(p_data))
