#User function Template for python3

class Solution:
    def sortTime(self,node,stack,visited,adj):
        
        visited[node] = True
        
        for adjNode in adj[node]:
            if not visited[adjNode]:
                self.sortTime(adjNode,stack,visited,adj)
        
        stack.append(node)
    
    def dfs(self,node,visited,adj):
        
        visited[node] = True
        
        for adjNode in adj[node]:
            if not visited[adjNode]:
                self.dfs(adjNode,visited,adj)            
        
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        
        stack = []
        visited = [False] * V
        
        for node in range(V):
            if not visited[node]:
                self.sortTime(node,stack,visited,adj)
        
        revAdj = [[] for _ in range(V)]
        
        for node in range(V):
            for adjNode in adj[node]:
                revAdj[adjNode].append(node)
        
        count = 0
        visited = [False] * V
        
        while len(stack):
            node = stack.pop()
            if not visited[node]:
                count+=1
                self.dfs(node,visited,revAdj)
               
        
        return count
        
        
        
        
        
