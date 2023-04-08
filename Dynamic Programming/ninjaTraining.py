from typing import *
from math import *
  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1 for _ in range(4)] for _ in range(n)]

    def helper(day,last):

        # If day is zero then we can easily find the maximum points we can earn
        # from the 0th day till the 0th day while not considering the task we 
        # performed on the previous day.

        # Cause this boils down finding the maximum points task  we can earn on
        # the 0th day ignoring the previous task we performed.

        if day == 0:
            maxPoints = -inf
            for i in range(3):
                if i != last:
                    maxPoints = max(maxPoints,points[0][i])
            return maxPoints

        # If we already have found the maximum points we can earn on this day
        # while ignoring the previous task we performed we just return it.    
        if dp[day][last] != -1:
            return dp[day][last]
        
        # If we havent found solution already then we compute it by checking 
        # through which task can we get the maximum points till the 0th day
        # by ignoring the last task we performed.
        maxPoints = -inf

        for i in range(3):
            if i != last:
                pointsTill0 = points[day][i] + helper(day-1,i)
                maxPoints = max(maxPoints,pointsTill0)

        dp[day][last] = maxPoints
        return dp[day][last]

    return helper(n-1,3)

from typing import *
from math import *
  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp = [[-1 for _ in range(4)] for _ in range(n)]

    # For day 0 we are checking for all last tasks that could be performed
    # and we are finding the maximum points that we can get by ignoring that
    # last task and we are storing the solution in our dp array for all base 
    # cases
    for last in range(4):
        maxPoints =  0
        for task in range(3):
            if task != last:
                maxPoints = max(maxPoints,points[0][task])
        dp[0][last] = maxPoints
    
    # Then we have to go from day 1 to day n-1 and again for them as well
    # consider all the last values and find the maximum points we can get
    # by ignoring the last task performed till the 0th day
    for day in range(1,n):
        for last in range(4):
            maxPoints = 0
            for task in range(3):
                if task != last:
                    pointsTill0 = points[day][task] + dp[day-1][task]
                    maxPoints = max(maxPoints,pointsTill0)
            dp[day][last] = maxPoints
    
    return dp[n-1][3]
    





