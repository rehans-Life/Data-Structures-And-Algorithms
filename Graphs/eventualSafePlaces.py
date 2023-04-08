from typing import List
class Solution:
    def dfs(self,node,path,visited,safeNodes,graph):

        # Marking the node im traversing as visited and its also within my path so im including it in my path as well.
        visited[node] = True
        path[node] = True

        # Then going in dept into all of its unvisited path
        for neighbour in graph[node]:
            # In case when the neighbour is only visited we go dont in dept cause we arleady know there
            # isnt a cycle there.

            # In case when neighbour is not visited then i can go in dept to search for a cycle
            if not visited[neighbour]:
                # If a path finds a cycle then it returns a true hence this node is also part of a cycle
                # hence i can return True as well
                if self.dfs(neighbour,path,visited,safeNodes,graph):
                    return True
            # If its visited as well as its in my path then i have detected a cycle
            elif path[neighbour]:
                return True
            
        # If the none of the paths find a cycle hence there is no path from this node which connects to a 
        # cycle which means i can return a False as well as include the node as a safe node
        safeNodes.append(node)
        
        # Its no longer going to be in my path so i remove it from there.
        path[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)

        # An array to keep track of the visited node in my grpah
        visited = [False] * n

        # An array to keep track of the visited nodes within the path im currently traversing
        pathVisited = [False] * n

        # An array to store our safeNodes
        safeNodes = []

        # The graph could be divided into connected components hence i need to traverse all the nodes
        # values in order to traverse all the components
        for i in range(n):
            # If the node is not visited hence its part of a component i havent visited so i need
            # ot traverse it and find the safe nodes in it
            if not visited[i]:
                self.dfs(i,pathVisited,visited,safeNodes,graph)
        
        # Sorting the safe nodes in ascending order
        safeNodes.sort()
        return safeNodes
