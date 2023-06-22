import math
import time

path_straight_up = [(288, 430), (286, 385), (286, 345), (287, 308), (287, 266), (288, 227), (287, 187), (287, 149), (287, 107), (287, 69), (287, 26)]
path_straight_down = [(167, 28), (167, 48), (168, 70), (166, 87), (168, 106), (167, 127), (167, 143), (167, 163), (168, 189), (169, 207), (167, 227), (167, 249), (168, 267), (167, 289), (168, 308), (168, 329), (168, 350), (168, 370), (167, 390), (167, 405), (167, 428)]
path_straight_left = [(427, 166), (407, 167), (390, 167), (369, 167), (346, 166), (328, 166), (308, 166), (289, 165), (267, 166), (247, 164), (228, 166), (207, 167), (187, 167), (167, 167), (146, 167), (129, 167), (107, 167), (87, 167), (67, 167), (50, 167), (28, 167)]
path_straight_right = [(27, 287), (50, 286), (67, 286), (86, 288), (107, 286), (129, 287), (148, 286), (166, 286), (188, 286), (210, 286), (226, 287), (250, 287), (268, 287), (288, 287), (308, 287), (327, 288), (347, 288), (370, 287), (388, 286), (408, 286), (426, 286)]

path_right_up = [(287, 431), (287, 409), (287, 385), (288, 366), (288, 347), (288, 327), (294, 309), (307, 292), (328, 288), (347, 287), (367, 287), (388, 287), (410, 287), (428, 286)]
path_right_down = [(168, 26), (168, 49), (167, 69), (167, 87), (167, 108), (163, 130), (156, 149), (147, 161), (128, 166), (110, 164), (89, 167), (67, 165), (45, 167), (28, 166)]
path_right_left = [(428, 167), (406, 168), (388, 167), (368, 167), (347, 167), (330, 166), (310, 161), (294, 151), (287, 135), (288, 113), (288, 90), (288, 65), (286, 46), (287, 25)]
path_right_right = [(27, 287), (48, 287), (68, 287), (88, 287), (106, 287), (128, 286), (145, 292), (160, 299), (166, 311), (169, 327), (167, 347), (167, 367), (167, 390), (167, 407), (167, 426)]


path_straight = (path_straight_up, path_straight_down, path_straight_left, path_straight_right)
# path_left = ()
path_right = (path_right_up, path_right_down, path_right_left, path_right_right)

def State(direction):
    if direction == 'straight':
        return path_straight
    # elif direction == 'left':
    #     return path_left
    else:
        return path_right    