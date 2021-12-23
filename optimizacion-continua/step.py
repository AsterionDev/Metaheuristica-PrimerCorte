import numpy as np


class step:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub

    def evaluate(self, cells):
        newcells = np.floor(cells+0.5)
        summa = ( newcells * newcells).sum()
        return summa
    def __str__(self):
            return "Step-lb:"+str(self.lowerbound) + "-up:"+str(self.upperbound)