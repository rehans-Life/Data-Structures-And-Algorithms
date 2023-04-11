class Solution:
    def checkBit(self,n: int) -> bool:
        mask = 1
        while mask&n == 0:
            mask = mask<<1
        
        mask = ~mask
        return n&mask

solution = Solution()
print(solution.checkBit(8))

        