import stdio
import sys
import stdaudio

# read all integers from standard input into a list
measures = stdio.readAllInts()

# check if the number of measures is exactly 32
if len(measures) != 32:
    print("A waltz must contain exactly 32 measures")
    sys.exit()

# check if the first 16 measures are within the range [1, 176]
for v in measures[0:16]:
    if v < 1 or v > 176:
        print("A minuet measure must be from [1, 176]")
        sys.exit()

# check if the last 16 measures are within the range [1, 96]
for v in measures[16:32]:
    if v < 1 or v > 96:
        print("A trio measure must be from [1, 96]")
        sys.exit()

# play the first 16 minuet measures
for v in measures[0:16]:
    filename = "data/M" + str(v) + ".wav"
    stdaudio.playFile(filename)

# play the last 16 trio measures
for v in measures[16:32]:
    filename = "data/T" + str(v) + ".wav"
    stdaudio.playFile(filename)

...
