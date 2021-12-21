import numpy as np
import math as mt

class Ackley:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub
        self.optimun = 0.0

    def evaluate(self, cells):        
        a=20
        b=0.2 
        c=2*np.pi 
        cells = np.asarray_chkfinite(cells)
        n = len(cells)
        s1 = (np.power(cells,2)).sum()
        s2 = (np.cos(c*cells)).sum()
        return -a*mt.exp( -b*np.sqrt( s1 / n )) - mt.exp( s2 / n ) + a + mt.exp(1)
