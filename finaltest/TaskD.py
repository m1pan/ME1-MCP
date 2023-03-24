#CID 01853189
import numpy as np
import matplotlib.pyplot as plt
import random as rn

cid = [0,1,8,5,3,1,8,9]

#Task D

#define recrusive function sequence
def Sequence(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        y = Sequence(n-1) - (n+1)*Sequence(n-2)
        return y

#print first 20 values of sequence
print([Sequence(i) for i in range(1,21)])

    