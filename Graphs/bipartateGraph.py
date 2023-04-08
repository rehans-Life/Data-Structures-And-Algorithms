from queue import Queue

class Solution:
    def checkBipartite(self,start,V,coloured,adj):
		
            # A queue for our bfs teaversel
            queue = Queue()
            
            # Initially including the root node inside of the queue and 
            # assigning it a color
            queue.put(start)
            coloured[start] = 0
            
            while not queue.empty():
                node = queue.get()		    
                
                # Adding its neighbouring nodes back into the queue
                for neighbour in adj[node]:
                    # If its not already coloured then assign it the opposite
                    # color
                    if coloured[neighbour] == -1:
                        queue.put(neighbour)
                        coloured[neighbour] = 0 if coloured[node] else 1
                    # If one of its adjacent nodes has been coloured and it 
                    # has the same colour hence the graph is not bipartite.
                    elif coloured[neighbour] == coloured[node]:
                        return False
            
            # If im able to color all the nodes in a proper manner without
            # disrupting the loop i can return True
            return True
            
    def isBipartite(self, V, adj):
            # Here is where we mark the colour for the nodes 
            coloured = [-1] * V
            
            for i in range(V):
                if coloured[i] == -1:
                    if not self.checkBipartite(i,V,coloured,adj):
                        return False
            
            return True