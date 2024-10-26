import stdarray
import stdio
import stdrandom
import sys

# set the number of days in a year
DAYS_PER_YEAR = 365

# accept trials as command-line argument
trials = int(sys.argv[1])

# set total_count to 0
total_count = 0

# repeat for the number of trials
for t in range(trials):
    # create an array and initialized to False
    birthdays_seen = stdarray.create1D(DAYS_PER_YEAR, False)

    # set count to 0
    count = 0

    # start an infinite loop
    while True:
        # increment count
        count += 1

        # generate a random birthday as an integer from 0 to DAYS_PER_YEAR - 1
        birthday = stdrandom.uniformInt(0, DAYS_PER_YEAR)

        # check if the birthday has been seen before
        if birthdays_seen[birthday]:
            break
        else:
            # mark this birthday as seen
            birthdays_seen[birthday] = True

    # add the count of this trial to the total count
    total_count += count

# calculate the average number until a match
average_count = total_count // trials

# print the average count
stdio.writeln(average_count)


...
