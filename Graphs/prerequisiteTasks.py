from queue import Queue

class Solution:
    def isPossible(self,N,prerequisites):
        #Adjacency list for graph representation
        adj = [[] for _ in range(N)]
        for neighbour,parent in prerequisites:
            adj[parent].append(neighbour)
        
        # A queue to implement our bfs and its only going to consists of
        # nodes whose nodes which connect to it have already been placed
        # into the output cause they should exists before them in the
        # ordering.
        queue = Queue()
        
        # An output array to store our ordering
        order = []
        
        # An indegrees array which is going to store the indegrees of
        # each node within the graph (indegrees is the number of inward
        # edges of a node)
        indegrees = [0] * N
        
        # Finding the indegrees of each node
        # Checking for all nodes and seeing which nodes are conneting
        # to it and incrementing the indegrees for it
        for connectedNodes in adj:
            if node in connectedNodes:
                indegrees[node]+=1
        
        # Then those nodes which have zero indegrees should come first
        # within the ordering so i add them to the queue initially
        for node in range(N):
            if indegrees[node] == 0:
                queue.put(node)
                
        while not queue.empty():
            # Taking the top node out and inserting it into the ordering
            node = queue.get()
            order.append(node)
            
            # Then decrementing the indegree of nodes connected to it
            # cause one of the nodes which has an outward edge to it
            # just got inserted into the ordering if after decrementing
            # its indegree goes to zero hence that means all of the nodes
            # connecting to it are inserted and now its there turn so
            # I add them to the queue
            for neighbour in adj[node]:
                indegrees[neighbour]-=1
                if indegrees[neighbour] == 0:
                    queue.put(neighbour)
             
        # Then in the end if the order consist of n nodes hence the 
        # topo sort works which means there is no cycle and in that case
        # i can return True cause all tasks can be performed then
        # else false cause there is a cycle
        return True if len(order) == N else False

print([[]] * 5)