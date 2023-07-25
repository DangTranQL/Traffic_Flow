#!/usr/bin/env python3
# coding=UTF-8
import math
import numpy as np
from pylimo import limo
import rospy
import re
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

class CAVNode():

    def __init__(self, node_name):
        self.node_name = node_name
        self.position_z = 0
        self.position_x = 0
        self.position_yaw = 0
        self.velocity = 0
        self.acceleration = 0
        self.Receivedata = 0

        # construct publisher
# construct publisher
        rospy.init_node(self.node_name, anonymous=False)
        self.pub = rospy.Publisher('CAV_Data_1',String,queue_size=10) #topic name = CAV_Data
        self.sub = rospy.Subscriber('/vrpn_client_node/Limo_02/pose', PoseStamped, self.callback)

    def run (self):
        message = ("%s %s %s %s" %(self.position_z, self.position_x, self.velocity, self.acceleration))
        self.pub.publish(message)
        #rospy.loginfo(message)

    def callback(self, msg):
        Eul= self.quaternion_to_euler(msg.pose.orientation.x,msg.pose.orientation.y,msg.pose.orientation.z,msg.pose.orientation.w)
        self.position_z = -msg.pose.position.y*1000
        self.position_x = msg.pose.position.x*1000
        self.position_yaw = Eul[2]
        self.Receivedata=1
        #message = '%s %s %s \n' %(self.position_z, self.position_x, self.position_yaw)
        #rospy.loginfo(message)

    def callback2(self, msg):
        message = str(msg)
        temp = re.findall('"([^"]*)"', message)
        temp = temp[0].split()
        self.position_ip_z = float(temp[0])
        self.position_ip_x = float(temp[1])
        self.ip_velocity = float(temp[2])
        self.ip_acceleration = float(temp[3])
        #rospy.loginfo("%s %s %s %s" %(self.position_ip_z, self.position_ip_x, self.ip_velocity, self.ip_acceleration))


    def quaternion_to_euler(self, x, y, z, w):
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        X = math.degrees(math.atan2(t0, t1))

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        Y = math.degrees(math.asin(t2))

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        Z = math.degrees(math.atan2(t3, t4))

        return X, Y, Z

    def getNormalizedSteeringAngle(self,actualAngle):
        if actualAngle<0:
            y = actualAngle/.574
        else:
            y = actualAngle/.8596
        return y

    def steeringAngleToSteeringCommand(self,refAngle):
        x = refAngle
        y = 0.4*x
        return y

    def PIDController2(self, x, x_ref, prev_e, prev_int, delta_t, Kp, Ki, Kd): #add theta_ref as input

        # Tracking error
        e = x_ref - x
        if e <= 1 and e>=-1:
            e_int = 0
        # integral of the error
        e_int = prev_int + e*delta_t

        # anti-windup - preventing the integral error from growing too much
        e_int = max(min(e_int,0.5),-0.5)

        # derivative of the error
        e_der = (e - prev_e)/delta_t

        # controller coefficients
        #Kp = .001
        #Ki = 0
        #Kd = 0.0001

        # PID controller for omega
        u_k = Kp*e
        u_i = Ki*e_int
        u_d = Kd*e_der
        u = Kp*e + Ki*e_int + Kd*e_der

        return u, u_k, u_i, u_d, e, e_int

    def PIDController(self, e, prev_e, prev_int, delta_t, Kp, Ki, Kd): #add theta_ref as input
        if e <= 1 and e>=-1:
            e_int = 0
        # integral of the error
        e_int = prev_int + e*delta_t

        # anti-windup - preventing the integral error from growing too much
        e_int = max(min(e_int,0.5),-0.5)

        # derivative of the error
        e_der = (e - prev_e)/delta_t

        # PID controller for omega
        u_k = Kp*e
        u_i = Ki*e_int
        u_d = Kd*e_der
        u = Kp*e + Ki*e_int + Kd*e_der

        return u, u_k, u_i, u_d, e, e_int

    def vel_ip(self,t):

        #v = -2.459e-06*(t/0.05)**3 + 0.001152*(t/0.05)**2 + -0.1827*(t/0.05) + 20.0
        #v = 0.75*(-2.618e-12*t**8 + 1.255e-09*t**7 + -2.471e-07*t**6 + 2.576e-05*t**5 + -0.001522*t**4 + 0.05008*t**3 + -0.8075*t**2 + 3.479*t + 60.0)
        #v = 0*t +
        v=[1,
        0.95,
        0.9,
        0.85,
        0.8,
        0.75,
        0.7,
        0.65,
        0.6,
        0.55,
        0.5,
        0.45,
        0.4,
        0.35,
        0.3,
        0.25,
        0.2,
        0.25,
        0.3,
        0.35,
        0.4,
        0.45,
        0.5,
        0.55,
        0.6,
        0.65,
        0.7,
        0.75,
        0.8,
        0.85,
        0.9,
        0.95,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1]
        v=[45,
        42.6737722102789,
        40.3995252032583,
        37.8176368165554,
        35.8394152921692,
        34.7125478518746,
        33.5748515531829,
        32.6964195746972,
        32.7549780807449,
        32.1601105646737,
        30.5005722157318,
        29.4574400978314,
        27.0156680968869,
        25.7739459613037,
        25.4044766536586,
        24.7471479702784,
        24.5225072350171,
        24.5698874340449,
        24.3565808844202,
        23.2379942036987,
        23.2270180094179,
        23.7495825958504,
        23.7937136917195,
        23.8417083160883,
        22.9172074968420,
        22.9716514487450,
        22.9798112355021,
        22.6345792743095,
        22.7832166888715,
        23.2281746170485,
        23.6589841056309,
        23.7586902380757,
        23.6763340957891,
        23.2035817870352,
        23.1111229599860,
        22.5268566683617,
        22.4129837144848,
        23.1212193712114,
        23.2070958342689,
        22.4807418271275,
        22.5340946689757,
        22.1457735689179,
        22.3082690908568,
        22.7696127805802,
        22.9851130130690,
        22.3670382157850,
        22.8266194831664,
        22.5553507785624,
        22.9093710976191,
        23.2312017761899,
        23.6106941089980,
        23.6413504418668,
        23.1773599088134,
        23.3080011323710,
        23.4146321734798,
        23.4551602827201,
        23.4761685731945,
        23.6566427575619,
        23.4074189480231,
        22.7297080717492,
        22.7939804244489,
        23.0025095191951,
        23.0025095191951,
        23.0025095191951,
        23.0025095191951,
        23.0025095191951,
        23.0025095191951,
        23.0025095191951,
        23.0025095191951,
        23.0025095191951]
        return 0.01*v[cnt]

    def e2steer(self,e,bias,e_yaw,eprev_lateral,eint_lateral,eprev_yaw,eint_yaw,dt):
        if (eprev_lateral*e<=0):
            eint_lateral = 0
        if (eprev_yaw*e_yaw<=0):
            eint_yaw = 0
        if e<=170 and e>=-170:
            if (e<=0 and e_yaw<=0) or (e>0 and e_yaw>0):
                kp_lateral = -0.0001517647 /v_ref
                kint_lateral = -0#.00001/v_ref
                kd_lateral = 0
                kp_yaw = -0.006 #/v_ref
                kint_yaw = -.0#001/v_ref
                kd_yaw = 0
            elif (e<=0 and e_yaw>0) or (e>0 and e_yaw<0):
                kp_lateral = -0.0001517647/ v_ref
                kint_lateral = -0.0#0001/v_ref
                kd_lateral = 0
                kp_yaw = -0.002 #/v_ref
                kint_yaw = -.00#01/v_ref
                kd_yaw = 0
            [steer_lateral, u_k, u_i, u_d, eprev_lateral, eint_lateral] = self.PIDController(e, eprev_lateral, eint_lateral, dt, kp_lateral, kint_lateral, kd_lateral)
            [steer_yaw, u_k, u_i, u_d, eprev_yaw, eint_yaw] = self.PIDController(e_yaw, eprev_yaw, eint_yaw, dt, kp_yaw, kint_yaw, kd_yaw)
            steer =  steer_lateral + steer_yaw
        elif e>=170:
            steer=-0.25+bias
        elif e<=-170:
            steer=0.25+bias
        return [steer,eprev_lateral,eint_lateral,eprev_yaw,eint_yaw]

    def e2steer(self,e,bias,eprev_lateral,eint_lateral,dt):
        if (eprev_lateral*e<=0):
            eint_lateral = 0
        kp = -0.0005
        ki = -0.0001
        kd = -0.005
        [ref_steer,u_k ,u_i ,u_d, eprev_lateral, eint_lateral] = self.PIDController(e, eprev_lateral, eint_lateral, dt, kp, ki, kd)
        return ref_steer, eprev_lateral, eint_lateral

