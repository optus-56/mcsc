import numpy as np
 
def least_square():
    x = np.array([1, 2, 3, 4, 5, 6])
    y = np.array([2.4, 3.1, 3.5, 4.2, 5.0, 6.0])
    
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x**2)
    
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    b = (sum_y - a * sum_x) / n
    
    y_at_2_5 = a * 2.5 + b
    
    print(f"Linear fit: y = {a:.4f}x + {b:.4f}")
    print(f"y(2.5): {y_at_2_5:.4f}")

if __name__ == "__main__":
    least_square()