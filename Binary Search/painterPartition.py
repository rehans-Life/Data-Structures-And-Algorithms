#User function Template for python3

class Solution:
    
    def allocationPossible(self,boards,k,mid):
        
        no_of_painters = 1
        currUnits = 0
        
        for board in boards:
            if currUnits + board > mid:
                no_of_painters+=1
                currUnits = board
                if no_of_painters > k:
                    return False
            else:
                currUnits+=board
        
        return True
            
    
    def minTime (self, arr, n, k):
        #code here
        start = max(arr)
        end = sum(arr)
        
        res = -1
        
        while start <= end:
            
            mid = (start+end) // 2
            
            if self.allocationPossible(arr,k,mid):
                res = mid 
                end = mid-1
            else:
                start = mid+1
                
        return res
