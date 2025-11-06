import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def plastic_ball_2_order(m_in,c_in,v0_in):
        
    # Define constants
    m = m_in # mass (kg)
    g = 9.8 # gravitational acceleration (m / s^2)
    c = c_in # damping constant (kg/s)
    v0 = v0_in # velocity (m/s)
    t_arr = np.linspace(0,3,1000) # array with sampling times (s)

    #dy/dt = func(...)
    # y = [v,pos]
    def func(t, y, m, g, c):
        v = y[0]
        return [(-c*v - m*g)/m, v]

    # Solve the ODE using scipy.integrate.solve_ivp (initial value problem)
    sol = solve_ivp(func, [0,3],[v0,0.0],args=(m, g, c), t_eval=t_arr)

    # Find maximum height
    max_h_sample = np.where(sol.y[0] == min(sol.y[0], key=abs))

    # Plotting
    fig, axs = plt.subplots(1,2, figsize = (10,4))    
    fig.suptitle(f'Plastic Ball Motion: m = {m}, g = {g}, c = {c}, v0 = {v0}')
    axs[0].plot(sol.t, sol.y[0], zorder=1)
    axs[0].scatter(sol.t[max_h_sample], 0,c ='red' , label = f'V( {sol.t[max_h_sample][0]:.3f} s) ≈ 0',zorder=2)
    axs[0].set(xlabel='Elapsed Time(s)', ylabel='Velocity (m/s)')
    axs[0].legend()
    axs[0].grid()

    axs[1].plot(sol.t, sol.y[1], zorder=1)
    axs[1].scatter(sol.t[max_h_sample], sol.y[1][max_h_sample],c ='red' , label = f'Pos( {sol.t[max_h_sample][0]:.3f} s) ≈ {sol.y[1][max_h_sample][0]:.3f} m',zorder=2)
    axs[1].set(xlabel='Elapsed Time(s)', ylabel='Y Position (m)')
    axs[1].legend()
    axs[1].grid()
    plt.show()

#=================================================================
#Define inputs
m = 0.1
g = 9.8 
c = 0.5  #damping
v0 = 20

plastic_ball_2_order(m,c,v0)
