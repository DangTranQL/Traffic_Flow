#!/usr/bin/env python3
import rospy
import numpy as np
from std_msgs.msg import Float64MultiArray, String, Float64, MultiArrayDimension
from summer_project.msg import limo_info, limo_info_array, QP_solution
import QP
from calc import common_merge
# from calc import merging_dst

ns = rospy.get_namespace()
if len(ns) > 1:
    print("=======\n{}\n=======".format(ns))
ns = '/' + ns.strip('/')


info_topic_name = '/limo_info'          # this limo's info
MP_info_topic_name = '/MP_info'    # the info that this limo needs about the others

QP_solition_topic_name = '/qp_solution' # the qp solution topic

QP_SOLN = QP_solution()
LIMO_DATA = limo_info()
OTHER_LIMO_DATA = limo_info_array()

class project_node:
    def __init__(self):
        self.robot = QP.Robot(-1, 1, 0.18, 0.18, 0.1, 0, 1)
        self.limo_info_sub = rospy.Subscriber(ns+info_topic_name, limo_info, self.limo_info_callb, queue_size=1)
        self.other_limo_data_sub = rospy.Subscriber(ns+MP_info_topic_name, limo_info_array, self.other_limo_data_callb, queue_size=1)
        self.QP_soln_pub = rospy.Publisher(ns+QP_solition_topic_name, QP_solution, queue_size=1)
        # self.QP_time_pub = rospy.Publisher(ns+QP_dt, Float64, queue_size=1)
    def recalc_QP(self):
        global QP_SOLN
        # start_t = rospy.get_time()
        mp_d = LIMO_DATA.mp_dist.data
        v = LIMO_DATA.vel.data
        origin_dist = LIMO_DATA.origin_dist.data
        bot_path = LIMO_DATA.path.data
        other_paths = []
        all_positions = [(bot_path, (LIMO_DATA.x.data, LIMO_DATA.y.data)), []]
        QP_rows = []
        for other_limo_data in OTHER_LIMO_DATA:
            other_paths.append(other_limo_data.path.data)
            all_positions[1].append((other_limo_data.path.data, (other_limo_data.x.data, other_limo_data.y.data)))
            row = [other_limo_data.ID.data, other_limo_data.origin_dist.data, other_limo_data.vel.data]
            QP_rows.append(row)
        dst_list = common_merge(bot_path, other_paths, all_positions)

        # for
        car1_mp_dists = [origin_dist, v]
        for dsts in dst_list:
            for i, dst in enumerate(dsts[1:]):
                QP_rows[i].append(dst)
            car1_mp_dists.append(dsts[0])


        u = self.robot.OCBF_SecondOrderDynamics(1, np.array(
                    # [
                    #[ID, origin_distance, velocity, merging distance-origin distance(distance dang is giving us)]
                        QP_rows
                        # [-1, -1, -1, -1], # [-1, -1, -1, -1],
                        # [-1, -1, -1, -1],
                        # ]
                        ),
                        # [origin distance, velocity, remaining distance of car1 to the merging point]
                        # [origin_dist, v]
                        car1_mp_dists
                    )
        # fin_t = rospy.get_time()
        # rospy.loginfo("| {:^-9.4f} |".format(fin_t - start_t))
        # rospy.loginfo(str(v) + str(a))
        QP_SOLN.u.data = u
        # QP_SOLN.a.data = a
        self.QP_soln_pub.publish(QP_SOLN)
    def limo_info_callb(self, info_msg):
        global LIMO_DATA
        LIMO_DATA = info_msg
        self.recalc_QP()
    def other_limo_data_callb(self, info_arr_msg):
        global OTHER_LIMO_DATA
        OTHER_LIMO_DATA = info_arr_msg
        self.recalc_QP()

if __name__ == '__main__':
    rospy.init_node("QP_solver_node")
    node = project_node()
    rospy.spin()
    print("exitting loop")
