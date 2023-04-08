def getMaximumProfit(values, n):

    nextBuy,nextSell = 0,0
    
    for i in reversed(range(n)):
        # Max profit that i can get by buying or not buying the stock on this
        # day
        currBuy = max(-values[i] + nextSell, 0 + nextBuy)
        # Max Profit that i can get by selling or not selling the stock on this
        # day
        currSell = max(+values[i] + nextBuy, 0 + nextSell)

        nextBuy, nextSell = currBuy, currSell

    # The max profit that i can get from the 1st day to the last day if i am
    # suppose to buy on the first day.
    return nextBuy