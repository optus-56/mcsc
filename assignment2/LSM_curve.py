import numpy as np

def lsm_curve():
    x = np.array([2, 4, 6, 8, 10])
    y = np.array([4.077, 11.084, 30.128, 81.897, 222.62])
    
    ln_y = np.log(y)
    
    n = len(x)
    sum_x = np.sum(x)
    sum_ln_y = np.sum(ln_y)
    sum_x_ln_y = np.sum(x * ln_y)
    sum_x2 = np.sum(x**2)
    
    b = (n * sum_x_ln_y - sum_x * sum_ln_y) / (n * sum_x2 - sum_x**2)
    ln_a = (sum_ln_y - b * sum_x) / n
    a = np.exp(ln_a)
    
    y_at_9 = a * np.exp(b * 9)
    
    print(f"Exponential fit: y = {a:.4f}e^({b:.4f}x)")
    print(f"y(9): {y_at_9:.4f}")

if __name__ == "__main__":
    lsm_curve()