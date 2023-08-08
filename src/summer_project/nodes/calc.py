import math, circle
from itertools import groupby
from collections import defaultdict

turning_pts_right = [
    [-0.574, 2.354],
    [-2.26, 2.895],
    [-1.715, 4.386],
    [-0.269, 4.024]
]
turning_pts_left = [
    [-0.592, 2.93],
    [-1.707, 2.908],
    [-1.718, 4.047],
    [-0.612, 4.04]
]
right = [
    [-0.179, 2.929],
    [-1.715, 2.512],
    [-2.132, 4.022],
    [-0.609, 4.434]
]
left = [
    [-1.713, 4.05],
    [-0.607, 4.053],
    [-0.57, 2.9],
    [-1.702, 2.893]
]

left_circle, right_circle = circle.circle_lst()
border = [(-1.7,1.06), (-3.39,4.015), (-0.62,5.675), (0.7, 2.93)]

start_A = [-0.557,1.314]
start_B = [-3.294,2.89]
start_C = [-1.722,5.624]
start_D = [0.753,4.044]

pts_lst = {
    "1": (-0.579, 2.94),
    "2": (-0.228, 2.93),
    "3": (-0.604, 4.035),
    "4": (-0.608, 4.447),
    "5": (-1.078, 3.468),
    "6": (-1.73, 4.05),
    "7": (-2.14, 4.034),
    "8": (-1.72, 2.91),
    "9": (-1.72, 2.516),
    "10": (-0.574, 2.354),
    "11": (-2.26, 2.895),
    "12": (-1.715, 4.386),
    "13": (-0.269, 4.024)
}

merging_pts = {
    "straight_A": [pts_lst["1"], pts_lst["3"], pts_lst["4"]],
    "right_A": [pts_lst["2"]],
    "left_A": [pts_lst["1"], pts_lst["5"], pts_lst["6"], pts_lst["7"]],
    "straight_B": [pts_lst["8"], pts_lst["1"], pts_lst["2"]],
    "right_B": [pts_lst["9"]],
    "left_B": [pts_lst["8"], pts_lst["5"], pts_lst["3"], pts_lst["4"]],
    "straight_C": [pts_lst["6"], pts_lst["8"], pts_lst["9"]],
    "right_C": [pts_lst["7"]],
    "left_C": [pts_lst["6"], pts_lst["5"], pts_lst["1"], pts_lst["2"]],
    "straight_D": [pts_lst["3"], pts_lst["6"], pts_lst["7"]],
    "right_D": [pts_lst["4"]],
    "left_D": [pts_lst["3"], pts_lst["5"], pts_lst["8"], pts_lst["9"]]
}

merging_pts_copy = {
    "straight_A": [pts_lst["1"], pts_lst["3"], pts_lst["4"]],
    "right_A": [pts_lst["2"]],
    "left_A": [pts_lst["1"], pts_lst["5"], pts_lst["6"], pts_lst["7"]],
    "straight_B": [pts_lst["8"], pts_lst["1"], pts_lst["2"]],
    "right_B": [pts_lst["9"]],
    "left_B": [pts_lst["8"], pts_lst["5"], pts_lst["3"], pts_lst["4"]],
    "straight_C": [pts_lst["6"], pts_lst["8"], pts_lst["9"]],
    "right_C": [pts_lst["7"]],
    "left_C": [pts_lst["6"], pts_lst["5"], pts_lst["1"], pts_lst["2"]],
    "straight_D": [pts_lst["3"], pts_lst["6"], pts_lst["7"]],
    "right_D": [pts_lst["4"]],
    "left_D": [pts_lst["3"], pts_lst["5"], pts_lst["8"], pts_lst["9"]]
}


pts_filter = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

merging_filter = {
    "straight_A": [pts_filter["1"], pts_filter["3"], pts_filter["4"]],
    "right_A": [pts_filter["2"]],
    "left_A": [pts_filter["1"], pts_filter["5"], pts_filter["6"], pts_filter["7"]],
    "straight_B": [pts_filter["8"], pts_filter["1"], pts_filter["2"]],
    "right_B": [pts_filter["9"]],
    "left_B": [pts_filter["8"], pts_filter["5"], pts_filter["3"], pts_filter["4"]],
    "straight_C": [pts_filter["6"], pts_filter["8"], pts_filter["9"]],
    "right_C": [pts_filter["7"]],
    "left_C": [pts_filter["6"], pts_filter["5"], pts_filter["1"], pts_filter["2"]],
    "straight_D": [pts_filter["3"], pts_filter["6"], pts_filter["7"]],
    "right_D": [pts_filter["4"]],
    "left_D": [pts_filter["3"], pts_filter["5"], pts_filter["8"], pts_filter["9"]]
}

