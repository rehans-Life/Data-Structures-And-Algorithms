def spiralMatrix(matrix):
    
    top,bottom = 0,len(matrix)
    left,right = 0,len(matrix[0])
    
    res = list()
    
    while top < bottom and left < right:
        
        for i in range(left,right):
            res.append(matrix[top][i])
        top+=1
        
        for i in range(top,bottom):
            res.append(matrix[i][right-1])
        right-=1
        
        if top == bottom or right == left: break
        
        for i in reversed(range(left,right)):
            res.append(matrix[bottom-1][i])
        bottom-=1
        
        for i in reversed(range(top,bottom)):
            res.append(matrix[i][left])
        left+=1
    
    return res

matrix = [[1,2,3,4],[2,4,5,6]]    

print(spiralMatrix(matrix))

        
