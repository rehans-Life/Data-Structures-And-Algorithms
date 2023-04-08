from typing import List

class Solution:
    # A dfs to traverse the O's connected to a O on the boundry
    def dfs(self,row,col,board,visited,n,m):

        # Marking the node we traversing as visited
        visited[row][col] = True

        # Then i need to go indept in all directions from this O if there exists O's
        # in its four directions.
        if row+1 < n and board[row+1][col] == 'O' and not visited[row+1][col]:
            self.dfs(row+1,col,board,visited,n,m)
        
        if row-1 >= 0 and board[row-1][col] == 'O' and not visited[row-1][col]:
            self.dfs(row-1,col,board,visited,n,m)
        
        if col+1 < m and board[row][col+1] == 'O' and not visited[row][col+1]:
            self.dfs(row,col+1,board,visited,n,m)
        
        if col-1 >= 0 and board[row][col-1] == 'O' and not visited[row][col-1]:
            self.dfs(row,col-1,board,visited,n,m)


    def solve(self, board: List[List[str]]) -> None:

        n = len(board)
        m = len(board[0])

        # A visited matrix to mark all the O's which are indirectly or indirectly connected
        # to a O which exists on the boundry im marking them as visited to that they cannot
        # be replaced with X
        visited = [[False for _ in range(m)] for i in range(n)]

        # Traverse the last row and first row and then first column and last column
        for col in range(m):
            # First row
            if board[0][col] == 'O' and not visited[0][col]:
                self.dfs(0,col,board,visited,n,m)
            
            # Last Row
            if board[n-1][col] == 'O' and not visited[n-1][col]:
                self.dfs(n-1,col,board,visited,n,m)
            
        for row in range(n):
            # First column
            if board[row][0] == 'O' and not visited[row][0]:
                self.dfs(row,0,board,visited,n,m)
            
            # Last column
            if board[row][m-1] == 'O' and not visited[row][m-1]:
                self.dfs(row,m-1,board,visited,n,m)

        # Then i traverse the complete n*m matrix and see if there are any nodes with value
        # O and are unvisited then those nodes are bound to be covered by complete X's
        # therefore i can change there value to X
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'O' and not visited[row][col]:
                    board[row][col] = 'X'
        
        return board



