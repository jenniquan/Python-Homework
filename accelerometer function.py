# The accelerometer monitors acceleration in the x, y and z axes
# by reporting each value in m/s/s. 

# Write a function that, given the accleration of each axes,
# returns the resultant (square root of the sum of squares ) of all 3 values.


import math

def resultant (x, y, z):
    return math.sqrt ((math.pow (x, 2)) + (math.pow (y, 2)) + (math.pow (z, 2)))
