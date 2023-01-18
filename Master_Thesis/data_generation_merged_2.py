"""
Second attempt at data generation and partitioning
""""

import numpy as np

number = 10000000
border = 10000

alfa = 1.5
xmin = 0.1
tau_exp = 1.5
tau_trap = 5

rand_sample = np.random.uniform(size=number)
emissions_exp = -tau_exp*np.log(rand_sample)

trapped = emissions_exp[emissions_exp>tau_trap]

n_traped = len(trapped)

rand_sample_2 = np.random.uniform(size=n_traped)
emissions_pow = xmin*rand_sample_2**(-1/(alfa-1))

emissions_core = emissions_pow[emissions_pow<border]
emissions_tail = emissions_pow[emissions_pow>border]

emissions_pl = xmin*emissions_core**(-1/(alfa-1))

emissions = np.concatenate([emissions_exp,
                            emissions_pl])


print("Border of core part is: " + str(border/1000) + " µs\n") 

print("Number of points in core part: " + str(len(emissions_core)) 
      + " (" + str(len(emissions_core)*100/number) + "%)")
print("Number of points in tail part: " + str(len(emissions_tail))
      + " (" + str(len(emissions_tail)*100/number) + "%)")

np.savetxt('data\emissions.csv', emissions, delimiter = ',')
