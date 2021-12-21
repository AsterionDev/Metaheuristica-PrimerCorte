import numpy as np

class Griewank:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub
        self.optimin = 0.0

    def evaluate(cells):
        index = np.arange(1, len(cells)+1)
        t1=(np.power(cells, 2)).sum / 4000
        t2= np.prod(np.cos(cells / np.sqrt(index)))
        return t1 - t2 +1
