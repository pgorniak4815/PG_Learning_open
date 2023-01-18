import numpy as np

number = 1000000
tau = 1.5

rand_sample = np.random.uniform(size=number)

emissions = -tau*np.log(rand_sample)

np.savetxt('data\emissions_times_exp.csv', emissions, delimiter = ',')