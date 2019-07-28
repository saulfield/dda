# %%
import math
import numpy as np
import matplotlib.pyplot as plt

# %%

# y'(t) = f(y(t))
# y'(t) = y(t)

def solve(f, y0):
    dt = 0.002
    num_steps = 600

    t  = np.zeros(num_steps + 1)
    y  = np.zeros(num_steps + 1)
    dy = np.zeros(num_steps + 1)
    e  = np.zeros(num_steps + 1)

    y [0] = y0
    dy[0] = f(y0)
    e [0] = 1

    for step in range(num_steps):
        t [step + 1] = t[step] + dt
        y [step + 1] = y[step] + dt*dy[step]
        dy[step + 1] = f(y[step])
        e [step + 1] = math.e**t[step+1]

    return t, y, dy, e

t, y, dy, e = solve(lambda y: y, 1.0)

print("approximating e ~= 2.71828")
print(y[500])

plt.plot(t, y)
plt.plot(t, e)
plt.show()