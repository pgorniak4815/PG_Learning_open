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








