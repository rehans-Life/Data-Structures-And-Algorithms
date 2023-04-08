from queue import PriorityQueue
from math import * 

class Solution:
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        
        # A priority queue (minHeap) which is going to keep the nodes along
        # with the distances taken from src in order to get to them 
        
        # Its going to keep the nodes sorted on the basis of the distances
        # taken in order to get ot them.
        
        priorityQueue = PriorityQueue()
        
        # A distance array which is going to store the distances in order to
        # get to each node from the soruce node.
        # Initially all nodes marked as infinity 
        
        distances = [inf] * V
        
        # We know inorder to get to the source node the distances is zero
        # so we mark its index with zero and also insert into the priority
        # queue along with the distance
        distances[S] = 0
        
        # since I want the heap to sort on the basis of distances instead of
        # nodes so in the pair i keep the distance first and then the src
        priorityQueue.put([0,S])
        
        # Then we keep taking the top most node out of the PQ until its empty
        while not priorityQueue.empty():
            
            srcDistance,node = priorityQueue.get()
            
            # Since we have the distance from source node to our curr node
            # so then we can easily find the distances from the source node
            # to our curr node to adjacent nodes 
            for neighbour,distance in adj[node]:
                newDistance = srcDistance + distance
                # We will update the distance of neighbour from source node  
                # only if this new distance is less than what we currently
                # have in our array
                if newDistance < distances[neighbour]:
                    distances[neighbour] = newDistance
                    # Since we have got a shorter distance for it so i will
                    # also add it into the priority queue so i can calculate
                    # distance from src to its adjacent nodes as well
                    priorityQueue.put([newDistance,neighbour])
                    
        return distances
