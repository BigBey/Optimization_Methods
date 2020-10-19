import math

import pandas as pd
from Lab1 import Utils as u, Functions as f


def dihotomiaMethod(f, epsilon, a, b):
    delta = epsilon / 4
    x1 = (a + b) / 2 - delta
    x2 = (a + b) / 2 + delta
    f1 = f(x1)
    f2 = f(x2)
    while True:
        if f1 < f2:
            b = x2
        else:
            a = x1
        x1 = (a + b) / 2 - delta
        x2 = (a + b) / 2 + delta
        f1 = f(x1)
        f2 = f(x2)
        if abs(b - a) < epsilon:
            break
    return (a+b)/2


def dihotomiaMethodGetTable(f, epsilon, a, b):
    data = {'a': [], 'b': [], 'Отношение длин': [], 'x1': [], 'x2': [], 'f(x1)': [], 'f(x2)': []}
    delta = epsilon / 4
    x1 = (a + b) / 2 - delta
    x2 = (a + b) / 2 + delta
    f1 = f(x1)
    f2 = f(x2)
    prev_length = None
    u.writeRow(data, a, b, prev_length, x1, x2, f1, f2)
    count = 0
    while True:
        count += 1
        prev_length = abs(b - a)
        if f1 < f2:
            b = x2
        else:
            a = x1
        x1 = (a + b) / 2 - delta
        x2 = (a + b) / 2 + delta
        f1 = f(x1)
        f2 = f(x2)
        u.writeRow(data, a, b, prev_length, x1, x2, f1, f2)
        if abs(b - a) < epsilon:
            break
    return (count, pd.DataFrame(data))


print(dihotomiaMethod(f.f1, 0.000001, -0.5, 0.5))
print(dihotomiaMethod(f.f2, 0.000001, 6.0, 9.9))
print(dihotomiaMethod(f.f3, 0.000001, 0.0, 2 * math.pi))
print(dihotomiaMethod(f.f4, 0.000001, 0.0, 1.0))
print(dihotomiaMethod(f.f5, 0.000001, 0.5, 2.5))
