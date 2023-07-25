import numpy as np
# sqrt = np.sqrt
sqrt = lambda x: x**(0.5)


def dist_2_line(A, B, E):
    AB = [None, None];
    AB[0] = B[0] - A[0];
    AB[1] = B[1] - A[1];

    # vector BP
    BE = [None, None];
    BE[0] = E[0] - B[0];
    BE[1] = E[1] - B[1];

    # vector AP
    AE = [None, None];
    AE[0] = E[0] - A[0];
    AE[1] = E[1] - A[1];

    # Variables to store dot product

    # Calculating the dot product
    AB_BE = AB[0] * BE[0] + AB[1] * BE[1];
    AB_AE = AB[0] * AE[0] + AB[1] * AE[1];

    # Minimum distance from
    # point E to the line segment
    reqAns = 0;
    # Case 1
    if (AB_BE > 0) :
        # Finding the magnitude
        y = E[1] - B[1];
        x = E[0] - B[0];
        reqAns = sqrt(x * x + y * y);
    # Case 2
    elif (AB_AE < 0) :
        y = E[1] - A[1];
        x = E[0] - A[0];
        reqAns = sqrt(x * x + y * y);

    # Case 3
    else:

        # Finding the perpendicular distance
        x1 = AB[0];
        y1 = AB[1];
        x2 = AE[0];
        y2 = AE[1];
        mod = sqrt(x1 * x1 + y1 * y1);
        reqAns = abs(x1 * y2 - y1 * x2) / mod;

    return reqAns;


def clockwise(start_point,mid_point,end_point):
    """
    checks if the three points go in a clockwise direction
    i.e. if end_point is on the left or right
    of the line made by start_point and mid_point
    """
    result_a = mid_point[1]-start_point[1]
    result_a *= end_point[0]-mid_point[0]
    result_b = mid_point[0] - start_point[0]
    result_b *= end_point[1] - mid_point[1]
    result = result_a - result_b
    if result > 0:
        return True
    if result < 0:
        return False
    return None

dist = lambda p1, p2: ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(0.5)


def circleRadius(b, c, d):
    temp = c[0]**2 + c[1]**2
    bc = (b[0]**2 + b[1]**2 - temp) / 2
    cd = (temp - d[0]**2 - d[1]**2) / 2
    det = (b[0] - c[0]) * (c[1] - d[1]) - (c[0] - d[0]) * (b[1] - c[1])

    if abs(det) < 1.0e-10:
        return None

    # Center of circle
    cx = (bc*(c[1] - d[1]) - cd*(b[1] - c[1])) / det
    cy = ((b[0] - c[0]) * cd - (c[0] - d[0]) * bc) / det

    radius = ((cx - b[0])**2 + (cy - b[1])**2)**.5

    return radius, (cx, cy)

def arc_length(circle, a, b):
    r = circle[0]
    d = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    theta = math.acos(1-(d**2)/(2*(r**2)))
    return r*theta
