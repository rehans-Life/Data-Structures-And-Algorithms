from os import *
from sys import *
from collections import *
from math import *

def evaluateExp(exp):

	n = len(exp)
	dp = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]
	
	def helper(i,j,isTrue):

		if i == j:
			if isTrue:
				return 1 if exp[i] == 'T' else 0
			else:
				return 1 if exp[i] == 'F' else 0
		
		if dp[i][j][isTrue] != -1: return dp[i][j][isTrue]
		
		count = 0

		for k in range(i+1,j,2):

			x1 = helper(i,k-1,1)
			x2 = helper(k+1,j,1)
			x3 = helper(i,k-1,0)
			x4 = helper(k+1,j,0)

			if exp[k] == '|':
				if isTrue:
					count += ((x1 * x2 ) + (x1 * x4) + (x2 * x3))
				else:
					count += (x3*x4)
			
			elif exp[k] == '^':
				if isTrue:
					count += ((x1*x4) + (x2*x3))
				else:
					count += ((x1*x2) + (x3*x4))
			
			else:
				if isTrue:
					count += (x1*x2)
				else:
					count += ((x3 * x4) + (x1 * x4) + (x2 * x3))

		dp[i][j][isTrue] = count % 1000000007
		return dp[i][j][isTrue]

	return helper(0,n-1,1)


def evaluateExp(exp):

	n = len(exp)
	dp = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]

	for i in range(n):
		dp[i][i][1] = 1 if exp[i] == 'T' else 0
		dp[i][i][0] = 1 if exp[i] == 'F' else 0
	
	for i in reversed(range(0,n,2)):
		for j in range(i+2,n,2):
			countTrue = 0
			countFalse = 0

			for k in range(i+1,j,2):

				x1 = dp[i][k-1][1]
				x2 = dp[k+1][j][1]
				x3 = dp[i][k-1][0]
				x4 = dp[k+1][j][0]

				if exp[k] == '|':
					countTrue += ((x1 * x2 ) + (x1 * x4) + (x2 * x3))
					countFalse += (x3*x4)
				
				elif exp[k] == '^':
					countTrue += ((x1*x4) + (x2*x3))
					countFalse += ((x1*x2) + (x3*x4))
				
				else:
					countTrue += (x1*x2)
					countFalse += ((x3 * x4) + (x1 * x4) + (x2 * x3))

			dp[i][j][1] = countTrue 
			dp[i][j][0] = countFalse 			

	return dp[0][n-1][1] % 1000000007