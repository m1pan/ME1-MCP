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
plt.figure(1)
plt.plot([0,L],[D/2,D/2])
plt.plot([0,L],[-D/2,-D/2])


position = (D/(np.tan(theta)*2),D/2)
theta1 = np.pi/2 - theta
path = [(0,0),position]
N = 1
while position[0]<=L:
    xnew = position[0] + D/np.tan(theta1)
    ynew = -position[1]
    position = (xnew,ynew)
    path.append(position)
    N += 1
plt.plot([i[0] for i in path],[i[1] for i in path],c='r')

print(N)

#Question 3
with open('xaxis.txt','r') as f:
    xaxis = [float(i) for i in f]

def factorial(N):
    if N ==1:
        return 1
    s = 0
    s = N * factorial(N-1)
    return s
y = []
for j in range(len(xaxis)):
    sum = 0
    for i in range(0,11):
        sum += (xaxis[j]**(2*i))*((-1)**i)/factorial(2*i+1)
    y.append(sum)


deriv = []
for i in range(1,len(y)-1):
    deriv.append((y[i+1]-y[i-1])/(xaxis[i+1]+xaxis[i-1]))

plt.figure(2)
plt.plot(y,xaxis)
plt.plot(deriv,xaxis[1:len(xaxis)-1],c='r')
plt.show()