#starting location to all merging points on a path
def start_to_all_merging(path):
    index = ord(path[-1])-65
    if "A" in path:
        x,y = start_A
    elif "B" in path:
        x,y = start_B
    elif "C" in path:
        x,y = start_C
    else:
        x,y = start_D
    distances = []
    if "right" in path:
        if "A" in path or "C" in path:
            distances.append(abs(y-turning_pts_right[index][1]) + circle.arc_length(right_circle[index], turning_pts_right[index], merging_pts[path][0]))
        else:
            distances.append(abs(x-turning_pts_right[index][0]) + circle.arc_length(right_circle[index], turning_pts_right[index], merging_pts[path][0]))
    elif "left" in path:
        if "A" in path or "C" in path:
            distances.append(abs(y-merging_pts[path][0][1]))
            distances.append(abs(y-merging_pts[path][0][1]) + circle.arc_length(left_circle[index], merging_pts[path][0], merging_pts[path][1]))
            distances.append(abs(y-merging_pts[path][0][1]) + circle.arc_length(left_circle[index], merging_pts[path][0], merging_pts[path][2]))
            distances.append(abs(y-merging_pts[path][0][1]) + circle.arc_length(left_circle[index], merging_pts[path][0], merging_pts[path][2]) + abs(x-merging_pts[path][3][0]))
        else:
            distances.append(abs(x-merging_pts[path][0][0]))
            distances.append(abs(x-merging_pts[path][0][0]) + circle.arc_length(left_circle[index], merging_pts[path][0], merging_pts[path][1]))
            distances.append(abs(x-merging_pts[path][0][0]) + circle.arc_length(left_circle[index], merging_pts[path][0], merging_pts[path][2]))
            distances.append(abs(x-merging_pts[path][0][0]) + circle.arc_length(left_circle[index], merging_pts[path][0], merging_pts[path][2]) + abs(y-merging_pts[path][3][1]))
    else:
        if "A" in path or "C" in path:
            distances.append(abs(y-merging_pts[path][0][1]))
            distances.append(abs(y-merging_pts[path][1][1]))
            distances.append(abs(y-merging_pts[path][2][1]))
        else:
            distances.append(abs(x-merging_pts[path][0][0]))
            distances.append(abs(x-merging_pts[path][1][0]))
            distances.append(abs(x-merging_pts[path][2][0]))
    return distances

#starting location to any merging point
def start_to_any_merge(path, pos):
    distances = start_to_all_merging(path)
    index = merging_pts[path].index(pos)
    return distances[index]

