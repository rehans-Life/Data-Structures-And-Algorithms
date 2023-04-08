A = [2,8,15,18,20]
B = [5,9,12,17,19,20,25]

def twoWayMerge(A,B,n,m):
    
    i = 0
    j = 0
    
    C = [0] * (n+m)
    k = 0
    
    while i < n and j < m:
        
        if A[i] < B[j]:
            C[k] = A[i]
            i+=1
        else:
            C[k] = B[j]
            j+=1
        k+=1
        
    for i in range(i,n):
        C[k] = A[i]
        k+=1
    
    for j in range(j,m):
        C[k] = B[j]
        k+=1
    
    return C

# print(twoWayMerge(A,B,len(A),len(B)))