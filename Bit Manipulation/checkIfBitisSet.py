class Solution:
    def checkBit(self,n: int,i: int) -> bool:
        return (n>>i)&1==1

solution = Solution()
print(solution.checkBit(13,1))

        