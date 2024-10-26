import stdio
import sys

# read all input from standard input and split it into a list of words
input_strings = sys.stdin.read().split()

# reverse the list using slicing
input_strings = input_strings[::-1]

# print the reversed list with spaces between the words
for i in range(len(input_strings)):
    if i < len(input_strings) - 1:
        stdio.write(input_strings[i] + ' ')
    else:
        stdio.writeln(input_strings[i])

...


