import numpy as np
import matplotlib.pyplot as plt
import random as rn

cid = [0,1,8,5,3,1,8,9]
def factorial(n):
    if n <= 1:
        return 1
    sum = n * factorial(n-1)
    return sum

def Series(N):
    P=0
    for i in range(1,N+1):
        sub = 0
        for k in range(1,i+1):
            sub += (cid[3] + 10)**(k-3)
        P += sub/factorial(i-1)
    return P

N = range(1,51)
P = [Series(i) for i in N]
plt.plot(N,P)
plt.show()