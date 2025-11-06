#Imports
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#Define constants
T0 = 70 # Initial temperature inside (ºF)
Ta = 30 # Initial temperature outside (ºF)
k = 0.35# cooling constant (hours^(-1))

# Teste 1: k = 0.5
# Teste 2: k = 0.25
# Teste 3: k = 0.45
# Teste 4: k = 0.35 

t_arr = np.linspace(0,5,1000) # array with sampling times

# Newton's Law of Cooling)
# T' = -k(T - Ta)
# dy/dy = func(...)
# y = [T]
def func(t,y,k,Ta):
    T = y
    return -k*(T - Ta)

#Solve the ODE using scipy.integrate.solve_ivp (initial value problem)
sol = solve_ivp(func, (0,5),[T0], args=(k,Ta), t_eval = t_arr)

#Plot Solution
fig, ax = plt.subplots()
ax.plot(sol.t, sol.y[0])
ax.set(xlabel='Elapsed Time (h)', ylabel='Temperature (F)',
       title='Temperature Decay')
ax.grid()

#Search time with T ~= 40 ºF
diff = (sol.y[0]-40)**2
sample_40f = np.where( diff == np.amin(diff))[0][0]
t_40f = sol.t[sample_40f]
ax.scatter(t_40f, sol.y[0][sample_40f], c = 'red', label = 
           f'T({t_40f:.2f} h) = {sol.y[0][sample_40f]:.2f} F')
ax.legend()
plt.show()
print(f'\nThe temperature got closer to 40ºF at time t = {t_40f:.2f} h\n')
