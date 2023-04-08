from queue import Queue
from typing import *
from math import *

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        if grid[0][0] == 1:
            return -1

        if n-1 == 0:
            return 1

        distance = [[inf for _ in range(m)] for _ in range(n)]

        queue = Queue()

        distance[0][0] = 0
        queue.put([1,0,0])

        while not queue.empty():

            srcDistance,row,col = queue.get()

            newDistance = srcDistance + 1

            for delRow in range(-1,2):

                for delCol in range(-1,2):

                    adjRow = row + delRow
                    adjCol = col + delCol

                    if adjRow < n and adjRow >= 0 and adjCol < m and adjCol >= 0 and grid[adjRow][adjCol] == 0 and newDistance < distance[adjRow][adjCol]:
                        
                        if adjRow == n-1 and adjCol == n-1:
                            return newDistance

                        distance[adjRow][adjCol] = newDistance
                        queue.put([newDistance,adjRow,adjCol])
        
        return -1