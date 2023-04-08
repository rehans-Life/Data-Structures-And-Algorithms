from typing import List

# Time Complexity: O(2^n)

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        def helper(i):
            
            # When we actually do rob the house then the only option we have is to rob it cause
            # we want to maximize our money that we stole cause there no reason to not rob it cause
            # there are no other adjacent houses to it
            if i == 0:
                return nums[i]

            # When we at house 1 and we do actually rob it we move to -1 which does not exist so
            # we return -1 from there
            if i < 0:
                return 0    
            
            # Then as per the recurrence relation what we could is either rob this house
            # not rob this house

            # If we do rob this house then we can include its money in our sum and not rob its
            # adjacent house anymore so we directly move to the house which is the nieghbour
            # of its adajcent house and get maximum money we can steal from that house till the 
            # 0th house

            pick = nums[i] + helper(i-2)

            notPick = 0 + helper(i-1)

            return max(pick,notPick) 

        return helper(n-1)


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        # A dp array to store the solutions to all of our sub problems
        dp = [-1] * n

        def helper(i):
            
            # When we actually do rob the house then the only option we have is to rob it cause
            # we want to maximize our money that we stole cause there no reason to not rob it cause
            # there are no other adjacent houses to it
            if i == 0:
                return nums[i]

            # When we at house 1 and we do actually rob it we move to -1 which does not exist so
            # we return -1 from there
            if i < 0:
                return 0

            # Before solving this subproblem we first check if we have already solved it or not 
            # by checking if we already have its solution in our dp array
            if dp[i] != -1:
                return dp[i]    
            
            # Then as per the recurrence relation what we could is either rob this house
            # not rob this house

            # If we do rob this house then we can include its money in our sum and not rob its
            # adjacent house anymore so we directly move to the house which is the nieghbour
            # of its adajcent house and get maximum money we can steal from that house till the 
            # 0th house

            pick = nums[i] + helper(i-2)

            notPick = 0 + helper(i-1)

            # Now Since we have solved this subproblem we will first store its solution in our
            # dp array and then return it so we can re use this solution to avoid computation
            # for the same subproblem again.

            dp[i] = max(pick,notPick) 

            return dp[i]

        return helper(n-1)

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1] * n

        # We starting from base and going till the n-1th house cause in tabulation we start from 
        # base case and go up until n
        dp[0] = nums[0]


        for i in range(1,n):
        
            if i != 1:
                pick = nums[i] + dp[i-2]
            else:
                pick = nums[i]

            notPick = 0 + dp[i-1]

            dp[i] = max(notPick,pick)

        return dp[n-1] 

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        prev2 = 0
        prev = nums[0]


        for i in range(1,n):
    
            pick = nums[i] + prev2

            notPick = 0 + prev

            curr = max(notPick,pick)

            prev2 = prev
            prev = curr

        return prev
        