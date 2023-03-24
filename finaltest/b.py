#CID 01853189
import numpy as np
import matplotlib.pyplot as plt
import random as rn

cid = [0,1,8,5,3,1,8,9]

#Task B
#open matrix.txt and read into a tmp list
with open('Matrix.txt','r') as f:
    data = [float(i) for i in f]

#initialise matrix A
A = np.zeros((7,7))
#fill A
for i in range(7):
    A[i] = data[i*7:i*7+7]

#initalise matrix C
C = np.zeros((A.shape[0]+1,A.shape[1]+1))
#fill matrix C
C[1:,1:] = A

#find largest value of A in each column
#initialise empty list for largest values
colA = []
#iterate through columns and fill colA
for i in range(7):
    largest = 0
    #iterate through individual columns
    for j in A[:,i]:
        if j > largest:
            largest = j
    colA.append(largest)

#find largest value of A in each row, same as columns
#initialise empty list for largest values
rowA = []
#iterate through columns and fill rowA
for i in range(7):
    largest = 0
    #iterate through individual rows
    for j in A[i]:
        if j > largest:
            largest = j
    rowA.append(largest)

#fill column and row of C
C[0,1:] = colA
C[1:,0] = rowA

#define diagonals to calculate sum of diagonal and antidiagonal in C
def Diagonals(c):
    #initialise diagonal and antidiagonal sum
    diag=0
    anti=0
    #iterate over matrix to find sums
    for i in range(c.shape[0]):
        diag += c[i,i]
        anti += c[i,-i-1]
    return (diag,anti)

#define function to find minor of matrix
def Minor(A,i,j):
    #check for square matrix
    if A.shape[0] != A.shape[1]:
        return 0
    size = A.shape[0]
    c = np.zeros((size - 1, size - 1))
    #fill c by quadrants
    #top left
    c[:i,:j] = A[:i,:j]
    #top right
    c[:i,j:] = A[:i,j+1:]
    #bottom left
    c[i:,:j] = A[i+1:,:j]
    #bottom right
    c[i:,j:] = A[i+1:,j+1:]
    return c

#define function to find determinant of matrix
def determinant(A):
    n = A.shape[0]
    #check for square matrix
    if n != A.shape[1]:
        return 0
    #basic determinant of 2x2 matrix
    elif n == 2:
        return A[0,0]*A[1,1] - A[0,1]*A[1,0]
    #recursive loop
    else:
        det = 0
        for i in range(n):
            det += A[0,i] * ((-1)**i) * determinant(Minor(A,0,i))
        return det

#find sum of all minor matrices in C
#initialise sum
S = 0
for i in range(C.shape[0]):
    for j in range(C.shape[1]):
        S += determinant(Minor(C,i,j))

#define transpose
def transpose(r):
    row0 = r.shape[0]
    col0 = r.shape[1]
    #initialise new transposed matrix
    c = np.ndarray((col0,row0))
    #iterate over r
    for i in range(row0):
        for j in range(col0):
            c[j,i] = r[i,j]
    return c

#initialise new matrix D
D = np.zeros(C.shape)
#fill D with each transposed quadrant of C
#nw quadrant
D[:4,:4] = transpose(C[:4,:4])
#ne quadrant
D[:4,4:] = transpose(C[:4,4:])
#sw quadrant
D[4:,:4] = transpose(C[4:,:4])
#se quadrant
D[4:,4:] = transpose(C[4:,4:])
print(D)