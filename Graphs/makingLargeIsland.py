from typing import *
from math import *

class DisjointSet:
    def __init__(self,V):
        self.size = [1] * V
        self.par = [i for i in range(V)]
    
    def findParent(self,node):

        if self.par[node] == node:
            return node
        
        ultimateParent = self.findParent(self.par[node])

        self.par[node] = ultimateParent 

        return ultimateParent

    def union(self,u,v):

        pu = self.findParent(u)
        pv = self.findParent(v)

        if pu == pv: return

        if self.size[pv] > self.size[pu]:
            self.par[pu] = pv
            self.size[pv]+=self.size[pu]
        else:
            self.par[pv] = pu
            self.size[pu]+=self.size[pv]

    def getSize(self,node):
        return self.size[node]

class Solution:

    def isValid(self,row,col,n):
        return row >= 0 and row < n and col >= 0 and col < n 

    def largestIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        disjointSet = DisjointSet(n*n)

        delRow = (-1,+1,0,0)
        delCol = (0,0,+1,-1)

        largestIsland = -inf

        # Connect all the islands together
        for row in range(n):
            for col in range(n):
                # When i find an land i connect it to its adjacent lands in the matrix
                if grid[row][col] == 1:

                    for i in range(4):
                        adjRow = row + delRow[i]
                        adjCol = col + delCol[i]

                        # Checking if its adjacent cell is in bound 
                        if self.isValid(adjRow,adjCol,n):
                            # Check if its actually a land that i can connect to
                            if grid[adjRow][adjCol] == 1:
                                # I need to compute the numric value of these cells
                                node = row * n + col
                                adjNode = adjRow * n + adjCol
                                # Then i can connect them into one island
                                disjointSet.union(node,adjNode)

        # Now i wanna iterate through all the zero valued cells and check which one when turned to 1 will 
        # produce the largest island.
        for row in range(n):
            for col in range(n):

                # If the cell is a zero
                if grid[row][col] == 0:
                    # A set to store the ultimate parents of all the adjacent islands.
                    ultParents = set()

                    # I wanna check in its adjacent cells and check if there are islands adjacent to it.
                    for i in range(4):
                        adjRow = row - delRow[i]
                        adjCol = col - delCol[i]

                        # Checking if the adj cell is in bound.
                        if self.isValid(adjRow,adjCol,n):
                            # Then checking if there is an island adjacent to this cell. 
                            if grid[adjRow][adjCol] == 1:
                                # If there is an island then i want its ultimate parent and i store it in a set.
                                adjNode = adjRow * n + adjCol
                                ultimateParent = disjointSet.findParent(adjNode)
                                ultParents.add(ultimateParent)

                    # Then i need to compute the island size by adding up sizes of all the ajdacent islands.
                    islandSize = 1
                    for ultimateParent in ultParents:
                        islandSize+=disjointSet.getSize(ultimateParent)
                    
                    # Checking if this is the largest island that ive generated up until now.
                    largestIsland = max(largestIsland,islandSize)

        # It could be that there are no zeroes within grid in that case i return that grid size.        
        return largestIsland if largestIsland != -inf else n*n