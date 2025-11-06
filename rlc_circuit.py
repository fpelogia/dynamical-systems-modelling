import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# define constants
L = 1.00 # Inductance (Henry)
R = 100 # Resistance (Ohm)
C = 0.0001 # Capacitance (Farad)
#V = lambda t: 1000 # test 1 : constant Voltage (Volt)
V = lambda t: 5*np.cos(t) # test 2 : sinusoidal

t_arr = np.linspace(0,10,2000)# array with sampling times

# Define the ODE
# dy/dt = func(...)
# y = [i(t), q(t)]
def func(t, y, L, R, C, V):
    return [(V(t) - y[1]/C - R*y[0])/L, y[0]]

#Solve the ODE using scipy.integrate.solve_ivp (initial value problem)             
sol = solve_ivp(func, [0,10], [0.0, 0.0], args=(L,R,C,V), t_eval = t_arr)

fig, axs = plt.subplots(1, 2, figsize=(12,4))
fig.suptitle('Electric Current and Charge on the RLC System')
axs[0].plot(sol.t, sol.y[0])
axs[0].set(xlabel='Elapsed Time(s)', ylabel='Electric Current (A)')
axs[0].grid()
axs[1].plot(sol.t, sol.y[1])
axs[1].set(xlabel='Elapsed Time(s)', ylabel='Electric Charge (C)')
axs[1].grid()
plt.show()
