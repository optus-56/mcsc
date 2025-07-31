import numpy as np

def lagrange_interpolation():
    x = np.array([0, 1, 3, 4 ,5])
    y = np.array([0, 1, 81, 256, 625])

    x_target = 2
    result = 0

    for i in range(len(x)):
        L = 1
        for j in range(len(x)):
            if i != j:
                L *= (x_target - x[j]) / (x[i] - x[j])
        result += y[i] * L

    print(f"y(2) = {result}")
    return result

if __name__ == "__main__":
    lagrange_interpolation()