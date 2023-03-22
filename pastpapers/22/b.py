import numpy as np
import matplotlib.pyplot as plt
import random as rn

def Minor(A,i,j):
    if A.shape[0] != A.shape[1]:
        return 0
    size = A.shape[0]
    c = np.zeros((size - 1, size - 1))
    c[:i,:j] = A[:i,:j]
    c[:i,j:] = A[:i,j+1:]
    c[i:,:j] = A[i+1:,:j]
    c[i:,j:] = A[i+1:,j+1:]
    return c
def determinant(A):
    n = A.shape[0]
    if n != A.shape[1]:
        return 0
    elif n == 2:
        return A[0,0]*A[1,1] - A[0,1]*A[1,0]

    else:
        det = 0
        for i in range(n):
            det += A[0,i] * ((-1)**i) * determinant(Minor(A,0,i))
        return det
    
def adjoint(A):
    N = A.shape[0]
    c = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            c[i,j] = ((-1)**(i+j)) * determinant(Minor(A,i,j))
    return transpose(c)

def inverse(A):
    return adjoint(A)/determinant(A)

def transpose(r):
    row0 = r.shape[0]
    col0 = r.shape[1]
    c = np.ndarray((col0,row0))
    for i in range(row0):
        for j in range(col0):
            c[j,i] = r[i,j]
    return c

#opening file
with open("Matrix.txt",'r') as f:
    huge = [int(i) for i in f]

A = np.ndarray((600,600))
for i in range(600):
    A[i] = huge[600*i:600*i+600]


av = np.zeros((60,60))
det = np.zeros((60,60))

for i in range(60):
    for j in range(60):
        sub = A[i*10:i*10+10,j*10:j*10+10]
        av[i,j] = sum(sum(sub))/100
        det[i,j] = np.linalg.det(sub)
        if det[i,j] != 0:
            A[i*10:i*10+10,j*10:j*10+10] = transpose(sub)

plt.imshow(A)
