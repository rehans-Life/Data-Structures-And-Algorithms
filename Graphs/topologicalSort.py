class Solution:
    
    def dfs(self,node,visited,stack,adj):
        
        # Marking the node im traversing a visited
        visited[node] = True

        # Then im going to recurse on the nodes to which its connected
        # to.
        for neighbour in adj[node]:
            if not visited[neighbour]:
                self.dfs(neighbour,visited,stack,adj)
        
        # After i have recursed on its connected nodes then only im 
        # going to include the node within the stack cause then it
        # will added on top of them within the stack hence exist before
        # them in ordering which helps us the stafiy the property.
        stack.append(node)
            
    def topoSort(self, V, adj):
        
        # A visited array to mark the nodes we have already visited in
        # our graph
        visited = [False] * V
        
        # A stack to maintain our topological order
        stack = []
        
        # Then traversing all the nodes cause we wanna traverse
        # the components as well if the graph is divided into any
        for i in range(V):
            # If the node is not visited hence i havent traversed its
            # component so i will perform the bfs on it.
            if not visited[i]:
                self.dfs(i,visited,stack,adj)
        
        # Then taking popping all the nodes out starting from the top
        # of the stack and inserting them into the answer
        ans = []
        while len(stack): ans.append(stack.pop())
        
        return ans
        