# -*- coding: utf-8 -*-
"""
Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals
List containing overlapping intervals:

[
   [1,4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

Examples:
sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ); // => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ); // => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ); // => 19
"""
def sum_of_intervals(intervals):
    #sorting the list on first elements
    dist = sorted(intervals,key= lambda ele: ele[0])
    interval=0
    while len(dist) != 1:
        i=-1
        j=0
        while i < len(dist):
            i+=1
            if i>=len(dist)-1:
                break
            #check if last element of current list is greater than first element of next list
            if dist[i][-1] >= dist[i+1][0]:
                #replace second item of current element with max of second item from current and next element of the list dist
                dist[i]=[(dist[i][0]),max(dist[i+1][-1],dist[i][-1])]
                #pop out the next element
                dist.pop(i+1)
                j+=1
        #repeat until no more elements can be merged        
        if j == 0:
            break
        
    for i in range(0,len(dist)):
        interval += (dist[i][1]-dist[i][0])
    return interval