import math
class Solution:

    def mBouqtsPossible(self,bloomDay,m,k,days):
        no_of_bouqets = 0
        flowersAssigned = 0
        
        for flower in bloomDay:
            if flower <= days:
                flowersAssigned+=1
                if flowersAssigned == k:
                    no_of_bouqets+=1
                    flowersAssigned = 0
                    if no_of_bouqets == m:
                        return True
            else:
                flowersAssigned = 0
        
        return False

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        
        start = min(bloomDay)
        end = max(bloomDay)
        
        while start <= end:

            mid = (start+end) // 2
            
            if self.mBouqtsPossible(bloomDay,m,k,mid):
                pass
            else:
                start = mid+1
                
solution = Solution()
print(solution.minDays([1,10,3,10,2],3,1))
