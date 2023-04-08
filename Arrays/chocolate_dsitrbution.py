#User function Template for python3
import math
class Solution:

    def findMinDiff(self, A,N,M):
        # Sorting the array to be able to generate all possible alternatives
        # that i can distribute the chocolates.
        A.sort()
        
        # Then we need two pointers to be able to create windows of size m
        # within the sorted array cause m is the amount of chocolates that 
        # we need to distribute among the students.
        s = 0
        e = M-1
        
        minDiff = math.inf
        
        # Iterating until ive tested out all possible alternatives in the question.
        while e < N:
           # Finding the diff b/w minimum and maximum number of chocolates for each
           # alterantive and checking which one produces the minimum result 
           minDiff = min(minDiff,A[e]-A[s])
           # Incrementing the pointers to create a new window which is to be 
           # tested out.
           s+=1
           e+=1
        
        return minDiff