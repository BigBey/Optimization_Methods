import math

from Lab1 import Utils as u, Functions as f
import pandas as pd

def goldenRatioMethod(f, epsilon, a, b):
    F = (1 + math.sqrt(5)) / 2
    x1 = b - (b - a) / F
    x2 = a + (b - a) / F
    f1 = f(x1)
    f2 = f(x2)
    while True:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - (b - a) / F
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (b - a) / F
            f2 = f(x2)
        if abs(b - a) < epsilon:
            break

    return 0.5 * (a + b)

def goldenRatioMethodGetTable(f, epsilon, a, b):
    data = {'a': [], 'b': [], 'Отношение длин': [], 'x1': [], 'x2': [], 'f(x1)': [], 'f(x2)': []}
    F = (1 + math.sqrt(5)) / 2
    x1 = b - (b - a) / F
    x2 = a + (b - a) / F
    f1 = f(x1)
    f2 = f(x2)
    prev_length = None
    count = 0
    u.writeRow(data, a, b, prev_length, x1, x2, f1, f2)
    while True:
        count += 1
        prev_length = abs(b-a)
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - (b - a) / F
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + (b - a) / F
            f2 = f(x2)
        u.writeRow(data, a, b, prev_length, x1, x2, f1, f2)
        if abs(b - a) < epsilon:
            break

    return (count, pd.DataFrame(data))

print(goldenRatioMethod(f.f1, 0.000001, -0.5, 0.5))
print(goldenRatioMethod(f.f2, 0.000001, 6.0, 9.9))
print(goldenRatioMethod(f.f3, 0.000001, 0.0, 2*math.pi))
print(goldenRatioMethod(f.f4, 0.000001, 0.0, 1.0))
print(goldenRatioMethod(f.f5, 0.000001, 0.5, 2.5))
