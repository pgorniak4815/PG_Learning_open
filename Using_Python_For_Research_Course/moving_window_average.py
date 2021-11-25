"""
Ex. 3 Hw. 1 from "Using Python for Research" course.

The task is to build a function to smooth the values in the list
Replace each value with the average of each value's neighbors,
including the value itself.
"""

import random

random.seed(1)


def moving_window_average(x, n_neighbors=1):
    """
    Calculate moving window average for given dataset (x)
    and number of neighbors (n_neighbors).
    """
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    return [sum(x[i: (i+width)]) / width for i in range(n)]

# test
x = [0, 10, 5, 3, 1, 5]
print(moving_window_average(x, 4))
