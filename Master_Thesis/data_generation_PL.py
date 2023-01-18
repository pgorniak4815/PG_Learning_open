import numpy as np

number = 1000000

alfa = 1.5
xmin = 0.1

rand_sample =np.random.uniform(size=number)

emissions = rand_sample**(-1/(alfa-1))*xmin

emissions.sort()

border = 10000

emissions_core = emissions[emissions<border]
emissions_tail = emissions[emissions>border]

print("Border of core part is: " + str(border/1000) + " µs\n") 

print("Number of points in core part: " + str(len(emissions_core)) 
      + " (" + str(len(emissions_core)*100/number) + "%)")
print("Number of points in tail part: " + str(len(emissions_tail))
      + " (" + str(len(emissions_tail)*100/number) + "%)")

np.savetxt('data\emissions_times_power_law_core.csv', emissions_core, delimiter = ',')
np.savetxt('data\emissions_times_power_law_tail.csv', emissions_tail, delimiter = ',')




