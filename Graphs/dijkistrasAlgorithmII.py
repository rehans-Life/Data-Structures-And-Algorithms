from math import * 

class Solution:
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        
        # A set which is going to store our nodes along with the distances 
        # taken in order to get to them via the source node.
        
        # A set will store the nodes in ascending order of there distances
        # from the source node
        
        s = set()
        
        # A distance array which is going store the distance taken to get
        # to each node from the source node
        distance = [inf] * V
        
        # Intially we know in order to get to the source node we will take a
        # distance of 0 so we mark it with that distance and we also insert
        # it into the set with that distance so we can find its adjacent
        # nodes distances
        distance[S] = 0
        s.add((0,S))
        
        # Then we starting nodes out of the set until it goes empty
        while len(s):
            # In order to get the first pair of the set we assign it a
            # iterator and take the first pair out by using next method
            # to move the iterator to the first pair which is the one
            # with the shortest distance to source.
            pair = next(iter(s))
            srcDistance,node = pair
            
            # Then im removing it from the set
            s.discard(pair)
            
            # Now since i have my current nodes distance from the source node
            # i can calculate the distance of the source node from my 
            # current node's adjacent nodes as well
            for neighbour,adjDistance in adj[node]:
                newDistance = adjDistance + srcDistance
                
                # So if this path is the first path ive found to this 
                # adjacent node i just set this distance in the array
                # and i add it to the set to find it adjacent nodes distance.
                if distance[neighbour] == inf:
                    distance[neighbour] = newDistance
                    s.add((newDistance,neighbour))
                # Now if I've already found a path to this adjacent node
                # previously and this is a shorter one hence i need to 
                # make sure i delete its previous instance from the set as
                # well cause its useless now and then i will insert it
                # in the set with the new distance.
                elif newDistance < distance[neighbour]:
                    s.discard((distance[neighbour],neighbour))
                    distance[neighbour] = newDistance
                    s.add((newDistance,neighbour))
            
        return distance