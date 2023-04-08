from typing import List
from queue import Queue
class Solution:
    def checkRotted(self,grid):

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # If we find any fresh oranges after our traversel then that means all the
                # fresh oranges cannot be rotted.
                if grid[row][col] == 1:
                    return  False
        
        return True

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # A counter for counting how many minutes have passed
        minutes = 0
        # A queue for our bfs traversel which is going to store the rotted oranges
        queue = Queue()

        # Initially adding the rotted oranges into the queue
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    queue.put([row,col])

        # Then we keep going until our queue is empty
        while not queue.empty():
            # We need to traverse all the rotten oranges that in the same minute
            # are going to rot their neighbouring orange.
            qSize = queue.qsize()

            for _ in range(qSize):
                # Getting the rotted orange out and checking who he rots
                row,col = queue.get()

                # Getting in all four directions to see if there are any fresh oranges that
                # it can rot
                if row + 1 < len(grid) and grid[row+1][col] == 1:
                    queue.put([row+1,col])
                    grid[row+1][col] = 2
                
                if row - 1 >= 0 and grid[row-1][col] == 1:
                    queue.put([row-1,col])
                    grid[row-1][col] = 2

                if col + 1 < len(grid[row]) and grid[row][col+1] == 1:
                    queue.put([row,col+1])
                    grid[row][col+1] = 2
                
                if col - 1 >= 0  and grid[row][col-1] == 1:
                    queue.put([row,col-1])
                    grid[row][col-1] = 2

            # After the current rotted oranges have rotted their neigbouring oranges i need to
            # check did they rot any oranges or not cause only if they did are we going
            # increment our time 
            if not queue.empty(): 
                minutes+=1

        if self.checkRotted(grid):
            return minutes
        else:
            return -1