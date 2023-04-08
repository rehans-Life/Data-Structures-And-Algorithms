# Brute Force

# Time Complexity: O(n^2)
# Space Complexity: O(1)

import math
class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        
        maximumProfit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i,n):
                maximumProfit = max(maximumProfit,prices[j]-prices[i])
        
        return maximumProfit

# Optimal Approach

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        n = len(prices)

        # Its initialized with zero becuase we dont want our losses to be stored here and we can
        # have a situation like [5,4,3,2,1] where we get nothing but losses no matter what day we 
        # or sell at and in those i need to return 0 then.
        maximumProfit = 0

        # Buy Pointer is placed initially at day 1 
        b = 0

        # And then sell pointer should obviously be placed infront of it and we can 
        # keep its initial spot at Day 2
        s = 1

        # Going to run a while loop until we have ran out of days to sell at.
        while s < n:
            # Calculating the profit or loss between our buying and selling day
            diff = prices[s] - prices[b]

            # Checking if we got profit or loss by selling at our current points
            if diff > 0:
                # If we get profit then im checking if it is the maximum profit that i've 
                # generated so far.
                maximumProfit = max(maximumProfit,diff)
            else:
                # If we are getting a loss by buying at our current day why dont we buy
                # at the day where we know the price is less than the current price that 
                # we paid for that stock so were switching our buying point to our current
                # selling point cause we know the price is less there than our current point.
                # and it can generate higher profits for us than our current point.
                b = s

            # Incrementing my selling pointer to another day
            s+=1
            
        return maximumProfit