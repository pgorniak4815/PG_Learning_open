from cProfile import label
from ctypes import sizeof
import numpy as np
import matplotlib.pyplot as plt
import math 
import random
import time

def binning(x, size = 10**(-9)):

    number_of_bins = np.round(max(x)/size) + 1;
    bins = range(0,number_of_bins*size,size);
    
    bins_label = [x for i in bins (x+size)/2];

    binned_data = {bins_label:[0]*len(bins_label)}

    n=0;

    for item in x:
        for lim in bins:
            if item >= lim:
                binned_data[bins_label[n]] =+ 1;
    
    return binned_data;


random.seed(100)
number = 100000;
emissions = [];
tau = 200

for i in range(number-1):
    
    t = -tau*math.log(random.uniform(0,1))
    emissions.append(t);



x = emissions;

size = 10;
number_of_bins = round((max(x)-min(x))/size) + 1;

bins = [i*size for i in range(0,number_of_bins)];

bins_label = [i+(size)/2 for i in bins];

values = [0]*len(bins_label)

binned_data = dict(zip(bins_label,values));


n=0;

for item in x:
    for lim in bins:
        if item <= lim:
            binned_data[bins_label[n]]+=1;
            break
        n+=1;
    n=0;    

EM = binned_data.items()
EM = sorted(EM) 
x, y = zip(*EM)

plt.plot(x,y,'ro')
plt.savefig("mygraph.png")




