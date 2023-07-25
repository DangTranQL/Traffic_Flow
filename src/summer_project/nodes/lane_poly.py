from spline import poly_calc as poly
from scipy.optimize import minimize
import numpy as np
import geom_util as geom
import math
arr = np.array
s = np.sin
c = np.cos
pi = np.pi
deg = np.rad2deg
rad = np.deg2rad

rot = lambda th: arr([
    [c(th), -s(th)],
    [s(th),  c(th)]
])

R_B = rot(-pi/2)
R_C = rot(-pi)
R_D = rot(pi/2)

lane_width = 1#0.575#345#meter
center_pos = arr([-1.075,3.476])

end_d = 2#4#2

straight_wpts_A = arr([
    [0.5, -end_d],
    [0.5, end_d]
]) * lane_width

straight_wpts_B = (R_B@straight_wpts_A.T).T
straight_wpts_C = (R_C@straight_wpts_A.T).T
straight_wpts_D = (R_D@straight_wpts_A.T).T

straight_wpts_A += center_pos
straight_wpts_B += center_pos
straight_wpts_C += center_pos
straight_wpts_D += center_pos

left_turn_wpts_A = arr([
    [0.5, -end_d],
    [0.5, -1],
    [0.5, -0.5],
    # quarter circle points here
    [-0.5, 0.5],
    [-end_d, 0.5]
]) * lane_width

left_turn_wpts_B = (R_B@left_turn_wpts_A.T).T
left_turn_wpts_C = (R_C@left_turn_wpts_A.T).T
left_turn_wpts_D = (R_D@left_turn_wpts_A.T).T

left_turn_wpts_A += center_pos
left_turn_wpts_B += center_pos
left_turn_wpts_C += center_pos
left_turn_wpts_D += center_pos

right_turn_wpts_A = arr([
    [0.5, -end_d],
    [0.5, -1],
    # quarter circle points here
    [1, -0.5],
    [end_d, -0.5]
]) * lane_width


right_turn_wpts_B = (R_B@right_turn_wpts_A.T).T
right_turn_wpts_C = (R_C@right_turn_wpts_A.T).T
right_turn_wpts_D = (R_D@right_turn_wpts_A.T).T

right_turn_wpts_A += center_pos
right_turn_wpts_B += center_pos
right_turn_wpts_C += center_pos
right_turn_wpts_D += center_pos



LT_COEFFS_A = poly(left_turn_wpts_A)
ST_COEFFS_A = poly(straight_wpts_A)
RT_COEFFS_A = poly(right_turn_wpts_A)
LT_COEFFS_B = poly(left_turn_wpts_B)
ST_COEFFS_B = poly(straight_wpts_B)
RT_COEFFS_B = poly(right_turn_wpts_B)
LT_COEFFS_C = poly(left_turn_wpts_C)
ST_COEFFS_C = poly(straight_wpts_C)
RT_COEFFS_C = poly(right_turn_wpts_C)
LT_COEFFS_D = poly(left_turn_wpts_D)
ST_COEFFS_D = poly(straight_wpts_D)
RT_COEFFS_D = poly(right_turn_wpts_D)

# print(ST_COEFFS)
ST_FUNCS_A = [np.poly1d(coeffs) for coeffs in ST_COEFFS_A]
LT_FUNCS_A = [np.poly1d(coeffs) for coeffs in LT_COEFFS_A]
RT_FUNCS_A = [np.poly1d(coeffs) for coeffs in RT_COEFFS_A]
ST_FUNCS_B = [np.poly1d(coeffs) for coeffs in ST_COEFFS_B]
LT_FUNCS_B = [np.poly1d(coeffs) for coeffs in LT_COEFFS_B]
RT_FUNCS_B = [np.poly1d(coeffs) for coeffs in RT_COEFFS_B]
ST_FUNCS_C = [np.poly1d(coeffs) for coeffs in ST_COEFFS_C]
LT_FUNCS_C = [np.poly1d(coeffs) for coeffs in LT_COEFFS_C]
RT_FUNCS_C = [np.poly1d(coeffs) for coeffs in RT_COEFFS_C]
ST_FUNCS_D = [np.poly1d(coeffs) for coeffs in ST_COEFFS_D]
LT_FUNCS_D = [np.poly1d(coeffs) for coeffs in LT_COEFFS_D]
RT_FUNCS_D = [np.poly1d(coeffs) for coeffs in RT_COEFFS_D]

def reg_wpts(FUNCS, n_pts = 10):
    wpts = []#[] for _ in range(FUNCS)]
    t = np.linspace(0, 1, n_pts)
    for f in FUNCS:
        wpts.append(f(t))
    return arr(wpts).T

ST_WPTS_A = reg_wpts(ST_FUNCS_A, n_pts=4)
LT_WPTS_A = reg_wpts(LT_FUNCS_A)
RT_WPTS_A = reg_wpts(RT_FUNCS_A)
ST_WPTS_B = reg_wpts(ST_FUNCS_B, n_pts=4)
LT_WPTS_B = reg_wpts(LT_FUNCS_B)
RT_WPTS_B = reg_wpts(RT_FUNCS_B)
ST_WPTS_C = reg_wpts(ST_FUNCS_C, n_pts=4)
LT_WPTS_C = reg_wpts(LT_FUNCS_C)
RT_WPTS_C = reg_wpts(RT_FUNCS_C)
ST_WPTS_D = reg_wpts(ST_FUNCS_D, n_pts=4)
LT_WPTS_D = reg_wpts(LT_FUNCS_D)
RT_WPTS_D = reg_wpts(RT_FUNCS_D)

