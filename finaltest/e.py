#CID 01853189
import numpy as np
import matplotlib.pyplot as plt
import random as rn

cid = [0,1,8,5,3,1,8,9]

#Task E

#define trigonometry class
class Trigonometry:
    def __init__(self, x:list, unit:bool):
        self.x = x
        self.unit = unit
    
    #define cos
    def cos(self):
        if self.unit == True:
            return np.cos(self.x)
        elif self.unit == False:
            #initialise temporary list to store radian angles
            tmp =[]
            #convert degrees to radians by iterating over all angles
            for i in self.x:
                tmp.append(i * np.pi / 180)
            return np.cos(tmp)

xr = Trigonometry(np.linspace(0,2*np.pi,100),True)
xd = Trigonometry(np.linspace(0,360),False)

#cos xr
yr = xr.cos()

#cos xd
yd = xd.cos()

#plot yr against xr and yd against xd
#configuring two sub plots
fig, (ax1,ax2) = plt.subplots(2)
#plot yr against xr
ax1.plot(xr.x,yr,c='b')
ax1.set_title('Radians')

#plot yd against xd
ax2.plot(xd.x,yd,c='r')
ax2.set_title('Degrees')
plt.show()