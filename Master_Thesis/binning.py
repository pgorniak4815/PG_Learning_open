def binning(x, size = 10):   
    number_of_bins = round((max(x)-min(x))/size) + 1

    bins = [i*size for i in range(0,number_of_bins)]
    bins_label = [i+(size)/2 for i in bins]

    values = [0]*len(bins_label)

    binned_data = dict(zip(bins_label,values))

    for item in x:
        n=0
        for lim in bins:
            if item <= lim+size:
                binned_data[bins_label[n]]+=1
                (binned_data[bins_label[n]])
                break
            n+=1

    return(binned_data)

import numpy as np

emissions = np.loadtxt('data\emissions.csv',
                 delimiter=",", dtype=float)

binned_emissions = binning(emissions,0.1)
EM = binned_emissions.items()
EM = sorted(EM) 
x, y = zip(*EM)

np.savetxt('data\emissions_binned.csv', (x,y), delimiter = ',')
