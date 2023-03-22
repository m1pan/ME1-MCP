import numpy as np
import matplotlib.pyplot as plt
import random as rn

x = np.arange(-2*np.pi,2*np.pi,0.01) 
y = np.sin(x) 
xm = [i for i in x if (-2*np.pi<=i<=-np.pi or 0<=i<=np.pi)] 
ym = np.sin(xm) 
plt.scatter(x,y,linewidth=10,c='b') 
plt.scatter(xm,ym,linewidth=1,c='r') 
plt.grid() 
plt.legend(['y','ym']) 
plt.show()