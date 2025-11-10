import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def sir(S0,I0, R0, beta, r, t_final):
    # S0: inital susceptible population (S(0))
    # I0: inital infected population (I(0))
    # R0: inital recovered population (R(0))
    # beta: infectivity coefficient
    # r: per capita recovery rate

    # array with sampling times
    t_arr = np.linspace(0, t_final,10000)

    # dy/dt = func(...)
    # y = [S, I, R]
    def func(t,y,beta,r):
        return [
                - 1 * beta * y[0] * y[1],
                beta * y[0] * y[1] - r * y[1],
                r * y[1]
                ]

    sol = solve_ivp(func, [0, t_final],[S0, I0, R0], args=(beta, r), t_eval = t_arr)

    fig, axs = plt.subplots(2, 2, figsize=(12,8), layout='constrained')
    fig.suptitle(f'SIR Model: S0 = {S0}, I0 = {I0}, R0 = {R0} beta = {beta}, r = {r}')
    axs[0,0].set(xlabel='Elapsed Time (days)', ylabel='Population')
    axs[0,0].plot(sol.t, sol.y[0], label = 'S(t)')
    axs[0,0].plot(sol.t, sol.y[1], label = 'I(t)')
    axs[0,0].plot(sol.t, sol.y[2], label = 'R(t)')
    axs[0,0].grid()
    axs[0,0].legend()

    axs[0,1].plot(sol.y[0], sol.y[1])
    axs[0,1].set(xlabel='Susceptible Population', ylabel='Infected Population')
    axs[0,1].grid()

    axs[1,0].plot(sol.y[0], sol.y[2])
    axs[1,0].set(xlabel='Susceptible Population', ylabel='Recovered Population')
    axs[1,0].grid()

    axs[1,1].plot(sol.y[1], sol.y[2])
    axs[1,1].set(xlabel='Infected Population', ylabel='Recovered Population')
    axs[1,1].grid()
    plt.show()

    if 0 == any(sol.y[0]):
        print('Prey was Extinguished')
    if 0 == any(sol.y[1]):
        print('Predator was Extinguished')
    
#=====================================================================
#Define inputs
S0 = 900
I0 = 1
R0 = 0
beta = 0.005
r = 1
t_final = 10

sir(S0, I0, R0, beta, r, t_final)
