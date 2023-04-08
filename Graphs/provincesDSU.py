
class DisjointSet:
    def __init__(self,V,par) -> None:
        self.size = [1] * V
        self.par = par
    
    def findParent(self,node) -> int:
        
        if self.par[node] == node:
            return node
            
        ultimateParent = self.findParent(self.par[node])
        
        self.par[node] = ultimateParent
        
        return ultimateParent
    
    def union(self,u,v):
        
        pu = self.findParent(u)
        pv = self.findParent(v)
        
        # if parents same then already connectec
        if pu == pv: return
    
        if self.size[pu] == self.size[pv]:
            self.par[pv] = pu
            self.size[pu]+=self.size[pv]
        
        elif self.size[pu] > self.size[pv]:
            self.par[pv] = pu
            self.size[pu]+=self.size[pv]
        
        else:
            self.par[pu] = pv
            self.size[pv]+=self.size[pu]
    
        
class Solution:
    def numProvinces(self, adj, V):
        
        edges = []
        
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1:
                    edges.append([i,j])
                    
        par = [i for i in range(V)]
        ds = DisjointSet(V,par)
        
        for u,v in edges:
            ds.union(u,v)
        
        provinces = 0
        
        for node in range(V):
            if par[node] == node:
                provinces+=1
        
        return provinces