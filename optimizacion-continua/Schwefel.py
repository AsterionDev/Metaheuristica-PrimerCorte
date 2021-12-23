import numpy as np
import math as mt
class Schwefel:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub
        self.optimun = 420.9687

    def evaluate(self, cells):        
        alpha = 418.982887
        cells = np.asarray_chkfinite(cells)
        n = len(cells)
        return 418.9829*n - ( cells * mt.sin( mt.sqrt( abs( cells )))).sum()
    
    def __str__(self):
        return "Schwefel-lb:"+str(self.lowerbound) + "-up:"+str(self.upperbound)
