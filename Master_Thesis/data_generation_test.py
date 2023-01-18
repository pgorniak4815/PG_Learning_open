import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import optimize as opt

number = 100000000
border = 100000

alfa = 1.8
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


emissions = np.concatenate([emissions_exp, emissions_exp_t1, emissions_exp_t2])



#tail cutting
emissions_core = emissions[emissions<=border]
emissions_tail = emissions[emissions>border]

emissions_core_t1 = emissions_exp_t1[emissions_exp_t1<=border]
emissions_core_t2 = emissions_exp_t2[emissions_exp_t2<=border]

len(emissions_core_t2)

#printing results
print("Border of core part is: " + str(border/1000) + " µs\n") 

print("Number of points in core part: " + str(len(emissions_core)) 
      + " (" + str(len(emissions_core)*100/number) + "%)")
print("Number of points in tail part: " + str(len(emissions_tail))
      + " (" + str(len(emissions_tail)*100/number) + "%)")

print("Number of once trapped emissions: " + str(len(emissions_exp_t1)) 
      + " (" + str(len(emissions_exp_t1)*100/number) + "%)")
print("Number of twice trapped emissions: " + str(len(emissions_exp_t2))
      + " (" + str(len(emissions_exp_t2)*100/number) + "%)")




def binning2(x, size = 0.1):   
    number_of_bins = math.ceil(max(x)/size) + 1

    bins = np.linspace(0, size*number_of_bins, number_of_bins+1)

    binned = np.histogram(x, bins)    
    
    return (binned[1][:-1], binned[0])


binned_core_emissions = binning2(emissions_core, 0.1)
(x_c, y_c) = binned_core_emissions

binned_exp_emissions = binning2(emissions_exp, 0.1)
(x_exp, y_exp) = binned_exp_emissions

binned_t1_emissions = binning2(emissions_core_t1, 0.1)
(x_t1, y_t1) = binned_t1_emissions

binned_t2_emissions = binning2(emissions_core_t2, 0.1)
(x_t2, y_t2) = binned_t2_emissions




plt.plot(x_c, y_c, 'green', alpha = 0.7)
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Int. [counts]')
plt.xlabel('time [ns]')

plt.plot(x_exp, y_exp, 'black', alpha = 1)
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Int. [counts]')
plt.xlabel('time [ns]')

plt.plot(x_t1, y_t1, 'orange', alpha = 0.8)
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Int. [counts]')
plt.xlabel('time [ns]')

plt.plot(x_t2, y_t2, 'yellow', alpha = 0.8)
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Int. [counts]')
plt.xlabel('time [ns]')

plt.title('Photoluminescemce decay')
plt.legend(['full', 'basic', 'once trapped', 'twice trapped'])
plt.show()


binned_core_na = np.array(binned_core_emissions)

to_check = binned_core_na

plt.plot(to_check[0], to_check[1], 'green')
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Int. [counts]')
plt.xlabel('time [ns]')

plt.show()

to_check[np.where(to_check == 0)] = 0.000001

(binned_exp_emissions_x, binned_exp_emissions_y) = binned_exp_emissions

np.savetxt('data\emissions_core_x.csv', x_c, delimiter = ',')
np.savetxt('data\emissions_core_y.csv', y_c, delimiter = ',')

np.savetxt('data\emissions_exp_x.csv', binned_exp_emissions_x, delimiter = ',')
np.savetxt('data\emissions_exp_y.csv', binned_exp_emissions_y, delimiter = ',')

np.savetxt('data\emissions_t1_x.csv', x_t1)
np.savetxt('data\emissions_t1_y.csv', y_t1)

np.savetxt('data\emissions_t2_x.csv', x_t2, delimiter = ',')
np.savetxt('data\emissions_t2_y.csv', y_t2, delimiter = ',')

hist = binned_core_na

x_n = 100
x_test = np.linspace(int(to_check[0][0]), (x_n + int(to_check[0][0]))*10, x_n)

a = np.zeros(len(x_test))

def Likehood(hist, bmin):
    
    def ES(*arg):
        
        l_tab = np.array([])    
        
        for alfa in np.nditer(arg):
            hist_work = hist.transpose()
    
            hist_work = hist_work[hist_work[:,0]>=bmin]
    
            n = hist_work[:, 1].sum()
        
            bi = hist_work[:, 0]
        
            bi_1 = np.concatenate((np.delete(hist_work[:, 0], [0]), [hist_work[-1,0]+ 0.1]))
        
            bi_pow = np.power(bi, (1 - alfa))
        
            bi_1_pow = np.power(bi_1, (1 - alfa))
        
            calculated = hist_work[:, 1]*np.log(bi_pow - bi_1_pow)
        
            l = n * (alfa - 1) * np.log(bmin) + calculated.sum()
            
            l_tab = np.concatenate((l_tab, [l]))          
            
        return -l_tab
    
    return ES




for i,item in np.ndenumerate(x_test):
    
    fun = Likehood(hist, item)
    
    a[i] = opt.minimize(fun, 1.00001, method='Nelder-Mead').x

a_x = np.array([x_test, a])

plt.scatter(a_x[0], a_x[1], c = 'blue')
plt.xscale('log')
#plt.yscale('log')
plt.ylabel('alfa')
plt.xlabel('xmin')
plt.show()

np.savetxt('data\estimation_x.csv', a_x[0], delimiter = ',')
np.savetxt('data\estimation_alfa.csv', a_x[1], delimiter = ',')













