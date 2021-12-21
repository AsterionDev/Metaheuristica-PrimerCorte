import numpy as np
from tsp import tsp
from iteration_utils import duplicates


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
        self.cells = np.arange(self.problem.size)
        #Inicializar un arreglo vacio de tamaño size
        #For rango tamaño
            #si i es impar:
                #generar valor aleatorio
                #Si no esta agregado agregarlo, si esta repetetir
            #Si es par:
                #sacar el más cercano del i-1
                #verificar si no esta, si esta repetir pero con el mas cercano -1 
        
        self.cells = np.random.choice(self.problem.size, self.problem.size, replace=False)
        self.fitness = self.problem.evaluate(self.cells)

    def verify(array):
        if len(set(array)) < len(array):
            return False
        return True
