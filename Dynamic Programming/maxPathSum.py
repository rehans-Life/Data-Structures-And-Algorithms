from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

# Space Optimisation

# Time Complexity: O(n*m)
# Space Complexity: O(m)

def getMaxPathSum(matrix):

    n = len(matrix)
    m = len(matrix[0])

    front = matrix[n-1].copy()

    for i in reversed(range(n-1)):        
        temp = [0] * m

        for j in range(m):

            d,dr,dl = -inf,-inf,-inf

            d = matrix[i][j] + front[j]
            if j > 0:
                dl = matrix[i][j] + front[j-1]
            if j < m-1:
                dr = matrix[i][j] + front[j+1]

            temp[j] = max(d,dr,dl)

        front = temp
    
    return max(front)
