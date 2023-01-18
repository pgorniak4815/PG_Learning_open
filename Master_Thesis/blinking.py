"""
Generator of data describing the blinking phenomenon of colloidal quantum dots.
"""

import numpy as np
import matplotlib.pyplot as plt
import math

times = np.array([])
excited_tab = np.array([])

duration = 0
expected_duration = 1*10**9
excited = True

#alfa coeficient
alfa = 1.6
#resolution of experiment
xmin = 0.1
#mean time to relaxation
tau_exp = 15
#mean time to excitation
tau_boost = 15
#mean time to getting trapped
tau_trap = 100


while duration < expected_duration:
    
    if excited == True:
        rand_sample_exp = np.random.uniform()
        rand_sample_trap = np.random.uniform()
        
        emission_exp = -tau_exp*np.log(rand_sample_exp)
        emission_trap = -tau_trap*np.log(rand_sample_trap)
        
        if emission_trap < emission_exp:
            rand_sample_pl = np.random.uniform()
            emission_pow = xmin*rand_sample_pl**(-1/(alfa-1))
            
            rand_sample_exp2 = np.random.uniform()
            rand_sample_trap2 = np.random.uniform()

            emission_exp2 = -tau_exp*np.log(rand_sample_exp2)
            emission_trap2 = -tau_trap*np.log(rand_sample_trap2)
            
            if emission_trap2 < emission_exp2:
                rand_sample_pl2 = np.random.uniform()
                emission_pow2 = xmin*rand_sample_pl**(-1/(alfa-1))
              
                rand_sample_exp3 = np.random.uniform()
                emission_exp3 = -tau_exp*np.log(rand_sample_exp3)
                
                time = emission_trap + emission_pow + emission_trap2 + emission_pow2 + emission_exp3
                
                times = np.concatenate((times, [time]))
                excited_tab = np.concatenate((excited_tab, [True]))
            
            else:
                time = emission_trap + emission_pow + emission_exp2
                
                times = np.concatenate((times, [time]))
                excited_tab = np.concatenate((excited_tab, [True]))
        
        else:
            time = emission_exp
                
            times = np.concatenate((times, [time]))
            excited_tab = np.concatenate((excited_tab, [True]))
        
        excited = False
    
    else:
        rand_sample_exp_boost = np.random.uniform()
        emission_exp_boost = -tau_boost*np.log(rand_sample_exp_boost)
        
        time = emission_exp_boost
        
        times = np.concatenate((times, [time]))
        excited_tab = np.concatenate((excited_tab, [False]))
        
        excited = True
        
    duration = np.sum(times)
    print(duration*100/expected_duration)

np.savetxt('blinking_time.csv', times, delimiter = ',')
    
