def mazeObstacles(n, m, mat):
    prev = [0] * m

    for i in range(n):
        temp = [0] * m    
        for j in range(m):
            
            if mat[i][j] == -1:
                temp[j] = 0
                
            elif i == 0 and j == 0:
                temp[j] = 1
                
            else:
                up,left = 0,0

                if i > 0: 
                    up = prev[j]

                if j > 0:
                    left = temp[j-1]
                
                temp[j] = up + left
        
        prev = temp
    
    return prev[m-1] % 1000000007