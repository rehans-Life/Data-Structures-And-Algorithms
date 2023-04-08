from queue import PriorityQueue

class Solution:
    
    def spanningTree(self, V, adj):
        
        # A visited array to mark the nodes we have already added into our mst
        visited = [False] * V
        
        # An array to store the edges of the mst
        mst = []
        
        # A sum to store the sum of mst
        sum = 0
        
        # A priority queue to store the nodes nodes along with the weights
        # taken in order to get to them along with their parents
        priorityQueue = PriorityQueue()
        
        # Initially we know in order to get to the parent we take weight zero
        # and there is no parent
        priorityQueue.put([0,0,-1])
        
        while not priorityQueue.empty():
            
            weight,node,parent = priorityQueue.get()
            
            # If node already visisted then continue to next node
            if visited[node]: continue
            
            # Adding up the weight taken in order to get to this node into
            # the mst sum
            sum+=weight
            
            # Adding the edge into our mst array
            mst.append([parent,node])
            
            # Then marking it as visited
            visited[node] = True
            
            # Then move its unvisited ajdacent nodes
            for adjNode,adjWeight in adj[node]:
                # If adjacent node not already visited then we consider it
                if not visited[adjNode]:
                    priorityQueue.put([adjWeight,adjNode,node])
        
        return sum,mst

solution = Solution()
ans = solution.spanningTree()