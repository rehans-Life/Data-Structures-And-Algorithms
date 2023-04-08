matrix = [
    [5,11,12,20],
    [6,11,16,21],
    [10,16,20,23],
    [15,22,24,25]
]

def sorted2dSearch(matrix,num):
    n = len(matrix)
    m = len(matrix[0])
    # Setting up to pointers to start traversing the matrix
    # from the top right.
    row = 0
    col = m-1
    
    while row >= 0 and row < n and col >= 0 and col < m:
            
        if matrix[row][col] == num:
            return (row,col)
        elif matrix[row][col] < num:
            row+=1
        else:
            col-=1
    
    return -1        

print(sorted2dSearch(matrix,10))