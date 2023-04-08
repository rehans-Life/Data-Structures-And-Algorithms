from math import *

# Time Comlexity: O(n^3)
# Space Complexity: O(n^2)

class Solution:
    
	def shortest_distance(self, matrix):
	    
            n = len(matrix)
            
            # First thing if there are no edges between two nodes we replace 
            # -1 to infinity
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] == -1:
                        matrix[i][j] = inf
            
            # Then we compute distances between two nodes i and j by going through 
            # paths via every node within the graph
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        # Then we store the minimum of the distance we are currently
                        # taking in order to go from i to j then what we are taking
                        # in order to go from i to j via the path from k.
                        matrix[i][j] = min(matrix[i][j],matrix[i][k]+matrix[k][j])
            
            # If any nodes distance to itself is negative then there is negative cycle
            for i in range(n):
                if matrix[i][i] < 0:
                    return -1
            
            # Then in the end if anyone is infinity that means we cant go that
            # node from any of the paths thats exists within the graph so we
            # wanna change them back to -1
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] == inf:
                        matrix[i][j] = -1
            
            return matrix