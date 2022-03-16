from cProfile import label
from ctypes import sizeof
import numpy as np
import matplotlib.pyplot as plt
import math 
import random
import time

def binning(x, size = 10):   
    number_of_bins = round((max(x)-min(x))/size) + 1
    
    bins = [i*size for i in range(0,number_of_bins)]
    bins_label = [i+(size)/2 for i in bins]

    values = [0]*len(bins_label)

    binned_data = dict(zip(bins_label,values))

    for item in x:
        n=0
        for lim in bins:
            if item <= lim+size:
                binned_data[bins_label[n]]+=1
                (binned_data[bins_label[n]])
                break
            n+=1

    return(binned_data)


random.seed(100)
number = 1000000
emissions = []
tau = 30

for i in range(number-1):
    
    t = -tau*math.log(random.uniform(0,1))
    emissions.append(t)

binned_emissions = binning(emissions)
EM = binned_emissions.items()
EM = sorted(EM) 
x, y = zip(*EM)

plt.plot(x,y,'ro')
plt.yscale('log')
plt.savefig("mygraph.png")




