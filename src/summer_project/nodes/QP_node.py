#!/usr/bin/env python3
import rospy
import numpy as np
from std_msgs.msg import Float64MultiArray, String, Float64, MultiArrayDimension, Bool
from summer_project.msg import limo_info, limo_info_array, QP_solution
import QP_2 as QP
from calc import common_merge
# from calc import merging_dst

ns = rospy.get_namespace()
if len(ns) > 1:
    print("=======\n{}\n=======".format(ns))
ns = '/' + ns.strip('/')


info_topic_name = '/limo_info'          # this limo's info
MP_info_topic_name = '/MP_info'    # the info that this limo needs about the others

QP_solition_topic_name = '/qp_solution' # the qp solution topic
QP_info_topic_name = '/qp_info'

start_stop_topic = '/start_stop'

v_setpoint_topic = '/v_setpoint'

QP_SOLN = QP_solution()
LIMO_DATA = limo_info()
OTHER_LIMO_DATA = limo_info_array()

QP_exceptions = 0
QP_soln_cnt = 0

cur_t = 0#rospy.get_time()
last_t = cur_t
start_t = 0

rt = [0, 0, 0]

class project_node:
    def __init__(self):
        self.READY = False
        self.READY_A = False
        self.READY_B = False
        #               u_min, u_max, phiRearEnd, phiLateral, deltaSafetyDistance, v_min, v_max
        self.robot = QP.Robot(-10, 1, 0.3, 0.3, 0.25, 0, 1)
        self.limo_info_sub = rospy.Subscriber(ns+info_topic_name, limo_info, self.limo_info_callb, queue_size=1)
        self.other_limo_data_sub = rospy.Subscriber(ns+MP_info_topic_name, limo_info_array, self.other_limo_data_callb, queue_size=1)
        self.QP_soln_pub = rospy.Publisher(ns+QP_solition_topic_name, QP_solution, queue_size=1)
        self.qp_info_pub = rospy.Publisher(ns+QP_info_topic_name, Float64, queue_size=1)
        self.start_stop_sub = rospy.Subscriber(start_stop_topic, Bool, self.start_stop_callb, queue_size=10)
        # self.v_set_sub = rospy.Subscriber(ns+v_setpoint_topic, Float64, self.v_set_callb, queue_size=1)
        # self.QP_time_pub = rospy.Publisher(ns+QP_dt, Float64, queue_size=1)
        # self.v_set = 0
        self.started = False
    # def v_set_callb(self, float64_msg):
    #     self.v_set = float64_msg.data
    def start_stop_callb(self, callb_msg):
        self.started = callb_msg.data
    def recalc_QP(self):
        global QP_SOLN, QP_exceptions, QP_soln_cnt, rt, last_t, cur_t

        mp_d = LIMO_DATA.mp_dist.data
        my_v = LIMO_DATA.vel.data
        origin_dist = LIMO_DATA.origin_dist.data
        my_pos = (LIMO_DATA.x.data, LIMO_DATA.y.data)
        # bot_path = LIMO_DATA.path.data
        # other_paths = []
        # all_positions = []
        # QP_rows = [] if len(OTHER_LIMO_DATA.limo_infos) != 0 else [[-1,-1,-1, -1]]
        QP_rows = [[-1,-1,-1,-1]]
        # d2s = [] if len(OTHER_LIMO_DATA.limo_infos) != 0 else [-1]
        d2s = [-1]
        for other_limo_data in OTHER_LIMO_DATA.limo_infos:
            o_mp_d = other_limo_data.mp_dist.data
            # other_paths.append(other_limo_data.path.data)
            if other_limo_data.d2.data >= 0:
                d2s.append(other_limo_data.d2.data)
                row = [other_limo_data.ID.data, other_limo_data.origin_dist.data, other_limo_data.vel.data, other_limo_data.d1.data]
            else:
                d2s.append(-1)
                row = [-1,-1,-1,-1]#[other_limo_data.ID.data, other_limo_data.origin_dist.data, other_limo_data.vel.data, other_limo_data.d1.data]
            # all_positions.append((other_limo_data.path.data, (other_limo_data.x.data, other_limo_data.y.data)))
            QP_rows.append(row)
        my_v = min(1, max(0, my_v))
        # my_v = .5
        my_vec = [2.715 - d2s[-1], my_v]
        for d2 in d2s:
            my_vec.append(d2)
        my_vec = np.array(my_vec)
        qp_mat = np.array(QP_rows)
        u = None
        if len(qp_mat) > 1:
            other_v = qp_mat[1][-2]
            other_origin_dist = qp_mat[1][1]
            d1 = qp_mat[1][-1]
            # qp_mat[1][-1] = 1.5452
            d2 = my_vec[-1]
            if d1 <= 0 or d2 <= 0:
                # rospy.logwarn("D1 and D2 must be POSITIVE! (got d1={:^9.3f} and d2={:^9.3f})".format(d1,d2))
                u = 0.1
                # return
            # else:
            #     pass
                # rospy.loginfo("d1={:^7.3f} | d2={:^7.3f} | v={:^7.3f} | other_v={:^7.3f} | my_o={:^7.3f} | other_o={:^7.3f} | (x,y) = ({:^5.3f}, {:^5.3f})".format(d1, d2, my_v, other_v, origin_dist, other_origin_dist, my_pos[0], my_pos[1]))
        # v = my_vec[1]
        # rospy.loginfo("| my_mp_d: {:^-9.4f} | ot_mp_d: {:^-9.4f} |".format(mp_d, o_mp_d))
        if u is None:
            # last_t = cur_t
            cur_t = rospy.get_time()
            # dt = cur_t - last_t
            # rospy.loginfo("dt: {:^8.4f}".format(dt))
            # rospy.loginfo("| d1: {:^-9.4f} | d2: {:^-9.4f} | my_v: {:^-9.4f} |".format(d1, d2, my_v))
            # QP_soln_cnt += 1
            t = cur_t - start_t
            # t = 0.1
            u = self.robot.OCBF_SecondOrderDynamics(qp_mat, my_vec)#, pfunc = rospy.loginfo)#, dprint=True)
            # rt = self.robot.OCBF_SecondOrderDynamics(1, qp_mat, my_vec)#, pfunc = rospy.loginfo)#, dprint=True)
            # L = 2.715
            # d2 = 2.2
            # # d1_fake = 0.236
            # d1_fake = d1
            # # d1_fake = round(d1, 3)
            #
            # # if abs(d1 - 0.23) > 0.1:
            # #     rospy.logwarn("d1 is not near hard coded value -- set to 0.23")
            # #     d1 = 0.23
            # rospy.loginfo("|{:^9.6f}|{:^9.6f}|{:^9.6f}|{:^9.6f}|{:^9.6f}|".format(d1_fake, d1, L-rt[0], rt[1], rt[2]))
            # rt = self.robot.OCBF_SecondOrderDynamics(1,
            #     np.array([
            #         [-1, -1, -1, -1],
            #         [789, 0.96751131, 0, d1_fake]
            #     ]),
            #     [rt[0], rt[1], -1, L - rt[0]]
            # )
            # u = rt[-1]
            # except ValueError:
            #     return
            if u is None:
                QP_exceptions += 1
                rospy.logwarn("EXCEPTIONS: {:^9d}".format(QP_exceptions))
                return
            else:
                pass
                # QP_soln_cnt
                # rospy.loginfo(au_b)
                # rospy.loginfo(u)
                # self.qp_info_pub.publish(Float64(qp_info))


        QP_SOLN.u.data = u

        self.QP_soln_pub.publish(QP_SOLN)
    def limo_info_callb(self, info_msg):
        global LIMO_DATA
        LIMO_DATA = info_msg
        self.READY_A = True
        self.READY = self.READY_A and self.READY_B
        # self.recalc_QP()
    def other_limo_data_callb(self, info_arr_msg):
        global OTHER_LIMO_DATA
        OTHER_LIMO_DATA = info_arr_msg
        self.READY_B = True
        self.READY = self.READY_A and self.READY_B
        # self.recalc_QP()

if __name__ == '__main__':
    rospy.init_node("QP_solver_node")
    node = project_node()
    # rospy.spin()
    while not node.READY:
        rospy.Rate(100)
    while not node.started:
        rospy.Rate(100)
        start_t = rospy.get_time()
    # rospy.spin()
    while not rospy.is_shutdown():
        node.recalc_QP()
        # rospy.Rate(50)
    print("exitting loop")
