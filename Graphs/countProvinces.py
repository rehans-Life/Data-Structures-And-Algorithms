from typing import List
class Solution:
    def dfs(self,node,isConnected,visited):
        visited[node] = True

        for i in range(len(isConnected[node])):
            if not visited[i] and isConnected[node][i]:
                self.dfs(i,isConnected,visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # A counter for provinces
        provinces = 0

        # A visited array to mark the nodes we have traversed for each province initially every
        # node is marked as False
        visited = [False] * len(isConnected)

        # Iterating through all the nodes which go from 0 to rows-1 
        for node in range(len(isConnected)):
            # If node has not been visited before therefore it means this node belongs to a completely
            # new province therefore i count it as a province and then traverse all the nodes within this
            # province marking them as visited so that if i find a new unvisited node then that means that
            # is a node from a completly different province hence i increment the count and repeat the same
            # process to find all the provinces
            if not visited[node]:
                provinces+=1
                self.dfs(node,isConnected,visited)

        # Returning the number of provinces found.
        return provinces