from typing import List
from queue import Queue

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        delRow = [-1,0,0,1]
        delCol = [0,-1,1,0]

        # A visited matrix to mark all the land cells which either exists on the boundry or are directly or
        # indirectly connected to one of the boundry cells so i know which land cells are not in my answer
        visited = [[False for _ in range(m)] for i in range(n)]

        # A queue for the bfs traversel
        queue = Queue()

        # A counter for the land cells through which i cannot out of boundry
        lands = 0

        # Initially adding all the boundry land cells into the queue and marking them as visited
        # So for that i need to traverse the first and last row and first and last column.
        for col in range(m):
            # First row
            if grid[0][col] == 1 and not visited[0][col]:
                visited[0][col] = True
                queue.put([0,col])
            
            # last row
            if grid[n-1][col] == 1 and not visited[n-1][col]:
                visited[n-1][col] = True
                queue.put([n-1,col])
        
        for row in range(n):
            # First column
            if grid[row][0] == 1 and not visited[row][0]:
                visited[row][0] = True
                queue.put([row,0])
            
            # last column
            if grid[row][m-1] == 1 and not visited[row][m-1]:
                visited[row][m-1] = True
                queue.put([row,m-1])
        
        # Then i can start my bfs traversel and continue with it until the queue goes empty
        while not queue.empty():
            
            row,col = queue.get()

            # Taking the land out and adding its neighbours back into the queue
            for i in range(4):
                nRow = row + delRow[i]
                nCol = col + delCol[i]

                if nRow >= 0 and nRow < n and nCol >= 0 and nCol < m and not visited[nRow][nCol] and grid[nRow][nCol]:
                    queue.put([nRow,nCol])
                    visited[nRow][nCol] = True

        # After the bfs traversel has ended i just need to traverse the grid and the lands which are unvisited are going to be considered
        # in my answer because since they are unvisited hence they are not any of the boundry lands nor are they conntected to any thats
        # why they are still unvisited therefore i cant go out of bound from them.
        for row in range(n):
            for col in range(m):
                if grid[row][col] and not visited[row][col]:
                    lands+=1

        return lands        
