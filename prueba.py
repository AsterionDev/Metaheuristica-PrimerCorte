import numpy as np
# from numpy.core.numerictypes import obj2sctype

# def verify(array):
#     if len(set(array)) < len(array):
#         return False
#     return True

# def closer(array):
#         auxLi=[]
#         for (distance,index) in array:
#             auxLi.append((index, distance ))
#         orderedList= sorted(auxLi, key=lambda tup: tup[1])
#         return orderedList
# cells = np.arange(10)
# cells = cells*-1
# arr=[1,2,3]
# cells = np.array(arr)
# print(verify(arr))
# print(cells)
# t=122%2

# distancias = [10, 20, 30, 40, 0]
# distancias = np.array(distancias)

# distancias = closer(distancias.tolist())
# print (distancias)

# # li= [(0,4),(1,3),(2,6),(3,1)]
# # x=[None]*10

# # x[0]=3
# # print(x)
# # print(verify(x))
# # sorted_li = sorted(li, key=lambda tup: tup[1])
# # print(li.pop(0))
# # print(li.pop(0))
# # print(sorted_li)
cells= np.array([0,1,2,3,4,5,6,7,8,9])
pos = np.random.choice(np.arange(1, 10), 2, replace=False)
print(pos)
pos.sort()
i = pos[0]
k = pos[1]
print(cells)
cells[i:k] = cells[k-1:i-1:-1]
print(pos)
print(i)
print(k)
print(cells)