"""
Program for the second part of the master's thesis, is used to count the intervals in which
there are frequent immissions and those in which they do not occur.
"""
import numpy as np
import matplotlib.pyplot as plt
import math

times = np.loadtxt('blinking_time.csv')

time_interval = 1*10**3
duration = times.sum()

n = int(duration/time_interval)
count = np.empty(n)

len(times)

times_c = times

sum_time = 0
j = 0

for i in range(0, n):
    
    c = 0
    while sum_time < (i+1)*time_interval:
        sum_time = sum_time + times_c[j]
        print(times_c[j])
        j = j + 1
        c = c + 1
    
    print("nastepny")
    
    delta = sum_time - (i+1)*time_interval
    
    print(delta)
    
    times_c[j] = times_c[j] - (times_c[j] - delta)
    
    sum_time = (i+1)*time_interval
    
    count[i] = int(c/2)   
    
    
time = np.linspace(0, n*time_interval, n+1)
plt.plot(time[:-1], count)

np.savetxt('ct_time.csv', time, delimiter = ',')
np.savetxt('counts_time.csv', count, delimiter = ',')

i = 0
on = []
off = []

while 1 == 1:
    
    n = 0
    while  count[i] > 25:
        n = n + 1
        i = i + 1
        
    on.append(n*time_interval)
    
    n = 0
    while  count[i] <= 25:
        n = n + 1
        i = i + 1
        
    off.append(n*time_interval)
    
    print("obieg" + str(i))
    
    if i == (len(count)-1):
        break

off_np = np.array(off)
on_np = np.array(on)

def binning2(x, size = 0.1):   
    number_of_bins = math.ceil(max(x)/size) + 1

    bins = np.linspace(0, size*number_of_bins, number_of_bins+1)

    binned = np.histogram(x, bins)    
    
    return (binned[1][:-1], binned[0])

b_off = binning2(off_np, time_interval)
b_on = binning2(on_np, time_interval)

(box, boy) = b_on
(bofx, bofy) = b_off

plt.scatter(box, boy)
plt.xscale('log')
plt.yscale('log')
plt
plt.show()

plt.scatter(bofx, bofy)
plt.xscale("log")
plt.yscale('log')
plt.show()

x_b_on = b_on[0]
y_b_on = b_on[1]

x_b_off = b_off[0]
y_b_off = b_off[1]

np.savetxt('x_on_blink_time.csv', x_b_on, delimiter = ',')
np.savetxt('y_on_blink_time.csv', y_b_on, delimiter = ',')
np.savetxt('x_off_blink_time.csv', x_b_off, delimiter = ',')
np.savetxt('y_off_blink_time.csv', y_b_off, delimiter = ',')
