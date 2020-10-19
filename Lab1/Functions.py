import math


def f1(x):
    return -5 * (x ** 5) + 4 * (x ** 4) - 12 * (x ** 3) + 11 * (x ** 2) - 2 * x + 1


def f2(x):
    return (math.log10(x - 2)) ** 2 + (math.log10(10 - x)) ** 2 - x ** (0.2)


def f3(x):
    return -3 * x * math.sin(0.75 * x) + math.exp(- 2 * x)


def f4(x):
    return math.exp(3 * x) + 5 * math.exp(- 2 * x)


def f5(x):
    return 0.2 * x * math.log10(x) + (x - 2.3) ** 2


def getFunc(index):
    return {1: f1,
            2: f2,
            3: f3,
            4: f4,
            5: f5
            }.get(index)
