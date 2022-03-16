import numpy as np
import matplotlib.pyplot as plt
import math 
import random
import time

def FD_bins_n(x):
    """returns the number of histogram bins for x dataset according to the Freedman-Diacons rule"""
    median = np.median(x)

    Q1 = x[x<median]
    Q3 = x[x>median]

    q1 = np.median(Q1)
    q3 = np.median(Q3)

    iqr = q3 - q1

    #histogram bins width according Freedmen Diacons rule
    bin_width = 2 * iqr * (len(x) ** (-1/3))

    #calculating number of bins with rounding
    bins = round((x.max() - x.min()) / bin_width)

    return bins

def Rice_bins_n(x):
    """returns the number of histogram bins for x dataset according to the Riece rule"""
    n = len(x)
    bins = math.ceil(2*n**(1/3))

    return bins

start = time.perf_counter_ns()

random.seed(100)
number = 100000;
emissions = np.array([]);

time_of_integration = 100;

tau = 200

for i in range(number-1):
    for s in range(time_of_integration):

        lamb = (1/tau)*s
        chance = random.uniform(0,1)
        if chance <= lamb:
            emissions = np.append(emissions, s)
            break;


print(np.sort(emissions))

bins = FD_bins_n(emissions)

print(bins)

plt.hist(emissions, bins=10, rwidth=0.8, log = True, align='right', edgecolor='black')

plt.ylabel("Int.")
plt.xlabel("Time [ns] ")
plt.draw()
end = time.perf_counter_ns()

print((end - start)*10**(-9))

plt.show()




