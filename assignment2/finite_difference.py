import numpy as np

def finite_difference():
    step_size = 0.1
    no_of_intervals = int((1-0)/step_size)
    
    x_values = np.array(np.linspace(0, 1, no_of_intervals+1))
    
    A = np.zeros((no_of_intervals-1, no_of_intervals-1))
    b = np.full(no_of_intervals - 1, -10 * step_size**2)
    
    for i in range(no_of_intervals - 1):
        A[i][i] = -2
        if i > 0:
            A[i][i - 1] = 1 + 32 * step_size
        if i < no_of_intervals - 2:
            A[i][i + 1] = 1 - 32 * step_size
    
    y_inner = np.linalg.solve(A, b)
    y = np.zeros(no_of_intervals + 1)
    y[1:no_of_intervals] = y_inner
    
    for xi, yi in zip(x_values, y):
        print(f"x = {xi:.1f}, y = {yi:.4f}")

if __name__ == "__main__":
    finite_difference()