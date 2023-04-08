from typing import List
from math import inf
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2: return 0

        # An index pointer which is going to point at the start of our unsorted subarray
        i = 0

        # An index pointer which is going to point at the end of our unsorted subarray
        j = n-1        

        # Im going to be running a while loop to find the start of my unsorted subarray by incrementing 'i' up 
        # until the element whose adjacent element is less than it and that would be the start of my unsorted 
        # subarray

        while i+1 < n and nums[i] <= nums[i+1]: i+=1

        # If the array is already sorted then only would i+1 would be equals n cause if that wasnt the case
        # then this wouldnt be the case.
        if i+1 == n : return 0

        # Im going to keep decrementing j until its pointing at an element whose number behind it is greater 
        # than it and that would denote that the section is unsorted

        while j-1 >= 0 and nums[j] >= nums[j-1]: j-=1

        # Since i need to find the continous subarray which i need to sort to be able to convert the whole
        # array into a sorted array therefore im going to consider all the elements between i and j to be
        # a part of the unsorted section as well cause i cant consider uncontinous subarrays i need them to
        # be combined.

        # Now I need find the minimum and the maximum element in my current sorted section so that i able 
        # to shift my ith pointer backwards up until the elements is greater than the minimum element 
        # this is so after sorting the minimum element is in its correct position
        # Similarly i need to increment my jth element as well up until the element which is less than 
        # than the maximum element in my unsorted section so i can move it in its correct position.

        unsortedMin = inf
        unsortedMax = -inf

        for k in range(i,j+1):
            unsortedMax = max(unsortedMax,nums[k])
            unsortedMin = min(unsortedMin,nums[k])
        
        # Then i keep moving my ith element backwards until the index pointer is pointing at the last element
        # in my left section which is greater than unsortedMin number so that i can move the element in its
        # correct position in the sorted array.
        while i - 1 >= 0 and nums[i-1] > unsortedMin: i-=1

        # Same mechanism for my jth element as well i keep moving it forwards until the elements are less than 
        # the maximum element in my unsorted section so that i can move it in its correct position in the sorted
        # array.
        while j + 1 < n and nums[j+1] < unsortedMax: j+=1  


        return j-i+1