def commonElements(matrix,n,m):
    
    freq = dict()
    
    for row in range(n):
        for col in range(m):
            if matrix[row][col] not in freq:
                freq[matrix[row][col]] = 1
            else:
                if freq[matrix[row][col]] == row:
                    freq[matrix[row][col]]+=1
    
    return [key for key,value in freq.items() if value == n]

matrix = [
    [1, 2, 1, 4, 8],
    [3, 7, 8, 5, 1],
    [8, 7, 7, 3, 1],
    [8, 1, 2, 7, 9]
]

n = len(matrix)
m = len(matrix[0])

print(commonElements(matrix,n,m))