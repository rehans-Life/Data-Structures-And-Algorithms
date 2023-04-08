from queue import *
from math import *
class Solution:
    def shortestPath(self, n, m, edges):
        
        adj = [[] for _ in range(n+1)]
        
        for node1,node2,edgeWeight in edges:
            adj[node1].append([node2,edgeWeight])
            adj[node2].append([node1,edgeWeight])
        print(adj)
        # So we need to perform a dijkstra's algorithm in order to get the 
        # shortest path to each node
        
        # A priority queue which is going to store the nodes along with there
        # distance from the source node on the basis of which it is going to
        # sort by and we are inserting them in here so we can find there
        # adajcent nodes distances from the source node as well.
        priorityQueue = PriorityQueue()
        
        # A distances array which is going to store the distances of each node
        # from the source node
        distance = [inf] * (n+1)
        
        # A path array which is going to store the node from where we are getting
        # the shortest distance to a node 
        path = [-1] * (n+1)
        
        # Initially to the source node we know we gon take a distance of
        # zero from source node.
        
        # And we are getting that shortest distance from souece node itself
        # so in path at index of source node we store the source itself
        distance[1] = 0
        path[1] = None
        
        priorityQueue.put((0,1))
        
        # Taking nodes out of the queue until it is empty
        while not priorityQueue.empty():
            
            # Taking the guy with the shortest distance to source out cause
            # its on top of the pq
            srcDistance,node = priorityQueue.get()
            
            # I need to find its adajcent nodes distances from source and 
            # update them
            for adjNode,adjDistance in adj[node]:
                newDistance = srcDistance + adjDistance
                # Only if the node previous distance is greater do we need
                # to update it to this new distance and update the path
                # array 
                if newDistance < distance[adjNode]:
                    distance[adjNode] = newDistance
                    # Since we have found a shorter distance to its adjacent
                    # node from this node hence its going to set as the node
                    # from which we are getting the shortest path to this
                    # node from.
                    path[adjNode] = node
                    # Also inserting the node in to the pq in order to get
                    # its adjacent nodes distance from source node
                    priorityQueue.put((newDistance,adjNode))
            
        shortestPath = []
        
        if path[n] == -1: return [-1]
        
        i = n
        print(i)        
        while i:
            print(i)        
            shortestPath.append(i)
            i = path[i]
        
        shortestPath.reverse()
        
        return shortestPath
    
solution = Solution()
edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]
ans = solution.shortestPath(5,len(edges),edges)
print(ans)