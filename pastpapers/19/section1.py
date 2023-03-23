import numpy as np
import random as rn
import matplotlib.pyplot as plt

def swap(a,b):
    (b,a) = (a,b)

def trace(A):
    N = len(A)
    T = 0
    for i in range(0,N):
        T += A[i][i]
    return T

def Twins(n):
    S = 0
    if n == 1:
        return n*((-1)**n)
    S += n*((-1)**n)*Twins(n-1)
    return S

