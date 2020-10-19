import math

from Lab1 import Utils as u, Functions as f
import pandas as pd

def fibonacci(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a

def fibonacciMethod(f, n, a, b):
    x1 = a + (b - a) * fibonacci(n - 2) / fibonacci(n)
    x2 = a + (b - a) * fibonacci(n - 1) / fibonacci(n)
    f1 = f(x1)
    f2 = f(x2)
    while True:
        n -= 1
        if f1 > f2:
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
            f1 = f2
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
            f2 = f1
            f1 = f(x1)
        if n == 1:
            return (x1 + x2) / 2

def fibonacciMethodGetTable(f, n, a, b):
    data = {'a': [], 'b': [], 'Отношение длин': [], 'x1': [], 'x2': [], 'f(x1)': [], 'f(x2)': []}
    x1 = a + (b - a) * fibonacci(n - 2) / fibonacci(n)
    x2 = a + (b - a) * fibonacci(n - 1) / fibonacci(n)
    f1 = f(x1)
    f2 = f(x2)
    prev_length = None
    count = 0
    u.writeRow(data, a, b, prev_length, x1, x2, f1, f2)
    while True:
        count += 1
        prev_length = abs(b - a)
        n -= 1
        if f1 > f2:
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
            f1 = f2
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
            f2 = f1
            f1 = f(x1)
        u.writeRow(data, a, b, prev_length, x1, x2, f1, f2)
        if n == 1:
            break
    return (count, pd.DataFrame(data))

print(fibonacciMethod(f.f1, 30, -0.5, 0.5))
print(fibonacciMethod(f.f2, 30, 6.0, 9.9))
print(fibonacciMethod(f.f3, 30, 0.0, 2*math.pi))
print(fibonacciMethod(f.f4, 30, 0.0, 1.0))
print(fibonacciMethod(f.f5, 30, 0.5, 2.5))
