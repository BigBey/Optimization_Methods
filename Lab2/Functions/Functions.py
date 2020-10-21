import math


def f1(x):
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def f1_deriv(x, index):
    return {
        1: 2 * (200 * x[0] ** 3 - 200 * x[0] * x[1] + x[0] - 1),
        2: 200 * (x[1] - x[0] ** 2)
    }.get(index)


def f1_grad(x):
    return [f1_deriv(x, i) for i in range(len(x))]


def f2(x):
    return (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def f2_deriv(x, index):
    return {
        1: 2 * (2 * x[0] ** 3 - 2 * x[0] * x[1] + x[0] - 1),
        2: 2 * (x[1] - x[0] ** 2)
    }.get(index)

def f2_grad(x):
    return [f2_deriv(x, i) for i in range(len(x))]

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

def f3_grad(x):
    return [f3_deriv(x, i) for i in range(len(x))]

def f4(x):
    return (x[0] + x[1]) ** 2 + 5 * (x[2] - x[3]) ** 2 + (x[1] - 2 * x[2]) ** 4 + 10 * (x[0] - x[3]) ** 4


def f4_deriv(x, index):
    return {
        1: 2 * (20 * (x[0] - x[3]) ** 3 + x[0] + x[1]),
        2: 2 * (x[0] + 2 * (x[1] - 2 * x[2]) ** 3 + x[1]),
        3: 10 * (x[2] - x[3]) - 8 * (x[1] - 2 * x[2]) ** 3,
        4: 10 * (-4 * (x[0] - x[3]) ** 3 + x[3] - x[2])
    }.get(index)

def f4_grad(x):
    return [f4_deriv(x, i) for i in range(len(x))]

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

def getFuncGrad(index):
    return {1: f1_grad,
            2: f2_grad,
            3: f3_grad,
            4: f4_grad
            }.get(index)
