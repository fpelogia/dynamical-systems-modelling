import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

"""
BSD 3-Clause License
Copyright (c) 2026, Frederico J. R. Pelogia
All rights reserved.
See the full license inside LICENSE.txt file 

Formulation based on the following book:
 - "Iniciação à Física Matemática: Modelagem de Processos e Métodos de Solução"
    written by Juan López Gondar and Rolci Cipolatti.
"""

# Simulate Phase 1 - Self propulsion
def simulate_propulsion(t0, tf_prop, pos0, vel0, v_fb, g, c, b, M):
    t_arr = np.linspace(t0,tf_prop,1000) # array with sampling times (s)

    # Define dynamics
    #dy/dt = func(t, y, ...params)
    # y = [pos, vel] 
    def dydt(t, y, v_fb, g, c):
        pos, vel = y
        return [vel, (c*v_fb - g*M(0) - b*vel)/M(t)]

    # Solve the ODE 
    sol = solve_ivp(dydt, [t0,tf_prop],[pos0,vel0],args=(v_fb, g, c), t_eval=t_arr)
    pos, vel = sol.y

    return t_arr, pos, vel


# Simulate Phase 2 - Free motion (when fuel is over)
def simulate_free_motion(tf_prop, tf, pos0, vel0, g, b, Mr):
    t_arr = np.linspace(tf_prop,tf,1000) # array with sampling times (s)

    # Define dynamics
    #dy/dt = func(t, y, ...params)
    # y = [pos, vel] 
    def dydt(t, y, g):
        pos, vel = y
        return [vel, -g -b*vel/Mr]

    # Solve the ODE 
    sol = solve_ivp(dydt, [tf_prop,tf],[pos0,vel0],args=(g,), t_eval=t_arr)
    pos, vel = sol.y

    return t_arr, pos, vel

# Simulate full rocket dynamics 
def rocket():

    # Define constants and functions
    Mr = 5; # Empty rocket mass (kg) 
    m0 = 15; # Initial fuel mass (kg)
    c = 2 # Fuel burn rate (kg/s)
    m = lambda t: m0 - c*t
    M = lambda t: Mr + m(t)
    v_fb = 150; # Fuel velocity (m/s)
    pos0 = 0 # Initial position (m)
    vel0 = 0 # Initial Velocity (m/s)
    g = 9.81 # Gravitational acceleration (m/s^2)
    b = 1.1 # Air drag

    t0 = 0 # Initial time (s)
    tf_prop = m0/c # time with self propulsion (s)
    tf = tf_prop + 30 # Final time (s)

    # Simulate Phase 1 - Self propulsion
    t_prop, pos_prop, vel_prop = simulate_propulsion(t0, tf_prop, pos0, vel0, v_fb, g, c, b, M)
    pos0 = pos_prop[-1] # Initial position (m)
    vel0 = vel_prop[-1] # Initial Velocity (m/s)

    # Simulate Phase 2 - Free motion (when fuel is over)
    t_free, pos_free, vel_free = simulate_free_motion(tf_prop, tf, pos0, vel0, g, b, Mr)

    # Join arrays with full simulation history
    t = np.hstack([t_prop, t_free])
    pos = np.hstack([pos_prop, pos_free])
    vel = np.hstack([vel_prop, vel_free])

    # Exclude data after ground collision
    index_ground = 0
    for p in pos:
        if index_ground > 0 and p < 0:
            break
        else:
            index_ground += 1
    print(index_ground)

    t = t[:index_ground]
    pos = pos[:index_ground]
    vel = vel[:index_ground]

    fig, axs = plt.subplots(1, 2)
    fig.suptitle('Rocket Motion')
    axs[0].set_xlabel('t (s)')
    axs[0].set_ylabel('Position (m)')
    axs[0].plot(t, pos)
    axs[1].set_xlabel('t (s)')
    axs[1].set_ylabel('Velocity (m/s)')
    axs[1].plot(t, vel)

    plt.show()

#=================================================================

if __name__ == '__main__':
    rocket()
