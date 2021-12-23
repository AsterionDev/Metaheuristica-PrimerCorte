import numpy as np
import math as mt
class Schwefel:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub
        self.optimun = 420.9687

    def evaluate(self, cells):        
        alpha = 418.982887
        fitness = 0
        cells = np.asarray_chkfinite(cells)
        n = len(cells)
        
        for i in range(len(cells)):
            fitness -= cells[i]*mt.sin(mt.sqrt(mt.fabs(cells[i])))
        return float(fitness) + alpha*len(cells)  
        
    def __str__(self):
        return "Schwefel-lb:"+str(self.lowerbound) + "-up:"+str(self.upperbound)
