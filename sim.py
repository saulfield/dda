# %%
import numpy as np
from numpy.linalg import norm
import math
import matplotlib.pyplot as plt

# %%
def sin_cos():
    num_points = 100
    rad_per_point = (2 * math.pi) / (num_points - 1.0)

    x = np.zeros(num_points)
    sin_x = np.zeros(num_points)
    cos_x = np.zeros(num_points)

    for i in range(num_points):
        x[i] = i * rad_per_point
        sin_x[i] = math.sin(3*x[i])
        cos_x[i] = math.cos(x[i])
    return x, sin_x, cos_x

# x, sin_x, cos_x = sin_cos()

# plt.plot(x, sin_x)
# plt.plot(x, cos_x)
# plt.show()

# %%
def forward_euler():
    dt = 0.1 # s
    g = 9.81 # m / s2

    num_steps = 50

    t = np.zeros(num_steps + 1)
    x = np.zeros(num_steps + 1)
    v = np.zeros(num_steps + 1)

    for step in range(num_steps):
        t[step + 1] = (step + 1)*dt
        x[step + 1] = x[step] + v[step]*dt
        v[step + 1] = v[step] - g*dt
    return t, x, v

t, x, v = forward_euler()

xplot = plt.subplot(2, 1, 1)
xplot.set_ylabel('Height [m]')
xplot.plot(t, x)

vplot = plt.subplot(2, 1, 2)
vplot.set_ylabel('Velocity [m/s]')
vplot.set_xlabel('Time [s]')
vplot.plot(t, v)

plt.show()

# %%

def acceleration(spaceship_position):
    earth_mass = 5.97e24 # kg
    gravitational_constant = 6.67e-11 # N m2 / kg2
    ds = norm(spaceship_position)
    uv = -spaceship_position/ds
    accel = (gravitational_constant * earth_mass / ds**2) * uv
    return accel

def ship_trajectory():
    dt = 0.01 # s
    num_steps = 1500000
    x = np.zeros([num_steps + 1, 2]) # m
    v = np.zeros([num_steps + 1, 2]) # m / s

    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3

    for step in range(num_steps):
        x[step + 1] = x[step] + v[step]*dt
        v[step + 1] = v[step] + acceleration(x[step])*dt

    return x, v

x, v = ship_trajectory()

plt.plot(x[:, 0], x[:, 1])
plt.scatter(0, 0)
plt.axis('equal')
axes = plt.gca()
axes.set_xlabel('Longitudinal position in m')
axes.set_ylabel('Lateral position in m')

# %%

# approximating e ~= 2.71828...
# y'(t) = f(y(t))
# y'(t) = y(t)

def solve(f, y0):
    # dt = 0.001
    dt = 0.002
    num_steps = 600

    t  = np.zeros(num_steps + 1)
    y  = np.zeros(num_steps + 1)
    dy = np.zeros(num_steps + 1)
    euler = np.zeros(num_steps + 1)

    y[0]  = y0
    dy[0] = f(y0)
    euler[0] = 1

    for step in range(num_steps):
        t [step + 1] = t[step] + dt
        y [step + 1] = y[step] + dt*dy[step]
        dy[step + 1] = f(y[step])
        euler[step + 1] = math.e**t[step+1]

    return t, y, dy, euler

t, y, dy, euler = solve(lambda y: y, 1.0)

print(y[500])

plt.plot(t, y)
plt.plot(t, euler)
plt.show()