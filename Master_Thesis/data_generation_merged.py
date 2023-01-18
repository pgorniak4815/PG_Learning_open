import numpy as np

number = 100000000
border = 10000

alfa = 1.3
xmin = 0.1
tau_exp = 15
tau_trap = 100

rand_sample_exp = np.random.uniform(size=number)
rand_sample_trap = np.random.uniform(size=number)

emissions_exp = -tau_exp*np.log(rand_sample_exp)
emissions_trap = -tau_trap*np.log(rand_sample_trap)

trapped = emissions_trap[emissions_trap<emissions_exp]
emissions_exp = emissions_exp[emissions_exp<=emissions_trap]

n_traped = len(trapped)

rand_sample_pl = np.random.uniform(size=n_traped)
emissions_pow = xmin*rand_sample_pl**(-1/(alfa-1))

n_pow = len(emissions_pow)

rand_sample_exp2 = np.random.uniform(size=n_pow)
rand_sample_trap2 = np.random.uniform(size=n_pow)

emissions_exp2 = -tau_exp*np.log(rand_sample_exp2)
emissions_trap2 = -tau_trap*np.log(rand_sample_trap2)

trapped_exp2 = trapped[emissions_exp2<=emissions_trap2]
trapped_exp3 = trapped[emissions_exp2>emissions_trap2]
emissions_pow_exp2 = emissions_pow[emissions_exp2<=emissions_trap2]
emissions_pow_exp3 = emissions_pow[emissions_exp2>emissions_trap2]

trapped2 = emissions_trap2[emissions_trap2<emissions_exp2]
emissions_exp2= emissions_exp2[emissions_exp2<=emissions_trap2]

emissions_exp_t1 = emissions_exp2 + trapped_exp2 + emissions_pow_exp2 

n_traped2 = len(trapped2)

rand_sample_pl2 = np.random.uniform(size=n_traped2)
emissions_pow2 = xmin*rand_sample_pl2**(-1/(alfa-1))

n_pow2 = len(emissions_pow2)

rand_sample_exp3 = np.random.uniform(size=n_pow2)
emissions_exp3 = -tau_exp*np.log(rand_sample_exp3)

emissions_exp_t2 = trapped_exp3 + emissions_pow_exp3 + trapped2 + emissions_pow2 + emissions_exp3

emissions = np.concatenate([emissions_exp, emissions_exp_t, emissions_exp_t2])

emissions_core = emissions[emissions<=border]
emissions_tail = emissions[emissions>border]

emissions = emissions_core

print("Border of core part is: " + str(border/1000) + " µs\n") 

print("Number of points in core part: " + str(len(emissions_core)) 
      + " (" + str(len(emissions_core)*100/number) + "%)")
print("Number of points in tail part: " + str(len(emissions_tail))
      + " (" + str(len(emissions_tail)*100/number) + "%)")

print("Number of once trapped emissions: " + str(len(emissions_exp_t1)) 
      + " (" + str(len(emissions_exp_t1)*100/number) + "%)")
print("Number of twice trapped emissions: " + str(len(emissions_exp_t2))
      + " (" + str(len(emissions_exp_t2)*100/number) + "%)")

np.savetxt('data\emissions.csv', emissions, delimiter = ',')
np.savetxt('data\emissions_times_exp.csv', emissions_exp, delimiter = ',')
np.savetxt('data\emissions_times_power_law_core.csv', emissions_core, delimiter = ',')
np.savetxt('data\emissions_times_power_law_tail.csv', emissions_tail, delimiter = ',')



