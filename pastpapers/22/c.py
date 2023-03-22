import numpy as np
import matplotlib.pyplot as plt
import random as rn

#Task C
Nmax = 1000

#spacial plot
Rad = 0.4
Rtheta = range(0,360)
for theta in Rtheta:
    thetar = theta * np.pi / 180
    plt.scatter(Rad*np.cos(thetar)-1,Rad*np.sin(thetar)+2,s=3,c='b')
    plt.scatter(Rad*np.cos(thetar)-2,Rad*np.sin(thetar)+1,s=3,c='b')

bx = np.arange(-4,0.1,0.1)
by = bx + 4
plt.plot(bx,by,linewidth=3,c='b')
bx = np.arange(-2,0.1,0.1)
by = bx + 2
plt.plot(bx,by,linewidth=3,c='b')
plt.plot([-4,-2],[0,0],linewidth=3,c='b')
plt.grid()

ant = (-3,0)
path = [(-3,0)]
N = 0

while ant[0] < 0 and N < 1000:
    dx = rn.random()*0.6-0.3
    dy = rn.random()*0.6-0.3
    new = (ant[0]+dx, ant[1]+dy)
    N += 1
    if new[1]>0 and new[0]+2<new[1]<new[0]+4 and (new[0]+1)**2+(new[1]-2)**2>Rad**2 and (new[0]+2)**2+(new[1]-1)**2>Rad**2:
        ant = new
        path.append(new)

if N >= 1000:
    print("The ant is exhausted.")
print(N)
plt.plot([i[0] for i in path],[i[1] for i in path],c='r')
plt.show()