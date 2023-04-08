from typing import List

class Solution:
    
    def dfs(self,node,parent,step,lowestStep,visited,steps,adj,bridges):

        # Marking the node as visited
        visited[node] = True 

        # Setting its step index to the steps taken in order to get to it
        step[node] = steps

        # Initially lowest stepped will be the node steps itself
        lowestStep[node] = steps

        # Recuse on its neighbouring nodes
        for adjNode in adj[node]:
            # Only if adjacent node is not the parent do i do something
            if adjNode != parent:
                # If its not visited then i recusrse
                if not visited[adjNode]:
                    # I know that node is going to exists at one step ahead of current step count
                    steps+=1
                    self.dfs(adjNode,node,step,lowestStep,visited,steps,adj,bridges)
                    # If the lowest stepped node to which the adjacent node can reach too is lesser
                    # than the current node steps hence not a bridge but if greater than its 
                    # bridge cause that means it cant reach back to the node.
                    if step[node] < lowestStep[adjNode]:
                        bridges.append([node,adjNode])
                
                # Comparing the lowest steps of current node with its adjacent node and accordingly updating it.
                lowestStep[node] = min(lowestStep[node],lowestStep[adjNode])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        adj = [[] for i in range(n)]

        for node1,node2 in connections:
            adj[node1].append(node2)
            adj[node2].append(node1)

        # A step array to count the steps taken in order to get to a node
        step = [0] * n

        # A lowest step array to find out the lowest stepped node to which the node can traverl too.
        lowestStep = [0] * n

        # A visited array to mark the visited nodes
        visited = [False] * n

        # A counter for steps to count the steps taken in order to get to a node
        steps = 1

        bridges = []

        self.dfs(0,0,step,lowestStep,visited,steps,adj,bridges)

        return bridges