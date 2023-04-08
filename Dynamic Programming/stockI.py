from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    n = len(prices)
    mini = prices[0]
    maxProfit = 0

    for i in range(1,n):
        currProfit = prices[i] - mini
        maxProfit = max(maxProfit,currProfit)
        mini = min(mini,prices[i])
    
    return maxProfit