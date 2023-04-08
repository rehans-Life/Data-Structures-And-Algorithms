from typing import List

class DisjointSet:
    
    def __init__(self,V):
        
        self.size = [1] * V
        self.par = [i for i in range(V)]
    
    def findParent(self,node):
        
        if self.par[node] == node:
            return node
        
        ultimateParent = self.findParent(self.par[node])
        
        self.par[node] = ultimateParent
        
        return ultimateParent
    
    def union(self,u,v):
        
        pu = self.findParent(u)
        pv = self.findParent(v)
        
        if pu == pv: return
        
        if self.size[pv] > self.size[pu]:
            self.par[pu] = pv
            self.size[pv]+=self.size[pu]
        else:
            self.par[pv] = pu
            self.size[pu]+=self.size[pv]

class Solution:
    def numOfIslands(self, rows: int, cols : int, operations : List[List[int]]) -> List[int]:
        
        k = len(operations)
        delRow = (-1,+1,0,0)
        delCol = (0,0,+1,-1)
        
        # A visited matrix marked whenever we place a land on a cell
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        # A counter for the islands as well
        islands = 0
        
        disjointSet = DisjointSet(rows*cols)
        
        # An array to store the number of islands at each operations.
        ans = [0 for _ in range(k)]
        
        for i in range(k):
            
            row,col = operations[i]
            
            # If the cell already visited then continue by setting the current islands as its count
            if visited[row][col]:
                ans[i] = islands
                continue
            
            # Calculating the node value of the current cell
            node = row*cols + col
            
            # Marking the cell as visited to denote that ive placed a land
            # there.
            visited[row][col] = True
            
            # Considering the new land as an individual island and 
            # incrementing for it.
            islands+=1
            
            # Then checking if there are islands in its four directions to 
            # which i can connect this node too 
            for j in range(4):
                
                adjRow = row + delRow[j]
                adjCol = col + delCol[j]
                
                adjNode = adjRow*cols + adjCol
                
                # If its visited then there is a island on the adjancent node
                if adjRow >= 0 and adjRow < rows and adjCol >= 0 and adjCol < cols and visited[adjRow][adjCol]:
                    
                    ultimateParent = disjointSet.findParent(node)
                    
                    # If there is an island then i need to also check are
                    # they two different island with common sides if they
                    # are then connect or else leave.
                    
                    # I will check that via the ultimate parents
                    if ultimateParent != disjointSet.findParent(adjNode):
                        disjointSet.union(node,adjNode)
                        
                        # Since an island just combined with another island
                        # now hence that island doesnt exist anymore so 
                        # decrement island count
                        islands-=1
            
            # After combining the islands i can set the current island count to be the number of islands present after 
            # performing the operation
            ans[i] = islands
        
        return ans
            