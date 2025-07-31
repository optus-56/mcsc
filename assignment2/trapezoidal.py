import numpy as np

def y_function(x):
    return np.sin(x)/np.exp(x)

def main():
    
    no_of_steps = 20
    x_values = np.linspace(0, np.pi, no_of_steps+1)
    y_values = np.round(y_function(x_values), 4)
    
    integral = 0
    for i in range(len(x_values)):
        if(i==0 or i == len(x_values)):
            integral += y_values[i]
        else:
            integral += 2*y_values[i]

    integral *= (np.pi-0)/no_of_steps
    integral /= 2
    
        
    print(f"Approximated Integral: {integral:.4f}\n")

if __name__ == "__main__":
    main()