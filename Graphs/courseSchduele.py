from queue import Queue
from typing import List
from string import *
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Representation of the problem as a grpah problem using adjacency list.
        adj = [[] for _ in range(numCourses)]
        for neighbour,parent in prerequisites:
            adj[parent].append(neighbour)
        
        indegrees = [0] * numCourses

        for neighbours in adj:
            for node in neighbours:
                indegrees[node]+=1

        queue = Queue()
        order = []

        for node in range(numCourses):
            if indegrees[node] == 0:
                queue.put(node)
        
        while not queue.empty():

            node = queue.get()
            order.append(node)

            for neighbour in adj[node]:
                indegrees[neighbour]-=1
                if indegrees[neighbour] == 0:
                    queue.put(neighbour)        

        return order if len(order) == numCourses else []            

print(ascii_lowercase)