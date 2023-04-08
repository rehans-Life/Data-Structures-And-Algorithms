from queue import PriorityQueue
from math import *

# This function is for finding the shortest distance from end node to all the other nodes
def dijkstrasAlgorithm(src,distance,adj):
    
    priorityQueue = PriorityQueue()    
    priorityQueue.put([0,src])
    distance[src] = 0
    
    while not priorityQueue.empty():        
        srcDistance,node = priorityQueue.get()

        for adjNode,adjDistance in adj[node]:
            # The adjacent nodes distance from the source will be able current nodes distance from source 
            # plus current nodes distance from adjacent node.
            newDistance = adjDistance + srcDistance
            
            # If this new distance is lesser then only you update the adjacent nodes distance from source 
            # and add it in the queue to compute its adjacent nodes distance as well
            if newDistance < distance[adjNode]:
                distance[adjNode] = newDistance
                priorityQueue.put([newDistance,adjNode])
        
def aStar(src,end,adj,V):
    
    priorityQueue = PriorityQueue()
    
    # An array to store each nodes shortest distance from end node as sourcr 
    huristic = [inf] * V
        
    dijkstrasAlgorithm(end,huristic,adj)
    
    # Then we can create an an array to get the shortest distance to our end node from actual source
    distance = [inf] * V
    
    # Initially we insert the source node into the pq and we know its distance from source is 0 and also we add 
    # are going to prioritize the nodes on the basis of there distance from source plus there distance from end 
    # as well
    distance[src] = 0
    priorityQueue.put([0+huristic[src],0,src])
    
    while not priorityQueue.empty():
        
        _,srcDistance,node = priorityQueue.get()
        if node == end:
            print(newDistance)
        
        # Computing the nodes adjacenot nodes distance from source
        for adjNode,adjDistance in adj[node]:
            newDistance = srcDistance + adjDistance
            if newDistance < distance[adjNode]:
                distance[adjNode] = newDistance
                priorityQueue.put([(newDistance+huristic[adjNode]),newDistance,adjNode])
        
    return distance
        
edges = [[0,4,4],[0,1,4],[1,4,2],[2,4,1],[2,5,3],[3,5,2],[4,3,3],[4,5,6]]
V = 6
adj = [[] for _ in range(6)]
for node1,node2,weight in edges:
    adj[node1].append([node2,weight])
    adj[node2].append([node1,weight])   
    
print(aStar(0,5,adj,V))        
    
    
    
    