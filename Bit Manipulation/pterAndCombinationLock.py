class Solution:
	def AllPossibleStrings(self, d):
     
            n = len(d)
            no_of_subsets = 2**n
            grid = [[0 for _ in range(n)] for _ in range(no_of_subsets)]
            
            for i in range(0,no_of_subsets):
                    x = i
                    for ct in range(n):
                        grid[i][ct] = 1 if x&1 != 0 else 0
                        x = x>>1
		
            for i in range(0,no_of_subsets):
                end = 0
                
                for j in range(n):
                    
                    if grid[i][j] == 1: 
                        end+=d[j]
                    else: 
                        end-=d[j]
                    
                if end == 0 or end == 360: return True
            
            return False

solution = Solution()
print(solution.AllPossibleStrings([120,120,120]))