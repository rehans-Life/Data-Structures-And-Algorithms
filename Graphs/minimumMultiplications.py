from typing import List
from queue import Queue
from math import *

class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        
        # A queue to insert the node along with the steps taken from source 
        # in order to get to it so i can calculate its adjacent nodes distances
        # as well from the source.
        queue = Queue()
        
        # A distance array to store the distance taken in order to get to 
        # each node and we know the nodes are only going to be valued from
        # 0 to 99,999 cause of mod
        distance = [inf] * 100000
        
        # Then we know initially we have to start from the start number to
        # as source to which the steps to get to is 0
        distance[start] = 0
        
        # And since we know the distance to start hence we can find its 
        # adjacent nodes distance as well so i insert it into the queue
        queue.put([0,start])
        
        while not queue.empty():
            
            srcDistance,node = queue.get()
            
            # Its adjacent nodes will be at a distance of one more than
            # what there parent node is from the source
            adjDistance = srcDistance + 1
            
            # Then it adjacent nodes will the output that we get for this
            # number when we multiply it by the numbers in the array
            for num in arr:
                
                adjNode = (num * node) % 100000
                
                # Only if this distance from the adjacent node is smaller 
                # then smaller then insert it into the queue to find its
                # adjacent nodes distances and set the distance in the array
                if adjDistance < distance[adjNode]:
                    
                    # If we find the adjNode to be the end number then 
                    # we return cause we know first instance of it is going
                    # to require the minimum steps.
                    if adjNode == end:
                        return adjDistance
                    
                    distance[adjNode] = adjDistance
                    queue.put([adjDistance,adjNode])
            
        return -1