class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        # This is going to store maximum profits up until each price by making two transactions till that point. The maximum profit we can
        # generate will be determined by the maximum profit we got by buying up until that point and also the maximum profit we got by
        # selling up until that point.
        profits = [0] * n

        # We run a while loop that is going to maximize of our second transaction. And since i know my second transaction will always be
        # on the right of the first transaction hence i start finding the maximum profit i can generate up until each point by checking
        # from the right. Through this i will also be able to get the maximum point i can generate by buyinh up to that point.
        s = n - 1
        b = n - 2
        while b >= 0:
            # Calculating the profit that we are generating at each point
            profit = prices[s] -  prices[b]
            # Im going to store the maximum profit up until that point.
            profits[b] = max(profit,profits[b+1])
            if profit < 0:
                # If I'm getting a loss then why should i sell at this point if i can sell for higher at my current buying point
                s = b
            b-=1
        
        # Now im going to maximize my first transaction with respect to my second transaction and im going to be calculating the 
        # maximum profit up until each point that im getting by selling upto that point. then im going to be adding that profit
        # to the maximum profit i was able to by buying stocks upto that point because thats where the second trasnaction was initiated
        # hence i need to calculate the total profit to get maximum profit generated by two transactions upto that point.
        b = 0
        s = 1

        while s < 0:
            # Calculating the profit that we generating by selling at that point
            profit = prices[s] - prices[b]

            # Checking if the im getting the maximum profit upto that point by adding the maximum profit by selling at this point
            # and the maximum profit i got by buying at this point and if this is not the maximum that we were able to generate by
            # buying and selling upto this point then we set it to the previous max.
            profits[s] = max(profits[s-1],(profit+profits[s]))

            if profit < 0:
                # If im getting a loss then why should i buy at this point if i can buy at cheap from my current selling point
                b = s
            s+=1
        
        return profits[n-1]