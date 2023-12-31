import cvxpy as cp
import numpy as np
from scipy.integrate import odeint
# from OCT1 import OCT1


class Robot:
    def __init__(self, u_min, u_max, phiRearEnd, phiLateral, deltaSafetyDistance, v_min, v_max):
        self.u_min = u_min
        self.u_max = u_max
        self.phiRearEnd = phiRearEnd
        self.phiLateral = phiLateral
        self.deltaSafetyDistance = deltaSafetyDistance
        self.v_min = v_min
        self.v_max = v_max

    def OCBF_SecondOrderDynamics(self, i, matrix, state, dprint = False):
        # ocpar = OCT1(0, 0.1, 1.564)
        ocpar = [-0.775514512237531, 1.35826989127805, 0.100000000000000, 0, 1.75144355114535, 1.28946652089692]

        c = np.array(ocpar)
        x0 = np.array(state)
        eps = 10
        psc = 0.1
        t = 0.1 * i

        # reference Trajectory
        vd = 0.5 * c[0] * t ** 2 + c[1] * t + c[2]
        # print(vd)
        u_ref = c[0] * t + c[1]

        # Physical Limitations on velocity
        b_vmax = self.v_max - x0[1]
        b_vmin = x0[1] - self.v_min

        # CLF
        phi0 = -eps * (x0[1] - vd) ** 2
        phi1 = 2 * (x0[1] - vd)

        def solveQP(n):
            x = cp.Variable(n)

            A = np.array([[1, 0], [-1, 0], [phi1, -1], [1, 0], [-1, 0]])
            b = np.array([self.u_max, -self.u_min, phi0, b_vmax, b_vmin])

            # Rear-end Safety Constraints

            if matrix[0][0] != -1:
                xip = matrix[0][1]
                h = xip - x0[0] - self.phiRearEnd * x0[1] - self.deltaSafetyDistance
                vip = matrix[0][2]
                uminValue = abs(self.u_min)
                hf = h - 0.5 * (vip - x0[1]) ** 2 / uminValue

                if x0[1] <= vip or hf < 0:
                    p = 1
                    LgB = 1
                    LfB = 2 * p * (vip - x0[1]) + p ** 2 * h
                    A = np.vstack((A, [LgB, 0]))
                    b = np.concatenate((b, [LfB]))

                else:
                    LgB = self.phiRearEnd - (vip - x0[1]) / uminValue
                    LfB = vip - x0[1]
                    if LgB != 0:
                        A = np.vstack((A, [LgB, 0]))
                        b = np.concatenate((b, [LfB + hf]))

            # Lateral Safety Constraints

            for row_index, row in enumerate(matrix):
                if -1 in row:
                    continue
                else:
                    d1 = matrix[row_index][3]
                    d2 = state[row_index+2]
                    if dprint:
                        print("state[row_index+2]:")
                        print(state[row_index+2])
                        print("d1:")
                        print(d1)
                        print("d2:")
                        print(d2)
                L = state[row_index+2] + state[0]

                v0 = matrix[row_index][2]

                bigPhi = self.phiLateral * x0[0] / L
                h = d2 - d1 - bigPhi * x0[1]

                uminValue = abs(self.u_min)
                hf = d2 - d1 - 0.5 * (v0 - x0[1]) ** 2 / uminValue - self.phiLateral * v0 * (
                        x0[0] + 0.5 * (x0[1] ** 2 - v0 ** 2) / uminValue) / L

                if x0[1] <= v0 or hf < 0:
                    LgB = bigPhi
                    LfB = v0 - x0[1] - self.phiLateral * x0[1] ** 2 / L
                    if LgB != 0:
                        A = np.vstack((A, [LgB, 0]))
                        b = np.concatenate((b, [LfB + h]))
                else:
                    LgB = self.phiLateral * v0 * x0[1] / uminValue / L - (v0 - x0[1]) / uminValue
                    LfB = v0 - x0[1] - self.phiLateral * v0 * x0[1] / L
                    if LgB != 0:
                        A = np.vstack((A, [LgB, 0]))
                        b = np.concatenate((b, [LfB + hf]))

            constraints = [
                A @ x <= b
            ]

            H = np.array([[1, 0], [0, psc]])
            f = np.array([-u_ref, 0])

            objective = cp.Minimize(0.5 * cp.quad_form(x, H) + f.T @ x)

            problem = cp.Problem(objective, constraints)
            try:
                problem.solve()#verbose=True)
            except cp.error.SolverError:
                if state[1] >=0:
                    u = 0#-state[1]
                else:
                    u = 0
                return None # u
            # optimal_value = problem.value
            optimal_variables = x.value
            try:
                # try:
                u = optimal_variables[0]
                # except TypeError:
                #     u = -0.5*state[1]
            except TypeError:# cvxpy.error.SolverError:
                if state[1] >=0:
                    u = 0#-state[1]
                else:
                    u = 0
                return None # u
            return u

        def second_order_model(x, t, u):
            # global u, noise1, noise2
            dx = np.zeros(2)
            dx[0] = x[1]
            dx[1] = u

            return dx

        # u = (solveQP(2),)
        u_final= solveQP(2)
        return u_final
        # x = np.zeros(2)
        # t_start = 0
        # t_end = 0.1
        # t_span = (t_start, t_end)
        #
        # solution = odeint(second_order_model, x0[0:2], t_span, args=u)
        #
        # rt = [solution[-1][0], solution[-1][1]]
        # # print(rt)
        # return rt#, vd



if __name__ == '__main__':
    my_robot = Robot(-1, 1, 0.18, 0.18, 0.1, 0, 1)
    tst_mat = np.array([
        [-1.00000000e+00, -1.00000000e+00, -1.00000000e+00, -1.00000000e+00],
        # [ 7.89000000e+02,  2.75848042e-01,  0.00000000e+00,  1.46101355e+00]
        []
        # [-1,-1,-1,-1]
    ])
    tst_vec = np.array([ 1.254289,    0.5,         1.123,          1.35015196])

    # my_robot.OCBF_SecondOrderDynamics(1, np.array([[3, 1.082444, 0, -1], [2, 2.25106, 0.5, 0.4373],
    #                                                [4, 1.1569, 0.5, 1.5314]]),
    #                                   [0.503779, 0.5, 0.2898, 1.061228, 1.061228, 1.061228])
    out = my_robot.OCBF_SecondOrderDynamics(1, tst_mat, tst_vec)
    print(out)

# The 5 additional columns in the state list for our car is the distance of our car from each of the merging points!
