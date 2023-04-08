from typing import List
from heapq import heapify,heappop,heappush
import math

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Counting the frequency for each element
        freq = {}
        for num in nums: 
            if num not in freq: freq[num] = 0
            freq[num]+=1

        # Maintain a min heap which is going to store the elements on the basis
        # of there frequencies.
        heap = []
        heapify(heap)

        # Then i need to run a loop and insert each distinct element into the heap 
        # along with its frequency.
        for num,val in freq.items():
            heappush(heap,[val,num])

            # If the heap size reaches k+1 hence that means that the root element's
            # frequency is less than k elements hence thats why its on the top
            # which means it can never be in our top k elements interms of frequency
            # so i can remove it
            if len(heap) == k+1:
                heappop(heap)
        
        # Adding the values of the top k elements in terms of frequency into our answer
        ans = []
        while len(heap): ans.append(heappop(heap)[1])
        
        return ans