#robot to starting location
def dst_to_start(pos, path):
    x,y = pos
    if path == "straight_A":
        return y-start_A[1]
    elif path == "straight_B":
        return x-start_B[0]
    elif path == "straight_C":
        return start_C[1]-y
    elif path == "straight_D":
        return start_D[0]-x
    elif path == "right_A":
        if y < turning_pts_right[0][1]:
            return y-start_A[1]
        else:
            if x > right[0][0]:
                return (turning_pts_right[0][1]-start_A[1])+circle.arc_length(right_circle[0],turning_pts_right[0],right[0])+(x-right[0][0])
            else:
                return (turning_pts_right[0][1]-start_A[1])+circle.arc_length(right_circle[0],turning_pts_right[0],(x,y))
    elif path == "right_B":
        if x < turning_pts_right[1][0]:
            return x-start_B[0]
        else:
            if y < right[1][1]:
                return (turning_pts_right[1][0]-start_B[0])+circle.arc_length(right_circle[1],turning_pts_right[1],right[1])+(right[1][1]-y)
            else:
                return (turning_pts_right[1][0]-start_B[0])+circle.arc_length(right_circle[1],turning_pts_right[1],(x,y))
    elif path == "right_C":
        if y > turning_pts_right[2][1]:
            return start_C[1]-y
        else:
            if x < right[2][0]:
                return (start_C[1]-y)+circle.arc_length(right_circle[2],turning_pts_right[2],right[2])+(right[2][0]-x)
            else:
                return (start_C[1]-y)+circle.arc_length(right_circle[2],turning_pts_right[2],(x,y))
    elif path == "right_D":
        if x > turning_pts_right[3][0]:
            return start_D[0]-x
        else:
            if y > right[3][1]:
                return (start_D[0]-x)+circle.arc_length(right_circle[3],turning_pts_right[3],right[3])+(y-right[3][1])
            else:
                return (start_D[0]-x)+circle.arc_length(right_circle[3],turning_pts_right[3],(x,y))

    elif path == "left_A":
        if y < turning_pts_left[0][1]:
            return y-start_A[1]
        else:
            if x < left[0][0]:
                return (turning_pts_left[0][1]-start_A[1])+circle.arc_length(left_circle[0],turning_pts_left[0],left[0])+(left[0][0]-x)
            else:
                return (turning_pts_left[0][1]-start_A[1])+circle.arc_length(left_circle[0],turning_pts_left[0],(x,y))
    elif path == "left_B":
        if x < turning_pts_left[1][0]:
            return x-start_B[0]
        else:
            if y > left[1][1]:
                return (turning_pts_left[1][0]-start_B[0])+circle.arc_length(left_circle[1],turning_pts_left[1],left[1])+(y-left[1][1])
            else:
                return (turning_pts_left[1][0]-start_B[0])+circle.arc_length(left_circle[1],turning_pts_left[1],(x,y))
    elif path == "left_C":
        if y > turning_pts_left[2][1]:
            return start_C[1]-y
        else:
            if x > left[2][0]:
                return (start_C[1]-turning_pts_left[2][1])+circle.arc_length(left_circle[2],turning_pts_left[2],left[2])+(x-left[2][0])
            else:
                return (start_C[1]-turning_pts_left[2][1])+circle.arc_length(left_circle[2],turning_pts_left[2],(x,y))
    elif path == "left_D":
        if x > turning_pts_left[3][0]:
            return start_D[0]-x
        else:
            if y < left[3][1]:
                return (start_D[0]-turning_pts_left[3][0])+circle.arc_length(left_circle[3],turning_pts_left[3],left[3])+(left[3][1]-y)
            else:
                return (start_D[0]-turning_pts_left[3][0])+circle.arc_length(left_circle[3],turning_pts_left[3],(x,y))

#distance from robot to any merging point
def dst_to_merge(pos, path, merge):
    distances = start_to_all_merging(path)
    merge_index = merging_pts[path].index(merge)
    return distances[merge_index] - dst_to_start(pos,path)

#robot to closest merging point
def merging_dst(pos, path):
    if "straight" in path:
        if len(merging_pts_copy[path]) != 0:
            d = dst_to_merge(pos, path, merging_pts_copy[path][0])
            if d <= 0.15:
                merging_pts_copy[path].pop(0)
        else:
            d=0
    elif "right" in path:
        if len(merging_pts_copy[path]) != 0:
            d = dst_to_merge(pos, path, merging_pts_copy[path][0])
            if d <= 0.15:
                merging_pts_copy[path].pop()
        else:
            d = 0
    elif "left" in path:
        if len(merging_pts_copy[path]) != 0:
            d = dst_to_merge(pos, path, merging_pts_copy[path][0])
            if d <= 0.15:
                merging_pts_copy[path].pop(0)
        else:
            d=0
    return d

def section(pos, path):
    x,y = pos
    if path == "right_A":
        if y < turning_pts_right[0][1]:
            return "vertical"
        else:
            if x <= right[0][0]:
                return "circle"
            else:
                return "horizontal"
    elif path == "right_B":
        if x <= turning_pts_right[1][0]:
            return "horizontal"
        else:
            if y > right[1][1]:
                return "circle"
            else:
                return "vertical"
    elif path == "right_C":
        if y > turning_pts_right[2][1]:
            return "vertical"
        else:
            if x >= right[2][0]:
                return "circle"
            else:
                return "horizontal"
    elif path == "right_D":
        if x > turning_pts_right[3][0]:
            return "horizontal"
        else:
            if y <= right[3][1]:
                return "circle"
            else:
                return "vertical"
    elif path == "left_A":
        if y < turning_pts_left[0][1]:
            return "vertical"
        else:
            if x >= left[0][0]:
                return "circle"
            else:
                return "horizontal"
    elif path == "left_B":
        if x < turning_pts_left[1][0]:
            return "horizontal"
        else:
            if y <= left[1][1]:
                return "circle"
            else:
                return "vertical"
    elif path == "left_C":
        if y > turning_pts_left[2][1]:
            return "vertical"
        else:
            if x <= left[2][0]:
                return "circle"
            else:
                return "horizontal"
    elif path == "left_D":
        if x > turning_pts_left[3][0]:
            return "horizontal"
        else:
            if y >= left[3][1]:
                return "circle"
            else:
                return "vertical"

