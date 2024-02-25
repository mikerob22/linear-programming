# Interval scheduling problem where depth equals 1

# Input –  An input of n intervals  {s(i), … , f(i)−1} for 1 ≤ i ≤ n where i represents the
# intervals, s(i) represents the start time, and f(i) represents the finish time.
#
# Output –  A schedule S of n intervals where no two intervals in S conflict, and the total
# number of intervals in S is maximized.


# Suppose we have a list of events, Each event is in the format [a,b], where a is the starting time
# and b Is the ending time. A person can only be at one of these events at a time, and they can
# immediately go from one event to another. If two events have coinciding stop and start times,
# respectively. Find the greatest number of events that a person can attend.


intervals = [(4, 5), (0, 2), (2, 7), (1, 3), (0, 4)]

# sorting the intervals
x = intervals.sort(key=lambda x: x[1])

print(intervals)
# counting the events
count = 0
# keeping track of ending of intervals
end = 0
# list of the intervals in which person will attend the events
answer = []

# traversing the list of intervals
for interval in intervals:
    # starting time of next interval will >= ending
    # time of previous interval
    if (end <= interval[0]):
        # update the and
        end = interval[1]
        # increment the count by one
        count += 1
        # insert the non-conflict interval in the list
        answer.append(interval)

    # print statements will print non-conflict
# intervals count as well intervals
print("The maximum events a person can attend is : ", count)
print("List of intervals in which person will attend events : ", answer)





