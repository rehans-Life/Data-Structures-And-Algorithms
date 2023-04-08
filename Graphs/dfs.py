
class Solution:
    def dfsOfGraph(self, V, adj):
        # We need a storage for our traversel values
        dfs = []
        
        # Maintaining a visited array so we dont traverse the same node
        # again
        visited = [False] * V
        
        # A recursive function to perform dfs
        def helper(node):
            
            # Including the node in our dfs traversel
            dfs.append(node)
            
            # Marking the node we traversed in our visited nodes
            visited[node] = True
            
            # Then going in dept in all directions from this node
            for neighbour in adj[node]:
                # If only the neighbour has not been visited then your
                # going to go indept in that direction
                if not visited[neighbour]:
                    helper(neighbour)
        
        helper(0)
        return dfs
                    
