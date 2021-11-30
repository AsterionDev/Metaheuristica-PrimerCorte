import numpy as np
import solution as solution
from sphere import sphere

class solution:
    def __init__(self, d: int, f):
        self.size = d
        self.cells = np.zeros(self.size, float)
        self.fitness = 0.0
        self.function = f

    def from_solution(self, origin:solution):
        self.size = origin.size
        self.cells = np.copy(origin.cells)
        self.fitness = origin.fitness
        self.function = origin.function

    def randomInitialization(self):
        self.cells = np.random.uniform(low=self.function.lowerbound, high=self.function.upperbound,
                                       size=(self.size,))
        self.fitness = self.function.evaluate(self.cells)

    def tweak(self, bw: float):
        bandwidths = np.random.uniform(low=-bw, high=bw, size=(self.size,))
        self.cells = self.cells + bandwidths
        self.cells[self.cells < self.function.lowerbound] = self.function.lowerbound
        self.cells[self.cells > self.function.upperbound] = self.function.upperbound
        self.fitness = self.function.evaluate(self.cells)

    def show(self):
        print(self.cells)
        print(self.fitness)