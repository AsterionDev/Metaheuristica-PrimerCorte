import numpy as np


class Rastrigin:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub
        self.optimun = 0.0

    def evaluate(self, cells):
        summa = (np.power(cells,2) -10 * np.cos(2* np.pi * cells) +10).sum()
        return summa
    
    def __str__(self):
        return "Rastrigin-lb:"+str(self.lowerbound) + "-up:"+str(self.upperbound)
