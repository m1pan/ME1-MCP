#CID 01853189
import numpy as np
import matplotlib.pyplot as plt
import random as rn

cid = [0,1,8,5,3,1,8,9]

#Task A

#define a factorial function
def factorial(n):
    if n <= 1:
        return 1
    sum = n * factorial(n-1)
    return sum

#define function series to take in n and output s
def Series(N):
    #initialise S
    S = 0
    #sum from -N to N+2
    for j in range(-N,N+3):
        #initialise sub sum
        sub = 0
        #sub sum from k=2 to 10j
        for k in range(2,(10*j)+1,2):
            sub += ((-1)**j)*(j**k)/factorial(k)
        S += sub/factorial(j)
    return S


#initialise empty list S
S = []

#compute sum 8 times with cid and fill up S
for i in range(8):
    S.append(Series(cid[i]))

plt.plot(range(8),S)
plt.show()

