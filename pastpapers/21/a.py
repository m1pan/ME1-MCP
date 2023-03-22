import numpy as np
import matplotlib.pyplot as plt
import random as rn

cid = [0,1,8,5,3,1,8,9]

#Create and fill matrix A
A = np.zeros((8,8))
A[:,0] = cid
A[:,-1] = cid[::-1]

#create and fill matrix B
B = np.zeros((8,8))
B[0,:] = cid
B[-1,:] = cid[::-1]
print(B)

#compute D
D = np.zeros((8,8))
add = A+B
minus = A-B
for i in range(8):
    for j in range(8):
        for k in range(8):
            D[i,j] += add[i,k]*minus[k,j]
