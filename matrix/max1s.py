from math import inf

class Solution:
    
    def firstOccurence(self,row):
        
        start = 0
        end = len(row) -1
        res = -1
        
        while start <= end:
            mid = (start+end) // 2
            
            if row[mid] == 1:
               res = mid
               end = mid-1
            else:
                start = mid+1
        
        return res
    
    def lastOccurence(self,row):
        start = 0
        end = len(row)-1
        res = -1
        
        while start <= end:
            
            mid = (start+end) // 2
            
            if row[mid] == 1:
                res = mid
                
            start = mid+1
        
        return res
        
    def rowWithMax1s(self,arr, n, m):
                
            ans = -1
            numberOf1sInAns = -inf

            for i in range(n):
                    
                    firstOccurenceOf1 = self.firstOccurence(arr[i])
                    
                    if firstOccurenceOf1 == -1:
                        continue
                    
                    lastOccurenceOf1 = self.lastOccurence(arr[i])

                    numberOf1sInRow = lastOccurenceOf1 - firstOccurenceOf1 + 1
                    
                    if numberOf1sInRow > 0 and numberOf1sInRow > numberOf1sInAns:
                        
                        ans = i
                        numberOf1sInAns = numberOf1sInRow
                    
            return ans    
        
solution = Solution()

matrix = [
    [0,1,1,1],
    [0,0,1,1],
    [1,1,1,1],
    [0,0,0,0]
]

n = len(matrix)
m = len(matrix[0])

print((solution.rowWithMax1s(matrix,n,m)))