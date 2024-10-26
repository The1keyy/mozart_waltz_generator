import math
import stdio
import sys

# get the value of n from the command line
n = int(sys.argv[1])

# create empty lists for x and y
x = []
y = []

# read n floats into list x
for i in range(n):
    # read a float and append to x
    x.append(stdio.readFloat())

# read n floats into list y
for i in range(n):
    # read a float and append to y
    y.append(stdio.readFloat())

# set initial distance to 0.0
distance = 0.0

# calculate the sum of squared differences between corresponding elements of x and y
for i in range(n):
    distance += (x[i] - y[i]) ** 2

# take the square root of the sum to get the Euclidean distance
distance = math.sqrt(distance)

# print the result
stdio.writeln(distance)

...
