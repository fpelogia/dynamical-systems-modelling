import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def predator_prey(x0,y0,a,b):
    #x0: inital prey population (e.g Rabbits)
    #y0: initial predator population (e.g Foxes)
    #a: contact coefficient of preys with predators
    #b: contact coefficient of predators with preys

    # array with sampling times
    t_arr = np.linspace(0,50,10000)

    # dy/dt = func(...)
    # y = [x,y]
    def func(t,y,a,b):
        return [y[0] - a*y[0]*y[1],
                -y[1] + b*y[0]*y[1],]

    sol = solve_ivp(func, [0,50],[x0,y0], args=(a,b), t_eval = t_arr)

    fig, axs = plt.subplots(1, 2, figsize=(12,4))
    fig.suptitle(f'Predator-Prey Model: x0 = {x0}, y0 = {y0}, a = {a}, b = {b}')
    axs[0].plot(sol.t, sol.y[0], label = 'Prey')
    axs[0].set(xlabel='Elapsed Time (days)', ylabel='Population')
    axs[0].plot(sol.t, sol.y[1], label = 'Predator')
    axs[0].grid()
    axs[0].legend()

    axs[1].plot(sol.y[0], sol.y[1])
    axs[1].set(xlabel='Prey Population', ylabel='Predator Population')
    axs[1].grid()
    plt.show()

    if 0 == any(sol.y[0]):
        print('Prey was Extinguished')
    if 0 == any(sol.y[1]):
        print('Predator was Extinguished')
    
#=====================================================================
#Define inputs
x0 = 150
y0 = 100
a = 0.01
b = 0.01

predator_prey(x0,y0,a,b)
