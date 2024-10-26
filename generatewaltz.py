import stdarray
import stdrandom
import stdio

# create a 2D list for minuet measures with dimensions 11 x 16
minuetMeasures = stdarray.create2D(11, 16)

#  values read from standard input
for i in range(11):
    for j in range(16):
        minuetMeasures[i][j] = stdio.readInt()

# create a 2D list for trio measures with dimensions 6 x 16
trioMeasures = stdarray.create2D(6, 16)

#  values read from standard input
for i in range(6):
    for j in range(16):
        trioMeasures[i][j] = stdio.readInt()

# generate and print minuet measures
for j in range(16):
    # roll dices and sum the results
    die1 = stdrandom.uniformInt(1, 7)
    die2 = stdrandom.uniformInt(1, 7)

    # sum of the two die rolls
    i = die1 + die2
    # print the measure
    stdio.write(str(minuetMeasures[i - 2][j]))
    stdio.write(" ")

# generate and print trio measures
for j in range(16):
    i = stdrandom.uniformInt(1, 7)
    # output the corresponding trio measure
    stdio.write(str(trioMeasures[i - 1][j]))
    stdio.write(" ")

# print a newline at the end
stdio.writeln()

...
