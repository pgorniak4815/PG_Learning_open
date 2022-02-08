import numpy as np
import matplotlib.pyplot as plt
from math import exp
import random
import time

random.seed(time.get_clock_info)
number = 1000000;
emissions = np.array([]);

time_of_integration = 10000;

for i in range(number):
    for s in range(time_of_integration):
        chance = random.randrange(0,11)
        if chance == 1:
            emissions = np.append(emissions, s)
            break;

print(emissions)

q25, q75 = np.percentile(emissions, [25, 75])
bin_width = 2 * (q75 - q25) * len(emissions) ** (-1/3)
bins = round((emissions.max() - emissions.min()) / bin_width)

plt.hist(emissions, density=True, bins=bins)
mn, mx = plt.xlim()
plt.xlim(mn, mx)
kde_xs = np.linspace(mn, mx, 100)

plt.legend(loc="upper left")
plt.ylabel("Int.")
plt.xlabel("Time")

plt.show()
