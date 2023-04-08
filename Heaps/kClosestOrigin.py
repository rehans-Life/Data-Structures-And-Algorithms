from typing import *
from heapq import *
from math import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # A max heap which is going to store atmost points in it and is going to maintain its
        # heap order property on the basis of the distance of the point from the origin which is
        # equivalent to root of x^2 + y^2

        heap = []
        heapify(heap)

        # Traversing and inserting the points into the heap along with there distances from the 
        # origing
        for point in points:
            x,y = point
            heappush(heap,[-1 * sqrt(x**2 + y**2),point]) 

            # When size its k+1 then top nodes distance from origin is greater than k elements
            # hence it cannot be the answer so we pop it out
            if len(heap) == k+1: heappop(heap)
        
        ans = []

        while len(heap): ans.append(heappop(heap)[1])

        return ans