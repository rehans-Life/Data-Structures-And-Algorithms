# Optimal Approach

# Time Comlpexity: O(n+m)
# Space Complexity: O(1)

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        
        r = len(grid)
        c = len(grid[0])

        positive_cells = 0

        i = 0
        j = len(grid[0]) - 1 

        while i < r and 0 <= j:            
            if grid[i][j] >= 0:
                positive_cells += (j+1)
                i+=1
            else:
                j-=1
        
        return (r*c) - positive_cells