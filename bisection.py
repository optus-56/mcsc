import math

def f(x):
    return x**2 - math.sin(x)

def bisection(a, b, tol=1e-3, max_iter=100):
    if f(a) * f(b) >= 0:
        print("There is no root in this domain")
        return None

    print(f"{'Iter':<5} {'a':<10} {'b':<10} {'x0':<10} {'f(x0)':<12}")
    for i in range(1, max_iter+1):
        x0 = (a + b) / 2
        fx0 = f(x0)
        print(f"{i:<5} {a:<10.4f} {b:<10.4f} {x0:<10.4f} {fx0:<12.4e}")

        if abs(fx0) < tol or abs(b - a) < tol:
            return x0

        if f(a) * fx0 < 0:
            b = x0
        else:
            a = x0

    print("Max iterations reached")
    return (a + b) / 2

root = bisection(0.5, 1.0)
print(f"\nApproximate root: {root}")
