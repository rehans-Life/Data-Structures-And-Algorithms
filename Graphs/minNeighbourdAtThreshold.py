from typing import List
from math import *

class Solution:
    
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        # A matrix to store our shortest distances from each node to every other node in the graph
        distance = [[inf if i != j else 0 for j in range(n)] for i in range(n)]

        # Marking the adjacent nodes with there weights.
        for node1,node2,weight in edges:
            distance[node1][node2] = weight
            distance[node2][node1] = weight
        
        # Then we go through each node within the graph and for each pair of cities i and j we compute
        # distances between them via the path through our the node.
        for k in range(n):
            # Going through each city i and j and computing there distances from the path through k
            for i in range(n):
                for j in range(n):
                    # We update the distance for the cell only if distance from the path via k is lesser 
                    # than the distance we previously computed for them
                    distance[i][j] = min(distance[i][j],distance[i][k]+distance[k][j])

        # A variable to store our city with the lowest number of cities under the threshold
        city = 0

        # A variable to store the minmum number of cities we have found a city being connected
        # too within the threshold initially it is n so any city can beat it
        countMin = inf

        for i in range(n):

            # A counter to count the number of cities found be within the threshold from the city i
            count = 0

            for j in range(n):
                if distance[i][j] <= distanceThreshold:
                    count+=1
            
            # If the number of cities that can be reached via this city is lesser than the previous
            # minimum we have found up until now then we update the city to this city and we also
            # update minimum count to this cities count.
            if count <= countMin:
                city = i
                countMin = count
        
        return city
