def n_queen(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    column_array = [0] * n
    left_diagonal_array = [0] * (2*n) 
    right_diagonal_array = [0] * (2*n)
    print(left_diagonal_array)
    ans=[]
    def helper(i=0):
        if i == n:
            ans.append([row.copy() for row in board])
            return
        
        for j in range(len(board[i])):
            if column_array[j] == 0 and left_diagonal_array[i+j] == 0 and right_diagonal_array[i-j+n-1] == 0:
                column_array[j] = 1
                left_diagonal_array[i+j] = 1
                right_diagonal_array[i-j+n-1] = 1
                board[i][j] = 'Q'
                helper(i+1)
                column_array[j] = 0
                left_diagonal_array[i+j] = 0
                right_diagonal_array[i-j+n-1] = 0
                board[i][j] = '.'        
    helper()
    return ans
ans = n_queen(2)

for board in ans:
    for row in board:
        print(' '.join(row))
    print('\n')