import math

from Lab1 import Functions as f
import pandas as pd

def parabolaMethod(f, epsilon, a, b):
    x1 = a
    x3 = b
    x2 = x1 + (x3 - x1) * 0.5
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    # find good x2
    step = 0.01
    if f1 < f2 < f3:
        while f1 < f2:
            x2 -= step
            f2 = f(x2)
    if f1 > f2 > f3:
        while f2 > f3:
            x2 += step
            f2 = f(x2)
    u = x2 - (((x2 - x1) ** 2) * (f2 - f3) - ((x2 - x3) ** 2) * (f2 - f1)) / 2 / (
            (x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))
    while True:
        fu = f(u)
        if u <= x2 and fu > f2:
            x1 = u
            f1 = fu
        elif u > x2 and fu > f2:
            x3 = u
            f3 = fu
        elif u > x2 and fu <= f2:
            x1 = x2
            f1 = f2
            x2 = u
            f2 = fu
        elif u <= x2 and fu <= f2:
            x3 = x2
            f3 = f2
            x2 = u
            f2 = fu
        u_prev = u
        u = x2 - (((x2 - x1) ** 2) * (f2 - f3) - ((x2 - x3) ** 2) * (f2 - f1)) / 2 / (
                (x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))
        if abs(u - u_prev) < epsilon:
            return u

def parabolaMethodGetTable(f, epsilon, a, b):
    data = {'a': [], 'b': [], 'Отношение длин': [], 'x1': [], 'x2': [], 'f(x1)': [], 'f(x2)': []}
    x1 = a
    x3 = b
    x2 = x1 + (x3 - x1) * 0.5
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    # find good x2
    step = 0.01
    if f1 < f2 < f3:
        while f1 < f2:
            x2 -= step
            f2 = f(x2)
    if f1 > f2 > f3:
        while f2 > f3:
            x2 += step
            f2 = f(x2)
    u = x2 - (((x2 - x1) ** 2) * (f2 - f3) - ((x2 - x3) ** 2) * (f2 - f1)) / 2 / (
            (x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))
    prev_length = None
    count = 0
    Utils.writeRow(data, x1, x3, prev_length, u, x2, f(u), f2)
    while True:
        count += 1
        prev_length = abs(b - a)
        fu = f(u)
        if u <= x2 and fu > f2:
            x1 = u
            f1 = fu
        elif u > x2 and fu > f2:
            x3 = u
            f3 = fu
        elif u > x2 and fu <= f2:
            x1 = x2
            f1 = f2
            x2 = u
            f2 = fu
        elif u <= x2 and fu <= f2:
            x3 = x2
            f3 = f2
            x2 = u
            f2 = fu
        u_prev = u
        u = x2 - (((x2 - x1) ** 2) * (f2 - f3) - ((x2 - x3) ** 2) * (f2 - f1)) / 2 / (
                (x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))
        Utils.writeRow(data, x1, x3, prev_length, u, x2, f(u), f2)
        if abs(u - u_prev) < epsilon:
            break
    return (count, pd.DataFrame(data))

print(parabolaMethod(f.f1, 0.000001, -0.5, 0.5))
print(parabolaMethod(f.f2, 0.000001, 6.0, 9.9))
print(parabolaMethod(f.f3, 0.000001, 0.0, 2*math.pi))
print(parabolaMethod(f.f4, 0.000001, 0.0, 1.0))
print(parabolaMethod(f.f5, 0.000001, 0.5, 2.5))
