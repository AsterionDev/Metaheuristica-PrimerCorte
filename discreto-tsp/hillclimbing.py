from solution import solution
from tsp import tsp
import numpy as np


class hillclimbing:
    def __init__(self, maxIter: int):
        self.maxIterations = maxIter
    
    def hillClimbingClasic(self):
        self.evolve=self.clasicEvolve
        self.name="HC-Clasic"
    def hillClimbingModified(self, numInter):
        self.numInter= numInter
        self.evolve=self.ourEvolve
        self.name="HC-Modified-numInter:"+str(self.numInter)

    def clasicEvolve(self, problem: tsp):
        self.best = solution(problem)
        self.problem = problem
        x = np.arange(0, self.maxIterations)
        y = np.zeros(self.maxIterations, float)
        self.best.randomInitialization()
        for iteration in range(self.maxIterations):
            copyOfBest = solution(self.best.problem)
            copyOfBest.from_solution(self.best)
            copyOfBest.tweak()
            if copyOfBest.fitness < self.best.fitness:
                self.best.from_solution(copyOfBest)
            y[iteration] = self.best.fitness
        return y

    def ourEvolve(self, problem: tsp):
        self.best = solution(problem)
        self.problem = problem
        x = np.arange(0, self.maxIterations)
        y = np.zeros(self.maxIterations, float)
        self.best.ourInitialization()
        for iteration in range(self.maxIterations):
            copyOfBest = solution(self.best.problem)
            copyOfBest.from_solution(self.best)
            copyOfBest.ourTweak(self.numInter)
            if copyOfBest.fitness < self.best.fitness:
                self.best.from_solution(copyOfBest)
            y[iteration] = self.best.fitness
        return y
    
    def __str__(self):
        return self.name