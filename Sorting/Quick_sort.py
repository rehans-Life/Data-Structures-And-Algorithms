from typing import List

class Solution:
    def partition(self,arr,start,end):

        # We need to find the sorted position of this given element
        pivot = arr[start]

        # The i pointer traverses through the left side and searches for elements which are greater than the pivot
        i = start

        # The j pointer traverses through the right side and searches for the elements which are less than the
        # pivot
        j = end

        # We continue our loop until i pointer exceeds j pointer
        while i < j:
            # We keep incrementing our ith pointer until we find an element greater than our pivot
            while i <= end and arr[i] <= pivot:
                i+=1
            
            # We keep decrememt our jth pointer until we find an element smaller than or equal to our pivot
            while j >= start and arr[j] > pivot:
                j-=1
            
            # After we find such element then swap them cause both of them are not there in there correct 
            # positions
            if i < j:
                arr[i],arr[j] = arr[j],arr[i]
        
        # When the loop ends then the jth pointer is pointing at the sorted position of our pivot 
        # which is in the start of the array so we swap j and start index values
        arr[start],arr[j] = arr[j],arr[start]

        # Then we return the sorted position of our pivot to divide the array
        return j

    def quickSort(self,arr,start,end):
        if start < end:
            pivot = self.partition(arr,start,end)
            # Then we divide the array and perform quicksort on both the parts
            self.quickSort(arr,start,pivot-1)
            self.quickSort(arr,pivot+1,end)            

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.quickSort(nums,0,n-1)
        return nums