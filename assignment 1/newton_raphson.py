import math

def f(x):
    return math.exp(x) - 4 * x

def df(x):
    return math.exp(x) - 4

def newton_raphson(x0, tol=1e-3, max_iter=100):
    print(f"{'Iter':<5} {'x_n':<12} {'f(x_n)':<12} {'f\'(x_n)':<12}")
    for i in range(1, max_iter+1):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Zero derivative. No solution found.")
            return None

        x1 = x0 - fx / dfx
        print(f"{i:<5} {x0:<12.4f} {fx:<12.4e} {dfx:<12.4f}")

        if abs(x1 - x0) < tol:
            return x1

        x0 = x1

    print("Max iterations reached")
    return x0

root = newton_raphson(1.0)
print(f"\nApproximate root: {root}")
