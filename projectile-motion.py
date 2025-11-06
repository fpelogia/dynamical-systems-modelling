#Imports
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def projectile_motion(V0, neg_g, pos0, drag, t_arr):
    #V0: initial (x, y) velocity (m/s)
    #neg_g: -1*gravitational acceleration (m/s^2)
    #pos0: initial position (m)
    #drag : air drag
    #t_arr : array with sampling times

    # Define the ODE
    # dy/dt = func(...)
    # y = [vx, vy, posx, posy]
    def func(t, y, neg_g, drag):
        acc_x = neg_g[0] - y[0]*drag*np.sqrt(y[0]**2 + y[1]**2)
        acc_y = neg_g[1] - y[1]*drag*np.sqrt(y[0]**2 + y[1]**2)
        return [acc_x, acc_y, y[0], y[1]]


    #Solve the ODE using scipy.integrate.solve_ivp (initial value problem)
    sol = solve_ivp(func, [0,50],[V0[0], V0[1], pos0[0], pos0[1]],args=(neg_g, drag)
    , t_eval = t_arr)

    v_mag = np.sqrt(sol.y[0]**2 + sol.y[1]**2)

    # Plotting
    fig, axs = plt.subplots(1, 3, figsize=(14,4))
    fig.suptitle(f'Projectile Motion Model: V0 = {V0}, pos0 = {pos0}, drag = {drag}, neg_g = {neg_g}')
    above_floor = sol.y[3] >= 0
    axs[1].plot(sol.t[above_floor], sol.y[3][above_floor])
    axs[1].set(xlabel='Elapsed Time(s)', ylabel='Y Position (m)')
    axs[1].grid()
    axs[0].plot(sol.t[above_floor], v_mag[above_floor])
    axs[0].set(xlabel='Elapsed Time (s)', ylabel='Velocity Magnitude (m/s)')
    axs[0].grid()
    axs[2].plot(sol.y[2][above_floor], sol.y[3][above_floor])
    axs[2].set(xlabel='X Position (m)', ylabel='Y Position (m)')
    axs[2].grid()
    plt.show()

# ========================================================================
# Define inputs
V0 = [80, 0] #(80 ft/s ~ 24.384 m/s)
neg_g = [0, -9.7536] #(32 ft/s^2 ~ 9.7536 m/s^2)
pos0 = [0, 10]#(4ft ~ 1.2192 m) 
drag = 0.25
t_arr = np.linspace(0,50,10000)

projectile_motion(V0, neg_g, pos0, drag, t_arr)
