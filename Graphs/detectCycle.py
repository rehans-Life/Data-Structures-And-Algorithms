from typing import List
from queue import Queue

# Breath First Search

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
            # are going to rot their neighbouring oranges.
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
        
# Dpet Dirst Search

class Solution:
    def detectCycle(self,node,prev,visited,adj):
        
        # Marking the node we are treaversing as visited
        visited[node] = True
        
        # Going indept into one directions from this node then we will
        # move onto the other one
        
        # I can get its neighbours by looking at its index the adjacency
        # list.        
        for neighbour in adj[node]:
            if not visited[neighbour]:
                # If the neighbour is not visited then i go in dept
                # and try to detect if there is a cycle
                
                # If we get a true then there is no need to check the
                # other neighbours we can just return True from here
                if self.detectCycle(neighbour,node,visited,adj):
                    return True
            # If the neighbour is visited and its not the previous
            # node where we came from just now hence we have found 
            # a cycle.
            elif neighbour != prev:
                return True
        
        # If we couldnt detect a cycle anywhere then we return False
        return False
        
        
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
		# An array to mark our nodes as visited once they are traversed
		# The value of nodes does start from zero itself.
        visited = [False] * V
		
        # And since the graph could consist of connected components
        # so we will run a traversel 0 to v which will allows us
        # to cover all the components. 
        for node in range(V):
            # If any of the components have a cycle then we can say
            # the graph has a cylce.
            if not visited[node] and self.detectCycle(node,-1,visited,adj):
                return True
        
        return False        
  
d = set()  
shape = [[3,4],[2,4],[6,8],[4,5]]
r,c = shape[0]
for i in range(len(shape)):
    shape[i][0]-=r
    shape[i][1]-=c
    shape[i] = tuple(shape[i])
print(shape)