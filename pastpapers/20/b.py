import numpy as np
import random as rn
import matplotlib.pyplot as plt

cid = [0,1,8,5,3,1,8,9]

R1 = 10
R2 = 20
Rtheta = range(0,360)
for theta in Rtheta:
    thetar = theta * np.pi / 180
    plt.scatter(R1*np.cos(thetar),R1*np.sin(thetar),s=3,c='b')
    plt.scatter(R2*np.cos(thetar),R2*np.sin(thetar),s=3,c='b')

ant = (0,18)
s1 = (cid[4]/10)+0.9
s2 = (cid[6]/10)+0.6
interval = s1 + s2
path = [ant]

plt.scatter(ant[0],ant[1],c='g')
count = 0
while ant[1] > 0:
    dx = (rn.random()*interval)-s1
    dy = (rn.random()*interval)-s1
    new = (ant[0]+dx, ant[1]+dy)
    count += 1

    #check if ant touches boundaries
    if new[0]**2+new[1]**2>R1**2 and new[0]**2+new[1]**2<R2**2:
        ant = new
        path.append(new)

plt.plot([i[0] for i in path],[i[1] for i in path],c='r')
plt.axis('equal')
plt.show()
print(count)
