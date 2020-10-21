import numpy as np
import Lab2.Functions.Functions as f


def step(v, func_number, h):
    x = []
    for i in range(len(v)):
        x.append(v[i] - h * f.getFuncDeriv(func_number)(v, i + 1))
    return np.array(x)


def ravineGradient(v_k, v_k_1, func_number, eps, C, h, max_iter):
    coordinates = []
    v_k = np.array(v_k)
    v_k_1 = np.array(v_k_1)
    x_k = step(v_k, func_number, h)
    x_k_1 = step(v_k_1, func_number, h)
    counter = 0
    while counter < max_iter:
        coordinates.append([x_k, x_k_1])
        counter += 1
        v_new = x_k_1 - (x_k_1 - x_k) / (np.linalg.norm(x_k_1 - x_k)) \
                * h * np.sign(np.array(f.getFunc(func_number)(x_k_1) - np.array(f.getFunc(func_number)(x_k))))
        x_new = step(v_new, func_number, h)
        cos_a = (np.dot(v_new - x_k_1, x_new - x_k_1)) / (
                np.linalg.norm(v_new - x_k_1) * (np.linalg.norm(x_new - x_k_1)))
        cos_a_1 = (np.dot(v_k_1 - x_k, x_k_1 - x_k)) / (np.linalg.norm(v_k_1 - x_k) * (np.linalg.norm(x_k_1 - x_k)))
        h = h * C ** (cos_a - cos_a_1)
        v_k = v_k_1
        v_k_1 = v_new
        x_k = x_k_1
        x_k_1 = x_new
        if np.linalg.norm(np.array(x_k_1) - np.array(x_k)) < eps:
            break
    return x_k_1, counter, coordinates


if __name__ == '__main__':
    x, counter, coordinates = ravineGradient([1.1, 1], [1, 1], 3, 0.001, 3, 0.001, 1000)
    print(x)
