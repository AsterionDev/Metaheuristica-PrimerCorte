import numpy as np

bw=10
best = np.random.normal(0,100)
bandwidths = np.random.uniform(low=-bw, high=bw, size=(10,))
print(best)
print(bandwidths)