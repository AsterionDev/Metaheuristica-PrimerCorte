from io import SEEK_CUR
import numpy as np
from numpy.lib.function_base import append
from tsp import tsp

class solution:
    def __init__(self, p: tsp):
        self.problem = p
        self.cells = np.zeros(self.problem.size, int)
        self.fitness = 0.0

    def from_solution(self, origin):
        self.problem = origin.problem
        self.cells = np.copy(origin.cells)
        self.fitness = origin.fitness

    def randomInitialization(self):
        #self.cells = np.arange(self.problem.size)
        self.cells = np.random.choice(self.problem.size, self.problem.size, replace=False)
        self.fitness = self.problem.evaluate(self.cells)

    def tweak(self):
        #print(self.cells, ' fitness = ', self.fitness)
        pos = np.random.choice(np.arange(1, self.problem.size), 2, replace=False)
        pos.sort()
        i = pos[0]
        k = pos[1]
        self.cells[i:k] = self.cells[k-1:i-1:-1]
        self.fitness = self.problem.evaluate(self.cells)
        #print(self.cells, ' fitness = ', self.fitness)

    def show(self):
        print(self.cells)
        print(self.fitness)

    def ourInitialization(self):
        self.cells = []
        for i in range(self.problem.size):
            self.cells.append(None)
            if i%2 == 0 :
                self.cells[i] = np.random.choice(self.problem.size)
                while(self.verify(self.cells)==False):
                    self.cells[i] = np.random.choice(self.problem.size)
            else:
                orderedDistanceList = self.closer(self.problem.distances[self.cells[i-1]])
                self.cells[i]=orderedDistanceList.pop(0)[0]
                while(self.verify(self.cells)==False):
                    self.cells[i]=orderedDistanceList.pop(0)[0]
        self.cells= np.array(self.cells)
        self.fitness = self.problem.evaluate(self.cells)

    def verify(self,array):
        if len(set(array)) < len(array):
            return False
        return True
    
    def closer(self, array):
        auxLi=[]
        for i in range(len(array)):
            auxLi.append((i, array[i] ))
        orderedList= sorted(auxLi, key=lambda tup: tup[1])
        return orderedList

