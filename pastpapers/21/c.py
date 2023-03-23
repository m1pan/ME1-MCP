import numpy as np
import matplotlib.pyplot as plt
import random as rn

with open('Vax.txt','r') as f:
    data = [i.strip() for i in f]
DAYS = int(len(data)/5)

first = 0
second = 0
largest = ['',0]
pfizer = 0
astrozeneca = 0
x = range(1,DAYS+1)

for i in range(DAYS):
    set = [data[i*5]] + [int(i) for i in data[i*5+1:i*5+5]]
    first += set[1] + set[2]
    second += set[3] + set[4]
    pfizer += set[1] + set[3]
    astrozeneca += set[2] + set[4]
    plt.scatter(x[i],(set[1]+set[2]),c='b')
    plt.scatter(x[i],(set[3]+set[4]),c='r')
    if sum(set[1:]) > largest[1]:
        largest = [set[0],sum(set[1:])]

print(first)
print(second)
print(largest)
plt.legend(['first','second'])
plt.show()

