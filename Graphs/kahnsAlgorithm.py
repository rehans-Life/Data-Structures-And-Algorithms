from queue import Queue
class Solution:
    def topoSort(self, V, adj):
        
        # A queue for our bfs traversel
        queue = Queue()
        
        # An indegrees array which is going to store the indegrees of each
        # node in the graph (indegrees is the number of edges coming into 
        # a node)
        indegrees = [0] * V
        
        # A node to store the ordering of the graph
        ans = []
        
        # Going through each node to count the indegrees
        for node in range(V):
            # Going to through each node to check how many of them have
            # a connection to the current node im iterating so i can count
            # its indegrees.
            for i in range(V):
                if node in adj[i]:
                    indegrees[node]+=1
        
        # Inserting the nodes with zero indegree into the queue
        for node in range(V):
            if indegrees[node] == 0:
                queue.put(node)
        
        # Then our bfs runs until queue is empty
        while not queue.empty():
            node = queue.get()
            
            # Inserting the node in our output array 
            ans.append(node)
            
            # Decrementing its connected indegree by one and if it
            # becomes zero after decrementing i add it in the queue
            # because that means that all the nodes that should be
            # placed on the left of this node in the output and 
            # actually placed there so now im adding it to the queue
            # so it can placed within the output.
            for neighbour in adj[node]:
                indegrees[neighbour]-=1
                if indegrees[neighbour] == 0:
                    queue.put(neighbour)
        
        return ans
