# Job sequence
# Function to schedule the jobs
def printjobschedule(array, t):
    m = len(array)
    # Sort all jobs accordingly
    for j in range(m):
        for q in range(m - 1 - j):
            if array[q][2] < array[q + 1][2]:
                array[q], array[q + 1] = array[q + 1], array[q]
    res = [False] * t
    # To store result
    job = ['-1'] * t
    for q in range(len(array)):
        # Find a free slot
        for q in range(min(t - 1, array[q][1] - 1), -1, -1):
            if res[q] is False:
                res[q] = True
                job[q] = array[q][0]
                break
    # print
    print(job)
# Driver
array = [['a', 7, 202],
       ['b', 5, 29],
       ['c', 6, 84],
       ['d', 1, 75],
       ['e', 2, 43]]
print("Maximum profit sequence of jobs is- ")
printjobschedule(array, 3)



'''1) Jobs are to be sorted in a decreased order of profit.

2) Repetition is done on jobs as per the decrease in profit value.

For each job:

a) A time slot is selected, such that the slot is empty.
It also has to be lesser than the given deadline.
Now the job is placed in that slot.
Then it is marked as a filled slot.

b)The job is ignored if no such time is found to exists.'''
