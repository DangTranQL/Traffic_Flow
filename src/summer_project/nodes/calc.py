import math, circle

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

pts_lst = {
    "1": (-0.579, 2.94, 1),
    "2": (-0.228, 2.93, 2),
    "3": (-0.604, 4.035, 3),
    "4": (-0.608, 4.447, 4),
    "5": (-1.078, 3.468, 5),
    "6": (-1.73, 4.05, 6),
    "7": (-2.14, 4.034, 7),
    "8": (-1.72, 2.91, 8),
    "9": (-1.72, 2.516, 9)
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

dist = lambda p0, p1: ((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)**0.5

def merging_dst(pos, path):
    x,y = pos
    index = ord(path[-1])-65
    merging_pts_copy = merging_pts
    if "straight" in path:
        if len(merging_pts_copy[path]) != 0:
            d = math.sqrt((x-merging_pts_copy[path][0][0])**2 + (y-merging_pts_copy[path][0][1])**2)
            if d <= 0.15:
                merging_pts_copy[path].pop(0)
        else:
            d=0
    elif "right" in path:
        if len(merging_pts_copy[path]) != 0:
            if ("A" in path and y < turning_pts_right[0][1]) or ("C" in path and y > turning_pts_right[2][1]):
                d = abs(y-turning_pts_right[index][1]) + circle.arc_length(right_circle[index], turning_pts_right[index], merging_pts_copy[path][0])
            elif ("B" in path and x < turning_pts_right[1][0]) or ("D" in path and x > turning_pts_right[3][0]):
                d = abs(x-turning_pts_right[index][0]) + circle.arc_length(right_circle[index], turning_pts_right[index], merging_pts_copy[path][0])
            else:
                if ("A" in path and x < right[0][0]) or ("C" in path and x > right[2][0]) or ("B" in path and y > right[1][1]) or ("D" in path and y < right[3][1]):
                    d = circle.arc_length(right_circle[index], (x,y), merging_pts_copy[path][0])
                else:
                    d = 0

            if d <= 0.15:
                merging_pts_copy[path].pop()
        else:
            d = 0
    elif "left" in path:
        if len(merging_pts_copy[path]) != 0:
            if ("A" in path and y < turning_pts_left[0][1]) or ("C" in path and y > turning_pts_left[2][1]):
                d = abs(y-merging_pts_copy[path][0][1])
            elif ("B" in path and x < turning_pts_right[1][0]) or ("D" in path and x > turning_pts_right[3][0]):
                d = abs(x-merging_pts_copy[path][0][0])
            elif ("A" in path and x < left[0][0]) or ("C" in path and x > left[2][0]):
                d = abs(x-merging_pts_copy[path][0][0])
            elif ("B" in path and y > left[1][1]) or ("D" in path and y < left[3][1]):
                d = abs(y-merging_pts_copy[path][0][1])
            else:
                d = circle.arc_length(left_circle[index], (x,y), merging_pts[path][0])

            if d <= 0.15:
                merging_pts_copy[path].pop(0)
        else:
            d=0
    return d

previous_pnt = None
total_d = 0

start_A = [-0.557,1.314]
start_B = [-3.294,2.89]
start_C = [-1.722,5.624]
start_D = [0.753,4.044]

def signed_dist(pos, path, v=1, stop_d = 0.2):
    global previous_pnt
    global total_d
    if previous_pnt is None:
        previous_pnt = pos
    if dist(previous_pnt, pos) < 0.01:
        v = 0
    # if v != 0:
        # pos = previous_pnt
    x,y = pos
    stop = False
    pid = ["straight", "right", "left"]
    # try:
    d = merging_dst(pos, path)
    # except ValueError:
    #     d = 1e9
    if path == "straight_A":
        if abs(y-border[2][1]) <= stop_d:
            stop = True
        return x - turning_pts_right[0][0], d, y-start_A[1], stop, pid[0]
    elif path == "straight_B":
        if abs(x-border[3][0]) <= stop_d:
            stop = True
        return -(y - turning_pts_right[1][1]), d, x-start_B[0], stop, pid[0]
    elif path == "straight_C":
        if abs(y-border[0][1]) <= stop_d:
            stop = True
        return -(x - turning_pts_right[2][0]), d, start_C[1]-y, stop, pid[0]
    elif path == "straight_D":
        if abs(x-border[1][0]) <= stop_d:
            stop = True
        return y - turning_pts_right[3][1], d, start_D[0]-x, stop, pid[0]

    elif path == "right_A":
        if abs(x-border[3][0]) <= stop_d:
            stop = True
        if y < turning_pts_right[0][1]:
            return x - turning_pts_right[0][0], d, y-start_A[1], stop, pid[0]
        else:
            if x > right[0][0]:
                return -(y - right[0][1]), d, (turning_pts_right[0][1]-start_A[1])+circle.arc_length(right_circle[0],turning_pts_right[0],right[0])+(x-right[0][0]), stop, pid[0]
            else:
                return -(math.sqrt((x-right_circle[0][1][0])**2 + (y-right_circle[0][1][1])**2) - right_circle[0][0]), d, (turning_pts_right[0][1]-start_A[1])+circle.arc_length(right_circle[0],turning_pts_right[0],right[0]), stop, pid[1]
    elif path == "right_B":
        if abs(y-border[0][1]) <= stop_d:
            stop = True
        if x < turning_pts_right[1][0]:
            return -(y - turning_pts_right[1][1]), d, x-start_B[0], stop, pid[0]
        else:
            if y < right[1][1]:
                return -(x - right[1][0]), d, total_d, (turning_pts_right[1][0]-start_B[0])+circle.arc_length(right_circle[1],turning_pts_right[1],right[1])+(right[1][1]-y), stop, pid[0]
            else:
                return -(math.sqrt((x-right_circle[1][1][0])**2 + (y-right_circle[1][1][1])**2) - right_circle[1][0]), d, (turning_pts_right[1][0]-start_B[0])+circle.arc_length(right_circle[1],turning_pts_right[1],right[1]), stop, pid[1]
    elif path == "right_C":
        if abs(x-border[1][0]) <= stop_d:
            stop = True
        if y > turning_pts_right[2][1]:
            return -(x - turning_pts_right[2][0]), d, start_C[1]-y, stop, pid[0]
        else:
            if x < right[2][0]:
                return (y - right[2][1]), d, (start_C[1]-y)+circle.arc_length(right_circle[2],turning_pts_right[2],right[2])+(right[2][0]-x), stop, pid[0]
            else:
                return -(math.sqrt((x-right_circle[2][1][0])**2 + (y-right_circle[2][1][1])**2) - right_circle[2][0]), d, (start_C[1]-y)+circle.arc_length(right_circle[2],turning_pts_right[2],right[2]), stop, pid[1]
    elif path == "right_D":
        if abs(y-border[2][1]) <= stop_d:
            stop = True
        if x > turning_pts_right[3][0]:
            return y - turning_pts_right[3][1], d, start_D[0]-x, stop, pid[0]
        else:
            if y > right[3][1]:
                return x - right[3][0], d, (start_D[0]-x)+circle.arc_length(right_circle[3],turning_pts_right[3],right[3])+(y-right[3][1]), stop, pid[0]
            else:
                return -(math.sqrt((x-right_circle[3][1][0])**2 + (y-right_circle[3][1][1])**2) - right_circle[3][0]), d, (start_D[0]-x)+circle.arc_length(right_circle[3],turning_pts_right[3],right[3]), stop, pid[1]

    elif path == "left_A":
        if abs(x-border[1][0]) <= stop_d:
            stop = True
        if y < turning_pts_left[0][1]:
            return x - turning_pts_left[0][0], d, y-start_A[1], stop, pid[0]
        else:
            if x < left[0][0]:
                return y - left[0][1], d, (y-start_A[1])+circle.arc_length(left_circle[0],turning_pts_left[0],(x,y))+(left[0][0]-x), stop, pid[0]
            else:
                return math.sqrt((x-left_circle[0][1][0])**2 + (y-left_circle[0][1][1])**2) - left_circle[0][0], d, (y-start_A[1])+circle.arc_length(left_circle[0],turning_pts_left[0],(x,y)), stop, pid[2]
    elif path == "left_B":
        if abs(y-border[2][1]) <= stop_d:
            stop = True
        if x < turning_pts_left[1][0]:
            return -(y - turning_pts_left[1][1]), d, x-start_B[0], stop, pid[0]
        else:
            if y > left[1][1]:
                return x - left[1][0], d, (x-start_B[0])+circle.arc_length(left_circle[1],turning_pts_left[1],(x,y))+(y-left[1][1]), stop, pid[0]
            else:
                return math.sqrt((x-left_circle[1][1][0])**2 + (y-left_circle[1][1][1])**2) - left_circle[1][0], d, (x-start_B[0])+circle.arc_length(left_circle[1],turning_pts_left[1],(x,y)), stop, pid[2]
    elif path == "left_C":
        if abs(x-border[3][0]) <= stop_d:
            stop = True
        if y > turning_pts_left[2][1]:
            return -(x - turning_pts_left[2][0]), d, start_C[1]-y, stop, pid[0]
        else:
            if x > left[2][0]:
                return -(y - left[2][1]), d, (start_C[1]-y)+circle.arc_length(left_circle[2],turning_pts_left[2],(x,y))+(x-left[2][0]), stop, pid[0]
            else:
                return math.sqrt((x-left_circle[2][1][0])**2 + (y-left_circle[2][1][1])**2) - left_circle[2][0], d, (start_C[1]-y)+circle.arc_length(left_circle[2],turning_pts_left[2],(x,y)), stop, pid[2]
    elif path == "left_D":
        if abs(y-border[0][1]) <= stop_d:
            stop = True
        if x > turning_pts_left[3][0]:
            return y - turning_pts_left[3][1], start_D[0]-x, stop, pid[0]
        else:
            if y < left[3][1]:
                return -(x - left[3][0]), d, (start_D[0]-x)+circle.arc_length(left_circle[3],turning_pts_left[3],(x,y))+(left[3][1]-y), stop, pid[0]
            else:
                return math.sqrt((x-left_circle[3][1][0])**2 + (y-left_circle[3][1][1])**2) - left_circle[3][0], d, (start_D[0]-x)+circle.arc_length(left_circle[3],turning_pts_left[3],(x,y)), stop, pid[2]

def common_merge(main, others):
    all_dst = []
    common = []
    for i in others:
        dst = []
        for j in merging_pts[i[0]]:
            if j in merging_pts[main[0]]:
                if "A" in main[0] or "C" in main[0]:
                    d_A = abs(main[1][1] - j[1])
                else:
                    d_A = abs(main[1][0] - j[0])
                if "A" in i[0]:
                    d_O = abs(i[1][1] - j[1])
                else:
                    d_O = abs(i[1][0] - j[0])
                dst.append([d_A, d_O])
                common.append(j[2])
        all_dst.append(dst)
    return all_dst, common

# a, b = common_merge(["straight_A",(0.1,0.2)], [["straight_B", (0.3,0.4)]])
#
# print(a)        



# def start_to_merging(pos, path):
#     index = ord(path[-1])-65
#     if "A" in path:
#         x,y = start_A
#     elif "B" in path:
#         x,y = start_B
#     elif "C" in path:
#         x,y = start_C
#     else:
#         x,y = start_D
#     distances = []
#     if "right" in path:
#         if "A" in path or "C" in path:
#             distances.append(abs(y-turning_pts_right[index]) + circle.arc_length(right_circle[index], turning_pts_right[index], merging_pts[path][0]))
#         else:
#             distances.append(abs(x-turning_pts_right[index]) + circle.arc_length(right_circle[index], turning_pts_right[index], merging_pts[path][0]))
#     elif "left" in path:
#         if "A" in path or "C" in path:
#             distances.append(abs(y-merging_pts[path][0][1]))
#             distances.append(abs(y-merging_pts[path][0][1]) + circle.arc_length(left_circle[index], merging_pts[path][0], merging_pts[path][1]))
#             distances.append(abs(y-merging_pts[path][0][1]) + circle.arc_length(left_circle[index], merging_pts[path][0], merging_pts[path][2]))
#             distances.append(abs(y-merging_pts[path][0][1]) + circle.arc_length(left_circle[index], merging_pts[path][0], merging_pts[path][2]) + abs(x-merging_pts[path][3][0]))
#         else:
#             distances.append(abs(x-merging_pts[path][0][1]))
#             distances.append(abs(x-merging_pts[path][0][1]) + circle.arc_length(left_circle[index], merging_pts[path][0], merging_pts[path][1]))
#             distances.append(abs(x-merging_pts[path][0][1]) + circle.arc_length(left_circle[index], merging_pts[path][0], merging_pts[path][2]))
#             distances.append(abs(x-merging_pts[path][0][1]) + circle.arc_length(left_circle[index], merging_pts[path][0], merging_pts[path][2]) + abs(y-merging_pts[path][3][0]))
#     else:
#         if "A" in path or "C" in path:
#             distances.append(abs(y-merging_pts[path][0][1]))
#             distances.append(abs(y-merging_pts[path][1][1]))
#             distances.append(abs(y-merging_pts[path][2][1]))
#         else:
#             distances.append(abs(x-merging_pts[path][0][0]))
#             distances.append(abs(x-merging_pts[path][1][0]))
#             distances.append(abs(x-merging_pts[path][2][0]))
