import numpy as np


import numpy as np
from pandas import array

filename= 'Datos/regresion.txt'
file1 = open(filename, 'r')
lines = file1.readlines()

name=filename
size = len(" ".join(lines[0].split()).split(" "))-1
print(size)

matrizX=[]
arregloY=[]

for line in lines[1:]:
    matrizX.append(" ".join(line.split()).split(" ")[:-1])
    arregloY.append(" ".join(line.split()).split(" ")[-1])


print(matrizX[0])
# distances = np.zeros(( size,  size), dtype=float)

# x = np.zeros( size, float)
# y = np.zeros( size, float)
# positionLine = 1
# for i in range(0,  size):
#     line = lines[positionLine].split(' ')
#     x[positionLine - 1] = float(line[0])
#     y[positionLine - 1] = float(line[1])
#     positionLine = positionLine + 1