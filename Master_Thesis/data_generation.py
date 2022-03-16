import math 
import random
import numpy as np


random.seed(100)


number = 1000000
tau = 15


emissions = []


for i in range(number-1):
    
    t = -tau*math.log(random.uniform(0,1))
    emissions.append(t)

emissions_np = np.array(emissions)
np.savetxt('Master_Thesis\data\emissions_times.csv', emissions_np, delimiter = ',')




