import numpy as np
import random as rn
import matplotlib.pyplot as plt

cid = [0,1,8,5,3,1,8,9]

def transpose(r):
    row0 = r.shape[0]
    col0 = r.shape[1]
    c = np.ndarray((col0,row0))
    for i in range(row0):
        for j in range(col0):
            c[j,i] = r[i,j]
    return c

def MatMat(A,B):
    NrA = A.shape[0]
    NcA = A.shape[1]
    NrB = B.shape[0]
    NcB = B.shape[1]
    
    if NcA != NrB:
        return 0
    C = np.zeros((NrA,NcB))
    for i in range(NrA):
        for j in range(NcB):
            for k in range(NcA):
                C[i,j] += A[i,k] * B[k,j]
    return C

a = np.zeros((8,8))
b = np.ndarray((8,1))

#populate b
b[:,0] = cid

#populate a
for i in range(8):
    a[i,i] = a[i,-i-1] = cid[i]

#compute array c

c = MatMat((a-transpose(a)),b)
print(c)

