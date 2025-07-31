import numpy as np
import pandas as pd

h = 0.1
x_values = np.arange(-1.0, 1.0 + h, h)
y_values = np.exp(x_values)

n = len(x_values)
diff_table = np.zeros((n, n))
diff_table[:, 0] = y_values

for j in range(1, n):
    for i in range(n - j):
        diff_table[i][j] = diff_table[i+1][j-1] - diff_table[i][j-1]

df = pd.DataFrame(diff_table[:, :6], columns=["Δ⁰y", "Δ¹y", "Δ²y", "Δ³y", "Δ⁴y", "Δ⁵y"])
df.insert(0, "x", x_values)
df.insert(1, "f(x)", y_values)
print(df.round(6))
