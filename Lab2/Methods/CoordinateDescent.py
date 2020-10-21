from itertools import cycle
import numpy as np
import Lab2.Functions.Functions as f


def coordinateDescent(x, func_number, eps, max_iter, learning_rate):
    coordinates = []  # отрезки для графика
    n_arg = len(x)
    cycler = cycle([i + 1 for i in range(n_arg)])  # чередование координат по кругу
    counter = 0
    while counter < max_iter:
        counter += 1
        index = next(cycler)
        d_x = f.getFuncDeriv(func_number)(x, index)
        new_x = x.copy()
        new_x[index - 1] = x[index - 1] - learning_rate * d_x
        coordinates.append([x, new_x])
        if np.linalg.norm(np.array(new_x) - np.array(x)) < eps:
            x = new_x
            break
        x = new_x
    return x, counter, coordinates


if __name__ == '__main__':
    x, counter, coordinates = coordinateDescent([-1, -1], 1, 0.00001, 5000, 0.002)
    print(x)
    print(counter)
    print(f.getFunc(1)(x))
