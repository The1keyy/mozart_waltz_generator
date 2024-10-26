import stdarray
import stdio
import sys

# accept m and n as command-line arguments
m = int(sys.argv[1])  # number of rows
n = int(sys.argv[2])  # number of columns

# create an m × n matrix initialized with None
a = stdarray.create2D(m, n, None)

# read the elements of the matrix from standard input
for i in range(m):
    for j in range(n):
        # set a[i][j] to a float read from standard input
        a[i][j] = stdio.readFloat()

# create an n × m matrix for the transpose
c = stdarray.create2D(n, m, None)

# calculate the transpose of the matrix
for i in range(n):
    for j in range(m):
        # set c[i][j] to a[j][i]
        c[i][j] = a[j][i]

# print the transposed matrix
for i in range(n):
    for j in range(m):
        # if j is not the last element in the row, print with a space
        if j < m - 1:
            stdio.write(str(c[i][j]) + ' ')
        else:
            # print the last element with a newline
            stdio.writeln(c[i][j])

...