#signed error distance
def signed_dist(pos, path, stop_d = 0.2):
    global previous_pnt
    global total_d
    if previous_pnt is None:
        previous_pnt = pos
    x,y = pos
    stop = False
    pid = ["straight", "right", "left"]
    d = merging_dst(pos, path)
    travel_d = dst_to_start(pos, path)
    if path == "straight_A":
        if abs(y-border[2][1]) <= stop_d:
            stop = True
        return x - turning_pts_right[0][0], d, travel_d, stop, pid[0]
    elif path == "straight_B":
        if abs(x-border[3][0]) <= stop_d:
            stop = True
        return -(y - turning_pts_right[1][1]), d, travel_d, stop, pid[0]
    elif path == "straight_C":
        if abs(y-border[0][1]) <= stop_d:
            stop = True
        return -(x - turning_pts_right[2][0]), d, travel_d, stop, pid[0]
    elif path == "straight_D":
        if abs(x-border[1][0]) <= stop_d:
            stop = True
        return y - turning_pts_right[3][1], d, travel_d, stop, pid[0]

    elif path == "right_A":
        if abs(x-border[3][0]) <= stop_d:
            stop = True
        if y < turning_pts_right[0][1]:
            return x - turning_pts_right[0][0], d, travel_d, stop, pid[0]
        else:
            if x > right[0][0]:
                return -(y - right[0][1]), d, travel_d, stop, pid[0]
            else:
                return -(math.sqrt((x-right_circle[0][1][0])**2 + (y-right_circle[0][1][1])**2) - right_circle[0][0]), d, travel_d, stop, pid[1]
    elif path == "right_B":
        if abs(y-border[0][1]) <= stop_d:
            stop = True
        if x < turning_pts_right[1][0]:
            return -(y - turning_pts_right[1][1]), d, travel_d, stop, pid[0]
        else:
            if y < right[1][1]:
                return -(x - right[1][0]), d, travel_d, stop, pid[0]
            else:
                return -(math.sqrt((x-right_circle[1][1][0])**2 + (y-right_circle[1][1][1])**2) - right_circle[1][0]), d, travel_d, stop, pid[1]
    elif path == "right_C":
        if abs(x-border[1][0]) <= stop_d:
            stop = True
        if y > turning_pts_right[2][1]:
            return -(x - turning_pts_right[2][0]), d, travel_d, stop, pid[0]
        else:
            if x < right[2][0]:
                return (y - right[2][1]), d, travel_d, stop, pid[0]
            else:
                return -(math.sqrt((x-right_circle[2][1][0])**2 + (y-right_circle[2][1][1])**2) - right_circle[2][0]), d, travel_d, stop, pid[1]
    elif path == "right_D":
        if abs(y-border[2][1]) <= stop_d:
            stop = True
        if x > turning_pts_right[3][0]:
            return y - turning_pts_right[3][1], d, travel_d, stop, pid[0]
        else:
            if y > right[3][1]:
                return x - right[3][0], d, travel_d, stop, pid[0]
            else:
                return -(math.sqrt((x-right_circle[3][1][0])**2 + (y-right_circle[3][1][1])**2) - right_circle[3][0]), d, travel_d, stop, pid[1]

    elif path == "left_A":
        if abs(x-border[1][0]) <= stop_d:
            stop = True
        if y < turning_pts_left[0][1]:
            return x - turning_pts_left[0][0], d, travel_d, stop, pid[0]
        else:
            if x < left[0][0]:
                return y - left[0][1], d, travel_d, stop, pid[0]
            else:
                return math.sqrt((x-left_circle[0][1][0])**2 + (y-left_circle[0][1][1])**2) - left_circle[0][0], d, travel_d, stop, pid[2]
    elif path == "left_B":
        if abs(y-border[2][1]) <= stop_d:
            stop = True
        if x < turning_pts_left[1][0]:
            return -(y - turning_pts_left[1][1]), d, travel_d, stop, pid[0]
        else:
            if y > left[1][1]:
                return x - left[1][0], d, travel_d, stop, pid[0]
            else:
                return math.sqrt((x-left_circle[1][1][0])**2 + (y-left_circle[1][1][1])**2) - left_circle[1][0], d, travel_d, stop, pid[2]
    elif path == "left_C":
        if abs(x-border[3][0]) <= stop_d:
            stop = True
        if y > turning_pts_left[2][1]:
            return -(x - turning_pts_left[2][0]), d, travel_d, stop, pid[0]
        else:
            if x > left[2][0]:
                return -(y - left[2][1]), d, travel_d, stop, pid[0]
            else:
                return math.sqrt((x-left_circle[2][1][0])**2 + (y-left_circle[2][1][1])**2) - left_circle[2][0], d, travel_d, stop, pid[2]
    elif path == "left_D":
        if abs(y-border[0][1]) <= stop_d:
            stop = True
        if x > turning_pts_left[3][0]:
            return y - turning_pts_left[3][1], d, travel_d, stop, pid[0]
        else:
            if y < left[3][1]:
                return -(x - left[3][0]), d, travel_d, stop, pid[0]
            else:
                return math.sqrt((x-left_circle[3][1][0])**2 + (y-left_circle[3][1][1])**2) - left_circle[3][0], d, travel_d, stop, pid[2]

