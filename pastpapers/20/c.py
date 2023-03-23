import numpy as np
import random as rn
import matplotlib.pyplot as plt

cid = [0,1,8,5,3,1,8,9]

with open('CV19.txt','r') as f:
    dat = [i.strip() for i in f]

total = 0
weekly = []
exceed = []
percincrement = []
weeks = int(len(dat)/15)
highest = ['',0]

datarange = range(2,15,2)


for i in range(weeks):
    tmp = [i for i in dat[i*15:i*15+15]]
    weeksum = 0
    for j in datarange:
        total += int(tmp[j])
        weeksum += int(tmp[j])
        if int(tmp[j]) > 2000:
            exceed.append(tmp[j-1])
    weekly.append(weeksum)
    if i > 0:
        percent = ((weeksum - weekly[i-1])/weekly[i-1])*100
        percincrement.append(percent)
    if weeksum > highest[1]:
        highest = [tmp[0],weeksum]
    
print(total)
print(weekly)
print(exceed)
print(highest)
print(percincrement)
