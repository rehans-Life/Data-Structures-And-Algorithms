#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    def dfs(self,node,parent,step,lowestStep,visited,steps,adj,points):

        # Marking the node as visited
        visited[node] = True 

        # Setting its step index to the steps taken in order to get to it
        step[node] = steps

        # Initially lowest stepped will be the node steps itself
        lowestStep[node] = steps
        
        count = 0

        # Recuse on its neighbouring nodes
        for adjNode in adj[node]:
            # Only if adjacent node is not the parent do i do something
            if adjNode != parent:
                # If its not visited then i recusrse
                if not visited[adjNode]:
                    count+=1
                    # I know that node is going to exists at one step ahead of current step count
                    steps+=1
                    self.dfs(adjNode,node,step,lowestStep,visited,steps,adj,points)
                    # If the lowest stepped node to which the adjacent node can reach too is lesser
                    # than the current node steps hence not a articulation node but if greater than or equal to then
                    # articulation node cause that means it cant reach back to the node.
                    if step[node] <= lowestStep[adjNode] and parent != -1:
                        points.add(node)
                
                    # Comparing the lowest steps of current node with its adjacent node and accordingly updating it.
                    lowestStep[node] = min(lowestStep[node],lowestStep[adjNode])
                else:
                    # If its adjacent node is visited hence it can possibly be removed in the future so this node cant
                    # above it at max it can go to it itself so i compare lowest of current node to that adjacent node
                    lowestStep[node] = min(lowestStep[node],step[adjNode])
        
        if parent == -1 and count > 1:
            points.add(node)
    
    def articulationPoints(self, V, adj):
        
        # A step array to count the steps taken in order to get to a node
        step = [0] * V

        # A lowest step array to find out the lowest stepped node to which the node can traverl too.
        lowestStep = [0] * V

        # A visited array to mark the visited nodes
        visited = [False] * V

        # A counter for steps to count the steps taken in order to get to a node
        steps = 1

        points = set()

        self.dfs(0,-1,step,lowestStep,visited,steps,adj,points)
        
        points = list(points)

        points.sort()

        return points if len(points) > 0 else [-1]