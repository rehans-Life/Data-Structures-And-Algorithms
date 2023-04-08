from queue import Queue

class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
            n = len(grid)
            m = len(grid[0])
            
            # This grid is for storing the distances of each of the nodes
            distance = [[0 for _ in range(m)] for _ in range(n)]
            
            # This grid is for marking the visited nodes as i traverse them
            visited = [[False for _ in range(m)] for _ in range(n)]

            # A queue for the bfs traversel
            queue = Queue()
            
            # Include all the nodes with value 1 inside of the queue mark
            # them visited and set there distances as 0 cause they themselves
            # are nearest cells with value 1
            for row in range(n):
                for col in range(m):
                    if grid[row][col] == 1:
                        queue.put([row,col])
                        distance[row][col] = 0
                        visited[row][col] = True
            
            # Then i start my bfs traversel
            while not queue.empty():
                # Taking the top most node out of the queue
                row,col = queue.get()
                
                # Then i need add its neighbouring nodes back into the queue
                # and i will have to mark them as visited and also there 
                # distance with the nodes with value 1 is going to be one
                # more than the distance of this curr node from one 
                if row+1 < n and not visited[row+1][col]:
                    queue.put([row+1,col])
                    visited[row+1][col] = True
                    distance[row+1][col] = distance[row][col] + 1
                
                if row-1 >= 0 and not visited[row-1][col]:
                    queue.put([row-1,col])
                    visited[row-1][col] = True
                    distance[row-1][col] = distance[row][col] + 1
                
                if col+1 < m and not visited[row][col+1]:
                    queue.put([row,col+1])
                    visited[row][col+1] = True
                    distance[row][col+1] = distance[row][col] + 1
                
                if col-1 >= 0 and not visited[row][col-1]:
                    queue.put([row,col-1])
                    visited[row][col-1] = True
                    distance[row][col-1] = distance[row][col] + 1
            
            return distance
             

#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends