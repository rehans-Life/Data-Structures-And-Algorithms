matrix = [
    [2,3,4,10,11],
    [5,8,2,5,12],
    [6,3,1,11,13],
    [1,5,4,12,14],
    [0,5,4,12,15]
]

def rotateMatrix(matrix,n):
    
    # Our Boundrie
    
    left,right = 0, n
    top,bottom = 0, n
    
    
    while left < right and top < bottom:
        
        if top == bottom-1 and left == right-1: break
        
        for i in range(left,right-1):
                            
            temp = matrix[top][i]            
            # Is the leftmost element of the square that we need to rotate
            
            matrix[top][i] = matrix[bottom-1-(i-top)][left]
            matrix[bottom-1-(i-top)][left] = matrix[bottom-1][right-1-(i-top)]
            matrix[bottom-1][right-1-(i-top)] = matrix[top+(i-top)][right-1]
            matrix[top+(i-top)][right-1] = temp
            
        top+=1
        bottom-=1
        right-=1
        left+=1
    

rotateMatrix(matrix,len(matrix))

print(matrix)