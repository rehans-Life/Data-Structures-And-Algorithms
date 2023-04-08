
from queue import Queue
from typing import *
from math import *

class Solution:
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = [[] for _ in range(n)]
        for node1,node2,cost in flights: adj[node1].append([node2,cost])

        # An array to store the costs taken to get to each city from the sorce.
        cost = [inf] * n

        # A queue which is going to store the nodes along with the stops taken in order to get to them via
        # the source and as well as the cost taken in order to get to them from the source to we can compute
        # the same for there adjacent nodes as well.
        queue = Queue()

        # Intially we know source node can be reached at a cost of 0 and at stops 0 so we mark it with 0
        # in cost array and insert it into the queue to compute its adjacent nodes distances as well.
        cost[src] = 0
        queue.put([0,src,0])

        # Keep taking nodes out from queue until its empty.
        while not queue.empty():

            stops,node,srcCost = queue.get()

            # If node is the destination then we dont want to move to its adjacent nodes and we can just
            # continue.
            if node == dst:
                continue

            # Else we wanna compute its adjacent nodes cost as well to reach from source and also compute
            # the stops in order to get to them.
            for adjNode,adjCost in adj[node]:
                # New cost is equal to cost taken in order to reach adjacent node plus cost from source to
                # reach current node. 
                newCost = adjCost + srcCost

                # If stops is lesser than k we can move to its adjacent nodes cause we know stops will only
                # becomes equal to or stay lesser than k which is allowed.
                if stops < k:
                    # Ill only update the cost for the adjacent node if new cost is lesser.
                    if newCost < cost[adjNode]:
                        cost[adjNode] = newCost
                        queue.put([stops+1,adjNode,newCost])
                # If sotps is equal to k then adjNode should be the destination node in order to be considered.
                elif stops == k and adjNode == dst:
                    if newCost < cost[adjNode]:
                        cost[adjNode] = newCost

        # If I wasnt able to reach the destination then cost to it would be infinity so i can return -1 in that case.
        return cost[dst] if cost[dst] != inf else -1   