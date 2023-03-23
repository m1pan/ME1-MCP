import numpy as np
import random as rn
import matplotlib.pyplot as plt

#question 1
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

def MatOp(A):
    size = A.shape
    C = D = E = np.zeros(size)
    for i in range(size[0]):
        D[i,i] = A[i,i]
        for j in range(size[0]):
            if j > i:
                E[i,j] = A[i,j]
            elif j<i:
                D[i,j] = A[i,j]
    T = MatMat(C,D) + MatMat(E,D)
    return T

#Pipe
theta = np.pi/6
D = 10
L = 20
