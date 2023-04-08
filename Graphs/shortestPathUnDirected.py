from math import *
from queue import Queue
from string import *
class Solution:
    
    def shortestPath(self, edges, n, m, src):
        
        # Finding the adjaceny list for the undirected graph
        adj = [[] for _ in range(n)]
        for node1,node2 in edges:
            # Since the edge is bidirectional hence both the nodes should
            # be in each others adjacency list.
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        # An array to store the distances of each node from the source 
        # node
        distances = [inf] * n
        
        # A queue to perform my bfs and find the distances of each node
        queue = Queue()
        
        # I know the source nodes distance from the source is 0
        # So im going to set its distance in the distance array.
        distances[src] = 0
        
        # Then also im going to start my bfs from the source node itself
        # and move outwards by one distance upon each iteration.
        queue.put([src,0])
        
        while not queue.empty():
            node,distance = queue.get()
            
        # Then finding its adjacent nodes distances from the source node
        
            # I know its adjacent nodes would be one extra distance away
            # from the source node than the current node.
            newDistance = distance + 1
            
            for neighbour in adj[node]:
                # Only if current distance of neighbour is greater than
                # update it
                if newDistance < distances[neighbour]:
                    distances[neighbour] = newDistance 
                    # Inserting the node inside of the queue to find its
                    # adjacent nodes distances from source node
                    queue.put([neighbour,newDistance])
            
        # In end the nodes with no path from source node will have 
        # distance of inf in the array but i gotta update it to -1
        for node in range(n):
            if distances[node] == inf:
                distances[node] = -1
        
        return distances
    