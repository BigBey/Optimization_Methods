import math
from Lab1 import Functions as f


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def calculateX_hat(x1, x2, x3, f1, f2, f3):
    return x2 - (((x2 - x1)**2 * (f2 - f3) - (x2 - x3)**2 * (f2 - f1)) / (2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))))

def brandtMethod(f, epsilon, a, c):
    K = (3 - math.sqrt(5)) / 2
    x = (a + c)/2
    w = (a + c)/2
    v = (a + c)/2
    fx = f(x)
    fw = f(w)
    fv = f(v)
    d = e = c - a
    u = None
    count = 0
    while True:
        count += 1
        prev_u = u
        g = e
        e = d
        if x != w and x != v and w != v and fx != fw and fx != fv and fw != fv:
            #u = w - (((w - x) ** 2) * (fw - fv) - ((w - v) ** 2) * (fw - fx)) / 2 / (
            #    (w - x) * (w - v) - (w - v) * (w - x))
            u = calculateX_hat(x, w, v, fx, fw, fv)
            if a + epsilon <= u and u <= c - epsilon and abs(u - x) < g / 2:
                d = abs(u - x)
            else:
                u = None
        if u is None:
            if x < (c + a) / 2:
                u = x + K*(c - x)
                d = c - x
            else:
                u = x - K*(x - a)
                d = x - a
        if abs(u - x) < epsilon:
            u = x + sign(u - x)* epsilon
        fu = f(u)
        if fu <= fx:
            if u >= x:
                a = x
            else:
                c = x
            v = w
            w = x
            x = u
            fv = fw
            fw = fx
            fx = fu
        else:
            if u >= x:
                c = u
            else:
                a = u
            if fu <= fw or w == x:
                v = w
                w = u
                fv = fw
                fw = fu
            elif fu <=fv or v == x or v == w:
                v = u
                fv = fu
        if count != 1:
            if abs(prev_u - u) < epsilon:
                break
    return (a + c)/2

print(brandtMethod(f.f1, 0.00001, -0.5, 0.5))