
# Union By Rank

class DisjointSet:
    
    def __init__(self,n) -> None:
        
        self.rank = [0] * n
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
        
        # If ultimate parent is same then that means there already in the same component there is nothing to 
        # connect
        if pu == pv: return 
        
        if self.rank[pu] == self.rank[pv]:
            self.par[pv] = pu
            self.rank[pu]+=1
            
        elif self.rank[pu] > self.rank[pv]:
            self.par[pv] = pu  
            
        else:
            self.par[pu] = pv
            
ds = DisjointSet(9)
ds.union(6,8)
ds.union(5,7)
ds.union(3,8)

if ds.findParent(3) == ds.findParent(7):
    print('Same Component')
else:
    print('Not Same Component')    

if ds.findParent(8) == ds.findParent(3):
    print('Same Component')
else:
    print('Not Same Component')

ds.union(3,7)
ds.union(2,4)
ds.union(2,7)

if ds.findParent(4) == ds.findParent(7):
    print('Same Component')
else:
    print('Not Same Component')

ds.union(1,4)

# Union By Rank

class DisjointSet:
    
    def __init__(self,n) -> None:
        
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
        
        # If ultimate parent is same then that means there already in the same component there is nothing to 
        # connect
        if pu == pv: return 
        
        if self.size[pu] == self.size[pv]:
            self.par[pv] = pu
            self.rank[pu]+=self.size[pv]
            
        elif self.size[pu] > self.size[pv]:
            self.par[pv] = pu  
            self.rank[pu]+=self.size[pv]
            
        else:
            self.par[pu] = pv
            self.rank[pv]+=self.size[pu]         
