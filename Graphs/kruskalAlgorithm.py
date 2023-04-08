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
        
        # Finding the ultimate parents of both the nodes
        pu = self.findParent(u)
        pv = self.findParent(v)
        
        # If the ultimate parents is same then they are in the same component
        # so no need to do anything.
        if pu == pv: return 
        
        # If size of component from ultimate parent of u is greater than
        # ultimate parent of v's component then i need to merge the component
        # from parent of v into u and vice verse for the other case
        
        # So parent v's ultimate parent u then and the component from parent
        # v is going to get merged with parent u hence parent u's size is 
        # going to increment by parent v's components nodes.
        
        if self.size[pu] == self.size[pv]:
            self.par[pv] = pu
            self.size[pu]+=self.size[pv]
            
        elif self.size[pv] > self.size[pu]:
            self.par[pu] = pv
            self.size[pv]+=self.size[pu]
            
        else:
            self.par[pv] = pu
            self.size[pu]+=self.size[pv]

class Solution:
    
    def spanningTree(self, V, adj):
        
        edges = []
        
        for node in range(V):
            for adjNode,adjWeight in adj[node]:
                edges.append([adjWeight,node,adjNode])
        
        # Sorting the edges by weights        
        edges.sort()
        
        # A sum varaible to store the sum of all weights of mst
        sum = 0
        
        # A disjoint set to check if a nodes least weightest edge has 
        # already been considered and checking if a node is reachable by
        # other nodes.
        disjointSet = DisjointSet(V)
        
        for weight,u,v in edges:
            # Checking if the nodes already belong to the same component
            pu = disjointSet.findParent(u)
            pv = disjointSet.findParent(v)
            
            # If parent not same then i can consider this edge to be part of
            # the mst cause its the first edge to one of the nodes which is
            # also its minimum weighted edge cause edges are sorted so i 
            # connect the node to component so its reachable by every other
            # node as well.
            if pu != pv:
                sum+=weight
                disjointSet.union(u,v)
            
            # Already same component then ive already considered there minimum weighted edjes and connected them to the component
            # so ignore this edge.
            
        return sum