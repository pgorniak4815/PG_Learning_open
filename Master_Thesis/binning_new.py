def binning(x, size = 10):
    import numpy as np
    from scipy.stats import binned_statistic
    x_data = np.arange(0, len(df))
    y_data = df['Cupcake']
    x_bins,bin_edges, misc = binned_statistic(y_data,x_data, statistic="median", bins=2)
    
    bins = np.linspace(x.min(), x.max(), size)


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