WPTS = {
"S_A" : ST_WPTS_A,
"L_A" : LT_WPTS_A,
"R_A" : RT_WPTS_A,
"S_B" : ST_WPTS_B,
"L_B" : LT_WPTS_B,
"R_B" : RT_WPTS_B,
"S_C" : ST_WPTS_C,
"L_C" : LT_WPTS_C,
"R_C" : RT_WPTS_C,
"S_D" : ST_WPTS_D,
"L_D" : LT_WPTS_D,
"R_D" : RT_WPTS_D
}
COEFFS = {
"S_A" : ST_COEFFS_A,
"L_A" : LT_COEFFS_A,
"R_A" : RT_COEFFS_A,
"S_B" : ST_COEFFS_B,
"L_B" : LT_COEFFS_B,
"R_B" : RT_COEFFS_B,
"S_C" : ST_COEFFS_C,
"L_C" : LT_COEFFS_C,
"R_C" : RT_COEFFS_C,
"S_D" : ST_COEFFS_D,
"L_D" : LT_COEFFS_D,
"R_D" : RT_COEFFS_D
}
POLYS = {
"S_A" : [np.poly1d(ST_COEFF) for ST_COEFF in ST_COEFFS_A],
"L_A" : [np.poly1d(LT_COEFF) for LT_COEFF in LT_COEFFS_A],
"R_A" : [np.poly1d(RT_COEFF) for RT_COEFF in RT_COEFFS_A],
"S_B" : [np.poly1d(ST_COEFF) for ST_COEFF in ST_COEFFS_B],
"L_B" : [np.poly1d(LT_COEFF) for LT_COEFF in LT_COEFFS_B],
"R_B" : [np.poly1d(RT_COEFF) for RT_COEFF in RT_COEFFS_B],
"S_C" : [np.poly1d(ST_COEFF) for ST_COEFF in ST_COEFFS_C],
"L_C" : [np.poly1d(LT_COEFF) for LT_COEFF in LT_COEFFS_C],
"R_C" : [np.poly1d(RT_COEFF) for RT_COEFF in RT_COEFFS_C],
"S_D" : [np.poly1d(ST_COEFF) for ST_COEFF in ST_COEFFS_D],
"L_D" : [np.poly1d(LT_COEFF) for LT_COEFF in LT_COEFFS_D],
"R_D" : [np.poly1d(RT_COEFF) for RT_COEFF in RT_COEFFS_D]
}
# print(ST_WPTS)

def signed_error(WPTS, pos):
    sort_func = lambda item: geom.dist(pos, item[1])
    nearest_2 = list(sorted( list(enumerate(WPTS)), key=sort_func ))[:2]
    ind_sort = lambda item: item[0]
    nearest_2 = [item[1] for item in list(sorted(nearest_2, key=ind_sort))]
    on_right = geom.clockwise(nearest_2[0], nearest_2[1], pos)
    # calculate dist

    dist_2_path = geom.dist_2_line(nearest_2[0], nearest_2[1], pos)
    return dist_2_path * (-1)**(on_right+1)

# print(signed_error(ST_WPTS, [1,0]))

formula = None
bot_pos = [0,0]
def min_pts(x):
    tx = 0
    ty = 0
    bx,by = bot_pos
    for i in range(len(formula[0])):
        if i != len(formula[0])-1:
            tx += formula[0][i] * (x**(len(formula[0])-i))
            ty += formula[1][i] * (x**(len(formula[1])-i))
        else:
            tx += formula[0][i]
            ty += formula[1][i]
    # return math.sqrt((tx-322)**2 + (ty-318)**2)#              ASK!!! MAGIC NUMBER??
    return math.sqrt((tx - bx)**2 + (ty - by)**2)
    #?????

def curve_dist(coeff, p):
    global formula, bot_pos
    bot_pos = p
    x,y = p
    formula = coeff
    # fit = minimize(min_pts, x0=0.5, method='Nelder-Mead', bounds=((0,1),))# 0.09-0.2 avg 0.1
    # fit = minimize(min_pts, x0=0.5, method='SCS', bounds=((0,1),))
    #best so far:
    fit = minimize(min_pts, x0=0.5, method='SLSQP', bounds=((0,1),)) # 0.04-0.1 avg 0.04
    # fit = minimize(min_pts, x0=0.5, method='L-BFGS-B', bounds=((0,1),)) # dt~0.04-0.1 avg 0.7
    t = fit.x[0]
    tx = 0
    ty = 0
    for i in range(len(formula[0])):
        if i != len(formula[0])-1:
            tx += formula[0][i] * (t**(len(formula[0])-i))
            ty += formula[1][i] * (t**(len(formula[1])-i))
        else:
            tx += formula[0][i]
            ty += formula[1][i]
    return math.sqrt((tx-x)**2 + (ty-y)**2), [tx,ty]

def poly_signed_error(coeffs, p):
    dist, ts = curve_dist(coeffs, p)
    amt = 0.05
    nts = [t + amt for t in ts]
    # nts = [ts[0] + amt, ts[1] + amt]
    polys = [np.poly1d(coeffs[i]) for i in [0,1]]
    near_p = [polynomial(ts[i]) for i, polynomial in enumerate(polys)]
    future_p = [polynomial(nts[i]) for i, polynomial in enumerate(polys)]
    on_right = geom.clockwise(p, near_p, future_p)
    return dist * ((-1)**(on_right+1))
