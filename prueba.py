import numpy as np
def verify(array):
    if len(set(array)) < len(array):
        return False
    return True

cells = np.arange(10)
arr=[1,2,3]
print(verify(arr))
print(cells)