if __name__ == '__main__':

    bias = 0
    e = 0
    eprev_lateral = 0
    eint_lateral = 0
    e_yaw = 0
    eprev_yaw = 0
    eint_yaw = 0
    dt = 0.05
    cnt = 0
    i = 0
    v_ref = 0
    v = 0
    ref_steer = 0
    steer = 0
    e_int =0
    stop = 0
    limo=limo.LIMO()
    limo.EnableCommand()         # 使能控制s

    # create the node
    CAV = CAVNode(node_name='CAV1_1')
    transmissionRate = 30
    rate = rospy.Rate(transmissionRate) # 1Hz

    while CAV.Receivedata == 0:
        print("no localization")
    bias_x  = CAV.position_x
    bias_z  = CAV.position_z

    # keep spinning
    while not rospy.is_shutdown():
        if i >= 5:
            cnt = cnt + 1
            #v_ref=CAV.vel_ip(cnt)
            v_ref=0.5
            i = 0
        if (CAV.position_x <= 187 and CAV.position_x>= -537) and CAV.position_z >= 1500 and CAV.position_z <= 6150:
            e=-(CAV.position_x+144)
            [ref_steer,eprev_lateral,eint_lateral]=CAV.e2steer(e,bias,eprev_lateral,eint_lateral,dt)
            print("I am 1")
            #print("%s %s"%(CAV.position_x,bias_x))
        elif CAV.position_z > 850 and abs(CAV.position_yaw) >= 110:
            if CAV.position_yaw <= 180 and CAV.position_yaw >= 0:
                CAV.position_yaw = - CAV.position_yaw
            Kp=-0.1
            Ki=-0.005
            Kd=-0.001
            [ref_steer,u_k ,u_i ,u_d, e_yaw, e_int]=CAV.PIDController2(CAV.position_yaw, -90, e_yaw, e_int, dt, Kp, Ki, Kd)
            ref_steer= 0.7*max(min(ref_steer,1),-1)
            print("I am 2")
        elif CAV.position_x < 2150 and CAV.position_z < 850:
            print("%s %s"%(CAV.position_x,CAV.position_yaw))
            e=-(CAV.position_z-750)
            [ref_steer,eprev_lateral,eint_lateral]=CAV.e2steer(e,bias,eprev_lateral,eint_lateral,dt)
            print("I am 3")
        elif CAV.position_x > 2050 and CAV.position_z < 1310 and abs(CAV.position_yaw) >= 5:
            if CAV.position_yaw <= 180 and CAV.position_yaw >= 0:
                CAV.position_yaw = - CAV.position_yaw
            Kp=-0.1
            Ki=-0.005
            Kd=-0.001
            [ref_steer,u_k ,u_i ,u_d, e_yaw, e_int]=CAV.PIDController2(CAV.position_yaw, 0, e_yaw, e_int, dt, Kp, Ki, Kd)
            ref_steer= 0.9*max(min(ref_steer,1),-1)
        elif CAV.position_z > 1310 and CAV.position_z <= 6040:
            e=(CAV.position_x-2710)
            [ref_steer,eprev_lateral,eint_lateral]=CAV.e2steer(e,bias,eprev_lateral,eint_lateral,dt)
            if CAV.position_z <= 5000:
                v_ref=0.5
            else:
                v_ref=0.5
        elif CAV.position_x >= 2220 and CAV.position_z >= 6040 and abs(CAV.position_yaw) <= 80:
            Kp=0.1
            Ki=0.005
            Kd=0.001
            [ref_steer,u_k ,u_i ,u_d, e_yaw, e_int]=CAV.PIDController2(CAV.position_yaw, -90, e_yaw, e_int, dt, Kp, Ki, Kd)
            ref_steer= 0.7*max(min(ref_steer,1),-1)
            #print("%s %s %s"%(CAV.position_x,CAV.position_yaw,CAV.position_z))
        elif (CAV.position_x < 2220 or abs(CAV.position_yaw) <= 10) and CAV.position_x >= 300:
            print("%s %s %s"%(CAV.position_x,CAV.position_z,CAV.position_yaw))
            e=(CAV.position_z-6690)
            [ref_steer,eprev_lateral,eint_lateral]=CAV.e2steer(e,bias,eprev_lateral,eint_lateral,dt)
        elif CAV.position_x <= 400 and CAV.position_z>= 6150 and abs(CAV.position_yaw) >= 10:
            Kp=0.1
            Ki=0.005
            Kd=0.001
            [ref_steer,u_k ,u_i ,u_d, e_yaw, e_int]=CAV.PIDController2(CAV.position_yaw, -180, e_yaw, e_int, dt, Kp, Ki, Kd)
            ref_steer= 1.1*max(min(ref_steer,1),-1)
        else:
            stop= 1
        v = limo.GetLinearVelocity()

        #print("%s %s %s %s"%(e,e_yaw,ref_steer,CAV.steeringAngleToSteeringCommand(ref_steer)))
        if (stop == 0):
            limo.SetMotionCommand(v_ref,0,0,CAV.steeringAngleToSteeringCommand(ref_steer))
        else:
            limo.SetMotionCommand(0,0,0,CAV.steeringAngleToSteeringCommand(ref_steer))
        i = i +1
        CAV.run()
        rate.sleep()
    rospy.spin()
