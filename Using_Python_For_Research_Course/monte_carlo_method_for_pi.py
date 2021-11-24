"""
Ex. 2 Hw. 1 from "Using Python for Research" course.

The task is to determine a value of pi, by monte carlo method.
Using information difference of the areas of the circle
and the square described on it is pi/4.
"""

import random

random.seed(1)

def rand():
    """
    Return random number from -1 to 1 with uniform distribution
    """
    return random.uniform(-1,1)

def distance(x, y):
    """
    Return a distance between 2 points on the plane
    """
    return(pow((y[0]-x[0])**2 + (y[1]-x[1])**2, 1/2))

def in_circle(x, origin = [0]*2):
    """
    Return true if point is in a circle with a radius of 1 and center
    in [0,0] or false if not
    """
    if distance(x,origin)<1:
        return True
    else:
        return False

R = 1000000 #number of random points (accuracy of the result)
x = []
inside = []

for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    inside.append(in_circle(point))

pi_calculated = (sum(inside)/R)*4

print("pi = " + str(pi_calculated))