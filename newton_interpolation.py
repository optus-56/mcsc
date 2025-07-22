from math import factorial

x_vals = [0.20, 0.22, 0.24, 0.26, 0.28, 0.30]
y_vals = [1.6596, 1.6698, 1.6804, 1.6912, 1.7024, 1.7139]
h = 0.02

def forward_newton(x, x_vals, y_vals):
    n = len(x_vals)
    diff = [y_vals.copy()]
    for i in range(1, n):
        temp = [diff[i-1][j+1] - diff[i-1][j] for j in range(n - i)]
        diff.append(temp)

    u = (x - x_vals[0]) / h
    result = y_vals[0]
    for i in range(1, n):
        term = diff[i][0]
        for j in range(i):
            term *= (u - j)
        result += term / factorial(i)
    return round(result, 4)

def backward_newton(x, x_vals, y_vals):
    n = len(x_vals)
    diff = [y_vals.copy()]
    for i in range(1, n):
        temp = [diff[i-1][j+1] - diff[i-1][j] for j in range(n - i)]
        diff.append(temp)

    u = (x - x_vals[-1]) / h
    result = y_vals[-1]
    for i in range(1, n):
        term = diff[i][-1]
        for j in range(i):
            term *= (u + j)
        result += term / factorial(i)
    return round(result, 4)

f0_21 = forward_newton(0.21, x_vals, y_vals)
f0_29 = backward_newton(0.29, x_vals, y_vals)

print(f"Estimated f(0.21) using Newton's forward interpolation: {f0_21}")
print(f"Estimated f(0.29) using Newton's backward interpolation: {f0_29}")
