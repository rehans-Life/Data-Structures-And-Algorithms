from queue import Queue

class Solution:
    
    def bfs(self,row,col,grid,visited):
        
        queue = Queue()
        queue.put([row,col])
        visited[row][col] = True
        n = len(grid)
        m = len(grid[m])
        
        while not queue.empty():
            
            row,col = queue.get()
            
            # Running a loop for calculating all the neighbours
            # This x covers the rows from row+1, row and row-1.
            for x in range(-1,2):
                # This y covers the columns col-1,col and col+1 for each row.
                for y in range(-1,2):
                    nRow = row+x
                    nCol = col+y
                    if nRow >= 0 and nRow < n and nCol >= 0  and nCol < m and not visited[nRow][nCol] and grid[nRow][nCol]:
                        queue.put([nRow,nCol])
                        visited[nRow][nCol] = True
                
    def numIslands(self,grid):
        # This is going to be the visited grid to mark the visited islands
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        # A counter for our number of islands
        islands = 0
        
        # Then we need to traverse each cell within the grid to find 
        # unvisited nodes 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # If we find an actual node which is unvisited then we 
                # have found an island that we have yet to add to in our
                # count so we add it and traverse that island so that
                # when we traverse the nodes of that island they are 
                # already marked as visited and we dont have to consider    
                # them as islands.
                if grid[i][j] and not visited[i][j]:
                    islands+=1
                    self.bfs(i,j,grid,visited)
                
        return islands