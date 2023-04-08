# Brute Force 

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def countInversions(arr):
    count = 0
    
    n = len(arr)
    
    for i in range(n-1):
        # Counting the inversions this element makes with other elements 
        
        # Note we are only checking the elements that are ahead of this element because an element can
        # only form an inversion with another element when its index is less than that element and its value
        # is greater than it.
        
        for j in range(i+1,n):
            # Incrementing count each time we find an inversion.
            if arr[i] > arr[j]:
                count+=1
                
    return count

# print(countInversions([8,4,2,1]))

# Writing code for reverse of finding the inversions to understant how the merge sort method works.

def reverseCount(arr):
    
    n = len(arr)
    
    count = 0
    
    for i in reversed(range(1,n)):
        for j in range(i):
            if arr[j] > arr[i]:
                count+=1
    
    return count

# print(reverseCount([2,1,5,6,4,3]))


# Optimal Approach 

# Time Complexity : O(nlong(n)))
# Space Complexity: O(n)

def twoWayMerge(arr,start,mid,end):
    
    start2 = mid+1
    
    A = []
    B = []
    
    for i in range(start,mid+1):
        A.append(arr[i])
    
    for j in range(start2,end+1):
        B.append(arr[j])
    
    i = 0
    j = 0
    
    count = 0
    
    n = len(A)
    m = len(B)
    
    C = [0] * (n+m)
    k = 0
    
    while i < n and j < m:
        
        if A[i] <= B[j]:
            C[k] = A[i]
            i+=1
        else:
            C[k] = B[j]
            count+=(n-i)
            j+=1
        k+=1
        
    for i in range(i,n):
        C[k] = A[i]
        k+=1
    
    for j in range(j,m):
        C[k] = B[j]
        k+=1
        
    k = 0
    for i in range(start,end+1):
        arr[i] = C[k]
        k+=1
        
    return count

def mergeSort(arr,start,end):
    
    if start < end:        
        
        count = 0 
        
        mid = (start+end) // 2
        
        count+=mergeSort(arr,start,mid)
        count+=mergeSort(arr,mid+1,end)
        
        count+=twoWayMerge(arr,start,mid,end)
        
        return count
    else: 
        return 0

def countInversions(arr):
    
    n = len(arr)
    start = 0
    end = n - 1
    return mergeSort(arr,start,end)
    
arr = [9,3,4,7,2,6,4,8,7,3,2]

print(countInversions(arr))
print(arr)