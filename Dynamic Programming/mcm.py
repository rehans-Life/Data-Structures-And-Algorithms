from os import *
from sys import *
from collections import *
from math import *

def matrixMultiplication(arr, n):
	dp = [[-1 for _ in range(n)] for i in range(n)]

	for i in range(1,n): dp[i][i] = 0
	
	for i in reversed(range(1,n)):
		for j in range(i+1,n):
			minOperations = inf

			for k in range(i,j):
				operations = dp[i][k] + dp[k+1][j] + (arr[i-1] * arr[j] * arr[k])
				minOperations = min(minOperations,operations)

			dp[i][j] = minOperations
	
	return dp[1][n-1]