def lagrange_interpolation(x, x_vals, y_vals):
    total = 0
    n = len(x_vals)
    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if i != j:
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        total += term
    return total

x_points = [0, 1, 3, 4, 5]
y_points = [0, 1, 81, 256, 625]
y_at_2 = lagrange_interpolation(2, x_points, y_points)

print(f"Estimated y(2) using Lagrange interpolation: {y_at_2}")
