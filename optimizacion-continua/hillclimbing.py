from solution import solution
import numpy as np


class hillclimbing:
    def __init__(self, mi: int):
        self.maxiterations = mi
    
    def hillcilmbingClasico(self, bw: float):
        self.bandwith = bw
        self.evolve=self.clasicEvolve
        self.name="HC-Clasic-bandwith:"+str(self.bandwith)

    def hillcilmbingModified(self,tries: int, sigma: float):
        self.tries = tries
        self.sigma = sigma
        self.evolve=self.ourEvolve
        self.name="HC-Modified-tries:"+str(self.tries)+" sigma:"+str(self.sigma)

    def clasicEvolve(self, f, d: int):
        self.function = f
        self.best=solution(d,f)
        x = np.arange(0, self.maxiterations)
        y = np.zeros(self.maxiterations, float)
        self.best.randomInitialization()
        for iteration in range(self.maxiterations):
            copyofbest = solution(self.best.size, self.best.function)
            copyofbest.from_solution(self.best)
            copyofbest.tweak(self.bandwith)
            if copyofbest.fitness < self.best.fitness:
                self.best.from_solution(copyofbest)
            y[iteration] = self.best.fitness
        return y

    def ourEvolve(self, f, d: int):
        self.function = f
        self.best=solution(d,f)
        x = np.arange(0, self.maxiterations)
        y = np.zeros(self.maxiterations, float)
        self.best.ourInitialization(self.tries)
        for iteration in range(self.maxiterations):
            copyofbest = solution(self.best.size, self.best.function)
            copyofbest.from_solution(self.best)
            copyofbest.ourTweak(self.sigma)
            if copyofbest.fitness < self.best.fitness:
                self.best.from_solution(copyofbest)
            y[iteration] = self.best.fitness
        return y

    def __str__(self):
        return self.name
