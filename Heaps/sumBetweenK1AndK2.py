from heapq import *

class Solution:
    def kthSmallest(self,arr,k):
        heap = []
        heapify(heap)
        
        for num in arr:
            heappush(heap,-1*num)
            
            if len(heap) == k+1:
                heappop(heap)
        
        return -1 * heappop(heap)
        
    def sumBetweenTwoKth(self, A, N, K1, K2):
        
        # Finding the k1th and k2th smallest elements from the array
        k1thSmallest = self.kthSmallest(A,K1)
        k2thSmallest = self.kthSmallest(A,K2)
        
        # An Accumulator for sums
        sum = 0
        
        # Then running a for loop and finding the elements b/w
        # k1th smallest and k2th smallest elements within the 
        # array.
        for num in A:
            # If the number is greater k1th smallest element and less
            # than k2th smallest element within the array hence it is 
            # our answer and we can add it to our sum
            if num > k1thSmallest and num < k2thSmallest:
                sum+=num

        return sum