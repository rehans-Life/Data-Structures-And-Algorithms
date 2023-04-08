
class DisjointSet:
    
    def __init__(self,V) -> None:
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
        
        if self.size[pv] > self.size[pu]:
            self.par[pu] = pv
            self.size[pv]+=self.size[pu]
        else:
            self.par[pv] = pu
            self.size[pu]+=self.size[pv]

class Solution:
    
    def Solve(self, n, edges):
        
        ds = DisjointSet(n)
        extraEdges = 0
        components = 0
        
        for u,v in edges:
            
            if ds.findParent(u) != ds.findParent(v):
                ds.union(u,v)
            else:
                extraEdges+=1
        
        for node in range(n):
            
            if ds.findParent(node) == node:
                components+=1
        
        minEdges = components - 1
        
        if minEdges <= extraEdges:
            return minEdges
        else:
            return -1
        
ans = [224,1,23,1,3,3,]
abs2 = [22.32,2323,12,12,]
print(ans.extend(abs2))
print(ans)