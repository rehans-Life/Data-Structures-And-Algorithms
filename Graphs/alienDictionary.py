#User function Template for python3
from string import *

class Solution:
    # Our dfs topo sort function
    def dfs(self,node,adj,stack,visited):
        
        # I need to mark the node im traversing as visited
        visited[node] = True
        
        # Then i wanna include its adjacent nodes first into the stack
        # before I include it into the stack so that its on top of them
        # in the stack and hence exists before them in the ordering
        for neighbour in adj[node]:
            # Only if the neighbour is not visited i recurse cause
            # if visited then that means its already in the stack
            if not visited[neighbour]:
                self.dfs(neighbour,adj,stack,visited)
                
        # After i have included all of its neighbours i add the current
        # node on top of them so it comes before them in the ordering.
        stack.append(node)
    
    def findOrder(self,dict, N, K):
        adj = [[] for _ in range(K)]
        
        # So we are going to check each pair of words within our sorted
        # dictionary and check why a word exists before the other 
        # by finding their differentiating characters and findng
        # which character exists before the other in the alien
        # alphabatical order and then creating a edge from that
        # character to the other in our adjacency list
        for i in range(N-1):
            # Extracting the consecutive words
            word1 = dict[i]
            word2 = dict[i+1]
            
            n = len(word1)
            m = len(word2)
            
            smaller = n if n < m else m
            # So basically in order to find the differentiating 
            # characters we need to find the first unequal characters
            # between the words and we wanna traverse the smaller words
            # length to them
            for j in range(smaller):
                if word1[j] != word2[j]:
                    # Then i know that word1 exists before word2 only
                    # because its differentiating character exists 
                    # before word2's in the alien alphabetical order.
                    # So i will create a directed edge between them
                    adj[(ord(word1[j]) - ord('a'))].append((ord(word2[j]) - ord('a')))
                    # Then i break out to check the next pair of words
                    break
        
        # A stack to store our alien alphabetical order of the k 
        # alphabets
        stack = []
        
        # A visited array so that we dont include the same node again 
        # in our topological ordering
        visited = [False] * K
        
        # So i need to traverse all the connected components so i 
        # traverse all characters
        for node in range(K):
            # Only if the node isnt visited then i wanna call dfs for
            # cause that means its a part of a component which i havent
            # traversed yet.
            if not visited[node]:
                self.dfs(node,adj,stack,visited)
        
        # After the dfs we have our alien alphabetical ordering in our 
        # stack but in numeric form so i start popping nodes from top
        # of the stack and convert them into the character they 
        # represent and add them to the answer
        ans = []
        
        while len(stack):
            num = stack.pop()
            # Converting the number into its character form
            char = ascii_lowercase[num]
            # Appending the character into our answer
            ans.append(char)
        
        # Then returning the answer
        return ans
    
solution = Solution()
dict = ['baa','abcd','abca','cab','cad']
ans = solution.findOrder(dict,len(dict),4)
print(ans)