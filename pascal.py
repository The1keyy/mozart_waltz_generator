import stdarray
import stdio
import sys

# accept n as a command line argument
n = int(sys.argv[1])

# create a list a of size n + 1
a = stdarray.create1D(n + 1, None)

# initialize each row of Pascal's triangle
for i in range(n + 1):
    a[i] = stdarray.create1D(i + 1, 1)

# calculate the values for Pascal's triangle
for i in range(2, n + 1):
    for j in range(1, i):
        a[i][j] = a[i - 1][j - 1] + a[i - 1][j]

# print Pascal's triangle
for i in range(n + 1):
    for j in range(i + 1):
        # if j is not the last element in the row, print with a space
        if j < i:
            stdio.write(str(a[i][j]) + ' ')
        else:
            # print the last element with a newline
            stdio.writeln(a[i][j])

...
