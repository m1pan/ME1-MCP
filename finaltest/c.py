#CID 01853189
import numpy as np
import matplotlib.pyplot as plt
import random as rn

cid = [0,1,8,5,3,1,8,9]

#Task C
#initialise position
position = (0,0)
#initialise path with initial position
path = [(0,0)]

#define winning
WIN = 100

#initalise horizontal distance walked
D = 0
#initialise steps
steps = 0

#keep mario moving till he crosses y = 100
while position[1] < 100:
    #generate random ints between 1 and 10 for dx and dy
    dx = int(rn.random()*9+1)
    dy = int(rn.random()*9+1)
    #new position coords
    xnew = position[0] + dx
    ynew = position[1] + dy

    #add horizontal distance
    D+=dx

    #add step
    steps+=1

    #move horizontal then vertical
    path.append((xnew,position[1]))
    path.append((xnew,ynew))

    #change position to new coords
    position = (xnew,ynew)
    
print(f"horizontal distance = {D}")
print(f"Steps = {steps}")

#plot marios path in red
plt.plot([i[0] for i in path],[i[1] for i in path],c='r')
plt.show()


