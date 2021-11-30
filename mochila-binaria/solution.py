import numpy as np
from knapsack import knapsack


class solution:
    def __init__(self, p: knapsack):
        self.problem = p
        self.cells = np.zeros(self.problem.size, int)
        self.fitness = 0.0
        self.weight = 0.0

    def from_solution(self, origin):
        self.problem = origin.problem
        self.cells = np.copy(origin.cells)
        self.fitness = origin.fitness
        self.weight = origin.weight

    def randomInitialization(self):
        positions = np.random.choice(self.problem.size, self.problem.size, replace=False)
        weight = 0
        for p in positions:
            if weight + self.problem.weights[p] < self.problem.capacity:
                self.cells[p] = 1
                weight = weight + self.problem.weights[p]
        self.fitness, self.weight = self.problem.evaluate(self.cells)

    def tweak(self):
        selectedPositions = np.where(self.cells == 1)[0]
        unselectedPositions = np.where(self.cells == 0)[0]
        x = np.random.randint(len(selectedPositions), size=1)
        elementToRemove = selectedPositions[x[0]]
        self.cells[elementToRemove] = 0
        self.weight = self.weight - self.problem.weights[elementToRemove]
        self.fitness = self.fitness - self.problem.profits[elementToRemove]

        empty = self.problem.capacity - self.weight
        while empty > 0 and len(unselectedPositions) > 0:
            fitUnselected = np.array([unselectedPositions, self.problem.weights[unselectedPositions]])
            fitUnselected = fitUnselected[:, np.where(fitUnselected[1, :] < empty)][0]
            unselectedPositions = np.copy(fitUnselected[0])

            if len(fitUnselected[0]) == 0:
                break

            elementToAdd = int(fitUnselected[0][np.random.randint(len(fitUnselected[0]))])
            self.cells[elementToAdd] = 1
            self.weight = self.weight + self.problem.weights[elementToAdd]
            self.fitness = self.fitness + self.problem.profits[elementToAdd]
            unselectedPositions = np.array(unselectedPositions[np.where(unselectedPositions != elementToAdd)],
                                           dtype=int)
            empty = self.problem.capacity - self.weight

    def show(self):
        print(self.cells)
        print(self.fitness)