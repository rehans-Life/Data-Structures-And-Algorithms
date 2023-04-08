# A helper function which is going to find the numbers less than or
# equal the mid value 
    
# Its going to find it by going through each row and finding the 
# index smallest index whose element is greater than the mid value    

def numbersLessThanOrEqualToMid(matrix,num):
    
    count = 0
    
    for row in matrix:
        
        n = len(row)        
        start = 0
        end = n-1
        res = n
            
        while start <= end:
            
            mid = (start+end) // 2
                
            if row[mid] <= num:
                start = mid+1
            else:
                res = mid
                end = mid-1
            
        count+=(res)
        
    return count

def medianOfMatrix(matrix):
    
    # The minimum most answer that i can have considering all the test
    # cases is 1 
    start = 1
    
    # The maximum most answer that i can have considering all the test 
    # cases is 2000
    end = 2000
    
    # This is going to store the possible answers that i get
    ans = 0
    
    n = len(matrix)
    m = len(matrix[0])
    
    # A value is my possible answer when the number of elements less than
    # or equal to it in the matrix is greater or equal to half of the 
    # elements inside of the matrix without including the element itself.
    half = (n*m) // 2

    while start <= end:
            
        mid = (start+end) // 2      
        
        if numbersLessThanOrEqualToMid(matrix,mid) <= half:
            start = mid+1
        else:
            ans = mid
            end= mid-1
    
    return ans
    
matrix = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
]

print(medianOfMatrix(matrix))