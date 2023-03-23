import numpy as np
import matplotlib.pyplot as plt
import random as rn

cid = [0,1,8,5,3,1,8,9]

N = 100000
def func(x):
    f = np.exp(-((x-0.5)**2)/((0.1+(cid[5]/20))**2))
    return f

bellx = np.linspace(0,1,N)
belly = func(bellx)
plt.plot(bellx,belly,c='g')

low = []
high = []

i = 0
while i < N:
    i+=1
    x = rn.random()
    y = rn.random()
    if y > func(x):
        high.append((x,y))
    elif y < func(x):
        low.append((x,y))
    else:
        continue

plt.scatter([i[0] for i in low],[i[1] for i in low],c='r',s=2)
plt.scatter([i[0] for i in high],[i[1] for i in high],c='b',s=2)
print(len(low)/len(high))
plt.show()
