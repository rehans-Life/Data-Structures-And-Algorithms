class Solution:
	def AllPossibleStrings(self, s):
            n = len(s)
            no_of_subsets = 2**n
            subsets = []
            grid = [[0 for _ in range(n)] for _ in range(no_of_subsets)]
            
            for i in range(1,no_of_subsets):
                    x = i
                    for ct in range(n):
                        grid[i][ct] = 1 if x&1 != 0 else 0
                        x = x>>1
		
            
            for i in range(1,no_of_subsets):
                subset = ""
                for j in range(n):
                    if grid[i][j] == 1:
                        subset+=s[j]
                subsets.append(subset)           
            
            return sorted(subsets)		 
