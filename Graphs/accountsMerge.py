from typing import List

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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]: 

        n = len(accounts)

        # A disjoint set to connect the accounts of the same person into one components.
        disjointSet = DisjointSet(n)

        # A map to map the emails to there account numbers.
        map = dict()

        # Iterating through all acounts.
        for i in range(n):
            m = len(accounts[i])
            # Going through all there emails and mapping them to there account number.
            for j in range(1,m):
                email = accounts[i][j]
                if email not in map:
                    map[email] = i
                else:
                    # If the email is already mapped to a another account number then combine these
                    # two accounts into one so that they can be merged together.
                    disjointSet.union(map[email],i)

        merge = [[] for i in range(n)]

        # Adding the emails to the ultimate parents of their account numbers
        for email,accNum in map.items():
            ultimateParent = disjointSet.findParent(accNum)
            merge[ultimateParent].append(email)
        
        ans = []

        # And then sorting the emails and combining it with the names as well to get the complete answer  
        for accNum,emails in enumerate(merge):
            if len(emails):
                emails.sort()
                mergedAccount = [accounts[accNum][0]]
                mergedAccount.extend(emails)
                ans.append(mergedAccount)

        return ans
