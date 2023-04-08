# Bellman-Ford Algorithm

# Time Complexity : O(V * E)
# Space Complexity: O(V)

from math import *

class Solution:
    
    def bellman_ford(self, V, edges, S):
        
        # Keeping a distance array to store the distance from source to all 
        # the other nodes within the array.
        distance = [100000000] * V 
        
        # Initially we know the distance in order to get the source is zero.
        distance[S] = 0
        
        # Relaxing each edge n-1 why because at max a path from the source
        # will have n-1 edges not more than that in a graph.
        
        # Hence even if you are able to relax only one edge upon each iteration
        # within a given patg you will still cover all edges in V-1 
        # iterations of every single path.
        
        # Hence sinxe relaxing is related finding the shortest distances to
        # each adjacent node hence you will be able to find the shortest
        # distance to each node from the source
        
        for _ in range(V-1):
            for u,v,w in edges:
                newDistance = distance[u] + w
                if newDistance < distance[v]:
                    distance[v] = newDistance
        
        # If on the nth iteration if the shortest distance to any node is 
        # still decreasing hence there is a negative cycle cause by n-1
        # i should be having the shortest distances to each node within the
        # graph.
        
        for u,v,w in edges:
            newDistance = distance[u]+w
            if newDistance < distance[v]:
                return [-1]
        
        return distance
        