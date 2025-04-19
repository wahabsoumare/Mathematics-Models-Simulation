import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class SIRS:
    def __init__(self, beta, gamma, delta, N = 1000):
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.N = N

    def model(self, y, t):
        S, I, R = y
        dS = -self.beta * S * I + self.delta * R
        dI = self.beta * S * I - self.gamma * I
        dR = self.gamma * I - self.delta * R
        return [dS, dI, dR]

    def solve(self, I0 = 1, R0 = 0):
        S0 = self.N - (I0 + R0)
        self.times = np.linspace(0, 160, 160)
        y0 = [S0 / self.N, I0 / self.N, R0 / self.N]
        self.solution = odeint(self.model, y0, self.times)
        self.S, self.I, self.R = self.solution.T

    def show_graph(self):
        plt.figure(figsize = (10, 5))

        plt.plot(self.times, self.S, label = 'Susceptibles')
        plt.plot(self.times, self.I, label = 'Infectés')
        plt.plot(self.times, self.R, label = 'Rétablis')
        plt.xlabel('Temps (jours)')
        plt.ylabel('Proportion de la population')
        plt.title('Simulation du modèle SIRS')
        plt.legend()
        plt.grid()

        plt.show()

    def simulate(self):
        fig, axis = plt.subplots(figsize = (10, 5))
        axis.set_xlim([min(self.times), max(self.times)])
        axis.set_ylim([0, max(max(self.S), max(self.I), max(self.R)) * 1.1])

        line_S, = axis.plot([], [], color = 'royalblue', label = 'Susceptibles')
        line_I, = axis.plot([], [], color = 'crimson', label = 'Infectés')
        line_R, = axis.plot([], [], color = 'forestgreen', label = 'Rétablis')

        def update(frame):
            line_S.set_data(self.times[:frame], self.S[:frame])
            line_I.set_data(self.times[:frame], self.I[:frame])
            line_R.set_data(self.times[:frame], self.R[:frame])

            return line_S, line_I, line_R
        
        animation = FuncAnimation(fig = fig, func = update, frames = len(self.times), interval = 25, repeat = False, blit = True)
        plt.title('Simulation du modèle SIRS')
        plt.xlabel('Temps (jours)')
        plt.ylabel('Proportion de la population')
        plt.legend(loc = 'best')
        plt.grid()
        
        plt.show()

model = SIRS(beta = 0.3, gamma = 0.1, delta = 0.1)
model.solve()
model.simulate()