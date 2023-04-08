class DisjointSet:
    def __init__(self,n):
        self.size = [1] * n
        self.par = [i for i in range(n)]
    
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
    def removeStones(self, stones: List[List[int]]) -> int:

        n = len(stones)
        maxRow = 0
        maxCol = 0
        # In order to find the size of the 2d matrix given i need to find the maximum
        # column and the row given to us in the stones array this is so that i can create my
        # disjointSet properly
        for row,col in stones:
            maxRow = max(maxRow,row)
            maxCol = max(maxCol,col)

        disjointSet = DisjointSet((maxRow+1) + (maxCol+1))

        # Then I need to connect the rows and columns of a stone together
        for row,col in stones:
            disjointSet.union(row,(maxRow + 1) + col)

        ultParents = set()

        for row,col in stones:
            # I know the row and column of a stone have same ultimateParent so imma just get the
            # ultimateParent of the row
            ultimateParent = disjointSet.findParent(row)
            ultParents.add(ultimateParent)

        return n - len(ultParents)