def euler_method():
    def f(x, y):
        return x**2 + x
    
    x0, y0 = 0, 1
    h = 0.1
    x_end = 2
    
    x_vals = [x0]
    y_vals = [y0]
    
    x, y = x0, y0
    while x < x_end - h/2:
        y = y + h * f(x, y)
        x = x + h
        x_vals.append(x)
        y_vals.append(y)
    
    print("n\t\tx\t\ty")
    for i in range(len(x_vals)):
        print(f"{i}\t\t{x_vals[i]:.1f}\t\t{y_vals[i]:.4f}")
    
    return x_vals, y_vals

if __name__ == "__main__":
    euler_method()