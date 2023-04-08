from sys import *
from collections import *
from math import *

# Memoization

# Time Complexity: O(n*m)
# Space Complexity: o(n+m + n*m)

def uniquePaths(m, n):

	# Declaring a dp grid so that we can store the solutions to all the 
	# subproblems we solve.
	dp = [[-1 for _ in range(n)] for _ in range(m)]
	
	def helper(row,col):

		# When we reach our destination cell we return suggesting there
		# is one path from this cell to destination cell
		if row == 0 and col == 0:
			return 1
		
		# If we go out of bound we return 0 to denote there are no paths from
		# this cell to the destination cell cause its out of bound
		if row < 0 or col < 0:
			return 0
		
		# Now before deviding this problem into subproblems we check if we
		# have already solved it or not via our dp array and if we have then
		# we just return the solution for it
		if dp[row][col] != -1: return dp[row][col]

		# To be able to compute how many ways we can reach from this cell to
		# the destination cell we need to find the number of ways we can reach
		# destination cell from the cell above and from the cell on the left
		# if we have that then we can just sum them up and that would be total
		# ways we can reach destination cell from this cell.
		left = helper(row,col-1)
		up = helper(row-1,col)

		# Since we solved this subproblem we store its solution in our 
		# dp array for future and return its solution to solve other problems

		dp[row][col] = left + up

		return dp[row][col]

	return helper(m-1,n-1)

# Tabulation 

# Time Complexity: O(n*m)
# Space Complexity: O(n*m)

def uniquePaths(m, n):

	# Declaring a dp grid so that we can store the solutions to all the 
	# subproblems we solve.
	dp = [[-1 for _ in range(n)] for _ in range(m)]
	
	# To cover all states in the recursion and in order to start from bottom
	# states of recursion tree to up states we gotta start from 0th row
	# and go till last row and even for columns for each row we gotta start
	# from 0th column to the last column 
	
	for i in range(m):
		for j in range(n):
			# If base case then we from it to destination cell one path exists
			# so we mark it in dp array
			if i == 0 and j == 0: 
				dp[i][j] = 1
			else:
				# Now for a cell to compute its paths to destination we need
				# to know its upward cells paths and left cells path to 
				# destination and we need to sum them up for this cell

				# And since we going to bottom to up of recursion tree its 
				# bottom guys in recursion are already computed so we access
				# its values from dp array
				up = 0
				left = 0

				if i > 0:
					up = dp[i-1][j]
				
				if j > 0:
					left = dp[i][j-1]
				
				dp[i][j] = up + left

	return dp[m-1][n-1]

# Space Optimised

# Time Complexity: O(n*m)
# Space Complexity: O(m)


def uniquePaths(m, n):

	# Now to be able to compute a certain rows values we only need its previous
	# row so thats the only thing that we will actually store.
	prev = [0] * n

	# To cover all states in the recursion and in order to start from bottom
	# states of recursion tree to up states we gotta start from 0th row
	# and go till last row and even for columns for each row we gotta start
	# from 0th column to the last column. 
	
	for i in range(m):

		# We store the current row values to get left guys for each cell
		# also to replace the current previous with this rows values to compute
		# next row.
		temp = [0] * n

		for j in range(n):
			# If base case then we from it to destination cell one path exists
			# so we mark it in dp array
			if i == 0 and j == 0: 
				temp[j] = 1
			else:
				# Now for a cell to compute its paths to destination we need
				# to know its upward cells paths and left cells path to 
				# destination and we need to sum them up for this cell

				# And since we going to bottom to up of recursion tree its 
				# bottom guys in recursion are already computed so we access
				# its values from dp array
				up = 0
				left = 0

				if i > 0:
					up = prev[j]
				
				if j > 0:
					left = temp[j-1]
				
				temp[j] = up + left

		prev = temp

	return prev[n-1]