#d2, d1 calculation
def common_merge(main, others):
    all_dst = []
    common = []
    for i in others:
        each_common = []
        dst = []
        if (("straight" in main[0] and "right" in i[0]) or ("right" in main[0] and "straight" in i[0]) or (("straight" in main[0] and "straight" in i[0]))) and (main[0][-1] == i[0][-1]):
            d2 = dst_to_start(main[2], main[0])
            d1 = dst_to_start(i[2], i[0])
            dst.append([i[1], d2, d1,i[3]])
            each_common.append("same_line")
        else:
            for j in merging_pts[i[0]]:
                if j in merging_pts[main[0]]:
                    d2 = dst_to_merge(main[2], main[0], j)
                    d1 = dst_to_merge(i[2], i[0], j)
                    if d2 > 0:
                        dst.append([i[1], d2, d1,i[3]])
                        each_common.append(merging_filter[main[0]][merging_pts[main[0]].index(j)])

        if len(dst) != 0:
            all_dst.append(dst)                     #all_dst = [[[id, d2, d1(1), vel], [id, d2, d1(2), vel], [id, d2, d1(1), vel]]  main and others[0]
            common.append(each_common)              #           [[id, d2, d1(1), vel], [id, d2, d1(2), vel], [id, d2, d1(1), vel]]  main and others[1]

    t = defaultdict(list)
    for i in all_dst:                               #dict(t) = {'others[0] ID': [id, d2, d1(1), vel], [id, d2, d1(2), vel], [id, d2, d1(1), vel]
        for j in i:                                 #           'others[1] ID': [id, d2, d1(1), vel], [id, d2, d1(2), vel], [id, d2, d1(1), vel]}
            t[j[0]].append(j)

    return all_dst, dict(t), common

# reformatting
def ip(main, others):
    dst, _, common = common_merge(main, others)
    flatten = []
    l = []
    for i in range(len(dst)):
        for j in range(len(dst[i])):
            dst[i][j].append(common[i][j])
            flatten.append(dst[i][j])
    res = defaultdict(list)
    for i in dst:
        for ele in i:
            res[ele[-1]].append(ele)
    for i in res:
        res[i].sort(key = lambda x: abs(x[2]))

    for i in dict(res):
        if i != "same_line":
            l.append(start_to_any_merge(main[0],pts_lst[i]))
                                               #l = [start to common merging point 1, start to common merging point 2, etc]
    return dict(res), l                        #dict(res) = {'merging point ID': [[robot1 ID, d2, d1, vel, merging point ID], [robot2 ID, d2, d1, vel, merging point ID]]}


# x,_,c = common_merge(["straight_B", 770, (-3,2.919), 0.01], [["straight_B", 789, (-2,2.919),0]])
# print(x)

x, l = ip(["straight_B", 770, (-3,2.919), 0.01], [["right_B", 789, (-2,2.919),0], ["straight_B", 710, (-2,2.919),0], ["straight_A", 111, (-2,2.919),0]])
print(x)
