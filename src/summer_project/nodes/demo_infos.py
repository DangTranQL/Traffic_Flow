import rospy
import numpy as np
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64MultiArray, String, Float64, MultiArrayDimension
from summer_project.msg import limo_info, limo_info_array

LIMO_IDs = [789, 155]

limo_info_topics = ["LIMO_000{}/limo_info".format(ID) for ID in LIMO_IDs]

class project_node:
    def __init__(self):
