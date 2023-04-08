from typing import List
from math import * 

class Solution:
    
    def dfs(self,node,stack,visited,adj,n):
        
        # Marking the node as visited.
        visited[node] = True
        
        # Recursing on its adjacent nodes 
        for neighbour,_ in adj[node]:
            self.dfs(neighbour,stack,visited,adj,n)
        
        # After ive recursed the nodes to which this node was connected
        # to hence then that means they have been added into the stack
        # which means i can insert this node now cause it will exist on
        # top of them within the stack and hence be able to exist before
        # them in ordering as well and this is important to meet the
        # topo sort porperty
        stack.append(node)
        
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        
        # Iterating through the edges to find the connections
        for edge in edges:
            # The node at index 0 has an directed edge to node at index 1
            # and the distance its going to take in order to go from that
            # node to that adjacent Node via the edge is going at index 2.
            node = edge[0]
            adjacentNode = edge[1]
            distance = edge[2]
            adj[node].append([adjacentNode,distance])
        
        # Then a visited array for the dfs and a stack to store our
        # topological ordering.
        stack,visited = [],[False] * n
        
        # Since the graph can be divided into components hence we can
        # run a loop from 0 to n to cover all the components.
        for node in range(n):
            # If the node is not visited hence ive discovered a new
            # component which i havent traverse so I run dfs on it.
            if not visited[node]:
                self.dfs(node,stack,visited,adj,n)
            
        # Declaring a distance array of size n to cover all node values
        # intially for each the distances will be assigned as infinity
        distance = [inf] * n
        
        # Assigning the source node a distance of 0 cause its at a distance
        # of zero from itself
        distance[0] = 0
        
        # Then computing the distances via the stack
        while len(stack):
            node = stack.pop()
            currDistance = distance[node]
            # Now im assuming the distance stored at this nodes index
            # in the distance array is its distance from the source
            # therefore i can find the distance of the source node of
            # this nodes adjacent nodes then.
            for neighbour,adjDistance in adj[node]:
                # I might have already found a shorter path so i will
                # only set this as the neighbour distance from the source
                # if its less than the previous one ive already stored
                newDistance = currDistance+adjDistance
                if  newDistance < distance[neighbour]:
                    distance[neighbour] = newDistance 
        
        # The nodes in the end that still have a distance of infinity
        # have no connection to the source ndode hence i can set their
        # distance as -1
        for i in range(n):
            if distance[i] == inf:
                distance[i] = -1
        
        return distance