import numpy as np

def runge_kutta_2nd():
    def f(x, y):
        return x**2 + x
    
    x0, y0 = 0, 1
    h = 0.2
    x_end = 2
    
    x_vals = [x0]
    y_vals = [y0]
    
    x, y = x0, y0
    while x < x_end - h/2:
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y = y + (k1 + k2) / 2
        x = x + h
        x_vals.append(x)
        y_vals.append(y)
    
    print("n\t\tx\t\ty")
    for i in range(len(x_vals)):
        print(f"{i}\t\t{x_vals[i]:.1f}\t\t{y_vals[i]:.4f}")
    
    return x_vals, y_vals

if __name__ == "__main__":
    runge_kutta_2nd()