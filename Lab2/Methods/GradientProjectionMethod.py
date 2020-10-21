import math
import operator
import numpy as np
import Lab2.Methods.projecting_linear as pl


def f1(x):
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def f1_deriv(x, index):
    return {
        1: 2 * (200 * x[0] ** 3 - 200 * x[0] * x[1] + x[0] - 1),
        2: 200 * (x[1] - x[0] ** 2)
    }.get(index)


def f2(x):
    return (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def f2_deriv(x, index):
    return {
        1: 2 * (2 * x[0] ** 3 - 2 * x[0] * x[1] + x[0] - 1),
        2: 2 * (x[1] - x[0] ** 2)
    }.get(index)


def f3(x):
    return (1.5 - x[0] * (1 - x[1])) ** 2 + (2.25 - x[0] * (1 - x[1] ** 2)) ** 2 + (2.625 - x[0] * (1 - x[1] ** 3)) ** 2


def f3_deriv(x, index):
    return {
        1: 2 * x[0] * (
                x[1] ** 6 + x[1] ** 4 - 2 * x[1] ** 3 - x[1] ** 2 - 2 * x[1] + 3) + 5.25 * x[1] ** 3 + 4.5 * x[
               1] ** 2 + 3 * x[1] - 12.75,
        2: x[0] * (x[0] * (6 * x[1] ** 5 + 4 * x[1] ** 3 - 6 * x[1] ** 2 - 2 * x[1] - 2) + 15.75 * x[1] ** 2 + 9 * x[
            1] + 3)
    }.get(index)


def f4(x):
    return (x[0] + x[1]) ** 2 + 5 * (x[2] - x[3]) ** 2 + (x[1] - 2 * x[2]) ** 4 + 10 * (x[0] - x[3]) ** 4


def f4_deriv(x, index):
    return {
        1: 2 * (20 * (x[0] - x[3]) ** 3 + x[0] + x[1]),
        2: 2 * (x[0] + 2 * (x[1] - 2 * x[2]) ** 3 + x[1]),
        3: 10 * (x[2] - x[3]) - 8 * (x[1] - 2 * x[2]) ** 3,
        4: 10 * (-4 * (x[0] - x[3]) ** 3 + x[3] - x[2])
    }.get(index)


def getFunc(index):
    return {1: f1,
            2: f2,
            3: f3,
            4: f4
            }.get(index)


def getFuncDeriv(index):
    return {1: f1_deriv,
            2: f2_deriv,
            3: f3_deriv,
            4: f4_deriv
            }.get(index)


def getFuncVariableNumber(index):
    return {1: 2,
            2: 2,
            3: 2,
            4: 4}.get(index)


def goldenRatio(a, b, func, eps):
    PHI = (1 + np.sqrt(5)) / 2
    len_prev = 0
    x1 = b - (b - a) / PHI
    x2 = a + (b - a) / PHI
    f1 = func(x1)
    f2 = func(x2)
    counter = 0
    while abs(b - a) > eps:
        counter += 1
        len_prev = b - a
        if f1 < f2:
            b = x2
            f2, x2 = f1, x1
            x1 = b - (b - a) / PHI
            f1 = func(x1)
        else:
            a = x1
            f1, x1 = f2, x2
            x2 = a + (b - a) / PHI
            f2 = func(x2)
    return (a + b) / 2


def steepestDescent(func_index, eps):
    func = getFunc(func_index)
    func_deriv = getFuncDeriv(func_index)
    variable_number = getFuncVariableNumber(func_index)
    x = [0 for i in range(variable_number)]
    points = [(x, func(x))]
    iterations = 0
    while True:
        grad = [func_deriv(x, i) for i in range(1, variable_number + 1)]
        new_x_func = lambda step: list(map(operator.sub, x, [step * grad[i] for i in range(len(grad))]))
        step_func = lambda step: func(new_x_func(step))
        result_step = goldenRatio(0, 10, step_func, 10 ** -6)
        pr = pl.LinearWorker(new_x_func(result_step), getFuncVariableNumber(func_index) + 2, pl.ProjectionSurface.BALL)
        x = pr.project()
        #x = new_x_func(result_step)
        points.append((x, func(x)))
        iterations += 1
        if abs(points[-1][1] - points[-2][1]) < eps:
            break
    print(iterations)
    print(points[-1])


for i in range(1, 5):
    steepestDescent(i, 0.0000001)
