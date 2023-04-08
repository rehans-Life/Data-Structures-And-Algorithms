import math
from typing import List
class Solution:

    def eatingPossible(self,piles,h,speed):
        no_of_hours = 0
        for i in range(len(piles)):
            no_of_hours+=(math.ceil(piles[i] / speed))
            if no_of_hours > h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        start = 1
        end = sum(piles)
        res = -1

        while start <= end:

            mid = (start+end) // 2

            if self.eatingPossible(piles,h,mid):
                res = mid
                end = mid-1
            else:
                start = mid+1
        
        return res