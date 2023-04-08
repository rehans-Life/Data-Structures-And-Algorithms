import sys
from typing import List
sys.setrecursionlimit(10**8)

class Solution:
    def dfs(self,row,col,shape,grid,visited,delRow,delCol,n,m) -> None:
        # Marking the node im traversing and including it in the shapes
        # array for the island
        visited[row][col] = True
        shape.append([row,col])
        
        # Then going in all four directions.
        for i in range(4):
            nRow = row + delRow[i]
            nCol = col + delCol[i]
            
            if nRow >= 0 and nRow < n and nCol >= 0 and nCol < m and grid[nRow][nCol] and not visited[nRow][nCol]:
                self.dfs(nRow,nCol,shape,grid,visited,delRow,delCol,n,m)
    
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        delRow = [-1,0,0,+1]
        delCol = [0,1,-1,0]
        
        # A matrix to mark all of our visited cells
        visited = [[False for _ in range(m)] for i in range(n)]
        
        # A set to store the shapes of our distinct islands
        distinctIslands = set()
        
        # Then i need to traverse the grid to find all the islands
        for row in range(n):
            for col in range(m):
                # If the cell with a value one isnt visited then that
                # means ive found an island so i perform dfs on it.
                if grid[row][col] == 1 and not visited[row][col]:
                    # An array to store the shape
                    shape = []
                    self.dfs(row,col,shape,grid,visited,delRow,delCol,n,m)
                    # Now initially shape is going store the coordinates of all the cells of the island
                    # to get the shape i need to stubtract all the coordinates by the first cells coordinates
                    r,c = shape[0]
                    for i in range(len(shape)):
                        shape[i][0]-=r
                        shape[i][1]-=c
                        shape[i] = tuple(shape[i])
                    # Lists arent hashable so converting the lists
                    # with the shape into a tuple
                    shape = tuple(shape)
                    distinctIslands.add(shape)
        
        return len(distinctIslands)
                    