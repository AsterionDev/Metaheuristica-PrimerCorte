from solution import solution
from knapsack import knapsack
import numpy as np


class hillclimbing:
    def __init__(self, maxIter: int):
        self.maxIterations = maxIter

    def hillClimbingClasic(self):
        self.evolve=self.clasicEvolve
        self.name="HC-Clasic"

    def hillClimbingModified(self, numDeleted):
        self.numDeleted= numDeleted
        self.evolve=self.ourEvolve
        self.name="HC-Modified-numDeleted:"+str(self.numDeleted)

    def clasicEvolve(self, problem: knapsack):
        self.best = solution(problem)
        self.problem = problem
        x = np.arange(0, self.maxIterations)
        y = np.zeros(self.maxIterations, float)
        self.best.randomInitialization()
        for iteration in range(self.maxIterations):
            copyOfBest = solution(self.best.problem)
            copyOfBest.from_solution(self.best)
            copyOfBest.tweak()
            if copyOfBest.fitness > self.best.fitness:
                self.best.from_solution(copyOfBest)
            y[iteration] = self.best.fitness
        return y

    def ourEvolve(self, problem: knapsack):
        self.best = solution(problem)
        self.problem = problem
        x = np.arange(0, self.maxIterations)
        y = np.zeros(self.maxIterations, float)
        self.best.ourInitialization()
        for iteration in range(self.maxIterations):
            copyOfBest = solution(self.best.problem)
            copyOfBest.from_solution(self.best)
            copyOfBest.ourTweak(self.numDeleted)
            if copyOfBest.fitness > self.best.fitness:
                self.best.from_solution(copyOfBest)
            y[iteration] = self.best.fitness
        return y
    def __str__(self):
        return self.name
