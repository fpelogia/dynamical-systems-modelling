import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def plastic_ball(m_in,c_in,v0_in):
        
    # Define constants
    m = m_in # mass (kg)
    g = 9.8 # gravitational acceleration (m / s^2)
    c = c_in # damping constant (kg/s)
    v0 = v0_in # velocity (m/s)
    t_arr = np.linspace(0,10,1000) # array with sampling times (s)

    #dy/dt = func(...)
    # y = [v]
    def func(t, y, m, g, c):
        v = y
        return (-c*v - m*g)/m

    # Solve the ODE using scipy.integrate.solve_ivp (initial value problem)
    sol = solve_ivp(func, [0,10],[v0],args=(m, g, c), t_eval=t_arr)

    # Find maximum height
    max_h_sample = np.where(sol.y[0] == min(sol.y[0], key=abs))

    # Plotting
    fig, ax = plt.subplots()    
    ax.plot(sol.t, sol.y[0], zorder=1)
    ax.scatter(sol.t[max_h_sample], 0,c ='red' , label = f'V( {sol.t[max_h_sample][0]:.3f} s) ≈ 0',zorder=2)
    ax.set(xlabel='Elapsed Time(s)', ylabel='Velocity (m/s)',
       title=f'Plastic Ball Motion: m = {m}, g = {g}, c = {c}, v0 = {v0}')
    ax.legend()
    ax.grid()
    plt.show()

#=================================================================
#Define inputs
m = 0.25
g = 9.8 
c = 0.0  #damping
v0 = 50
t_arr = np.linspace(0,10,1000)

plastic_ball(m,c,v0)
