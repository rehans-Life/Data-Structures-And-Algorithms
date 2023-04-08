from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # A matrix to store our solution
        ans = [[image[i][j] for j in range(len(image[i]))] for i in range(len(image))]

        # Storing the starting value to identify the nodes we can traverse
        startingVal = image[sr][sc]

        # If the pixel value is already of the same color they asking us to change it too then we just return
        # the same image itself.
        if startingVal == color: return image

        def dfs(row,col):
            
            # We change the current node value to the given value then we try to find nodes which are of the 
            # same color as the starting pixel value in all 4 directions and if we do find one we go in dept
            # in that direction through recursion.
            ans[row][col] = color

            if row-1 >= 0 and ans[row-1][col] == startingVal:
                dfs(row-1,col)
            
            if row+1 < len(image) and ans[row+1][col] == startingVal:
                dfs(row+1,col)
            
            if col-1 >= 0 and ans[row][col-1] == startingVal:
                dfs(row,col-1)
            
            if col+1 < len(image[row]) and ans[row][col+1] == startingVal:
                dfs(row,col+1)
        
        dfs(sr,sc)

        return ans