import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import optimize as opt

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

def binning2(x, size = 0.1):   
    number_of_bins = math.ceil(max(x)/size) + 1

    bins = np.linspace(0, size*number_of_bins, number_of_bins+1)

    binned = np.histogram(x, bins)    
    
    return (binned[1][:-1], binned[0])

border = 100000
x_test = 0.1
alfa_test = 1.25

rand_sample_test = np.random.uniform(size=100000)
pow_test = x_test*rand_sample_test**(-1/(alfa_test-1))

pow_test = pow_test[pow_test<=border]

binned_test = binning2(pow_test, 0.1)

binned_test_na = np.array(binned_test)

fun_test = Likehood(binned_test_na, 1.01)
result = opt.minimize(fun_test, 1.00001, method = 'SLSQP')

print(result)

(x_test, y_test) = binned_test

plt.scatter(x_test, y_test, c = 'orange')
plt.xscale('log')
plt.yscale('log')
plt.ylabel('Int.')
plt.xlabel('t')
plt.show()

x_n = 100
x_t = np.linspace(int(binned_test[0][0]), (x_n + int(binned_test[0][0]))*10, x_n)

a = np.zeros(len(x_t))

for i,item in np.ndenumerate(x_t):
    
    fun = Likehood(binned_test_na, item)
    
    a[i] = opt.minimize(fun, 1.00001, method='Nelder-Mead').x

a_x = np.array([x_t, a])

plt.scatter(a_x[0], a_x[1], c = 'blue')
plt.xscale('log')
#plt.yscale('log')
plt.ylabel('alfa')
plt.xlabel('xmin')
plt.show()

np.savetxt('data\estimation_x.csv', a_x[0], delimiter = ',')
np.savetxt('data\estimation_alfa.csv', a_x[1], delimiter = ',')

