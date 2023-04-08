arr = [9,3,7,5,6,4,8,2]

def twoWayMerge(arr,start,mid,end):
    # We need to merge both the left sorted list and the right sorted list into one to merge the complete section
    A = list()
    B = list()
    
    # Getting the elements from the left sorted side and storing them in a list
    for i in range(start,mid+1):
        A.append(arr[i])
    
    # Getting the elements from the right sorted side and storing them in a list
    for j in range(mid+1,end+1):
        B.append(arr[j])
    
    # Two pointers one for list A and one for List B
    i = 0
    j = 0
    
    n = len(A)
    m = len(B)
    
    # The new list which is going to contain the merge sorted array.
    C = [0] * (n+m)
    k = 0
    
    # Running a while loop until one of the index pointers go out of there respective arrays
    while i < n and j < m:
    
    # If A of i is less than B of j then append A of i to the k empty space in our C array cause we wanna add the smaller elements 
    # first in our sorted array then increment i to point towards the next unused element in array A and vice versa for B.
        if A[i] < B[j]:
            C[k] = A[i]
            i+=1
        else:
            C[k] = B[j]
            j+=1
        # Increment k to point towards the next empty space.
        k+=1
        
    # One of the list will have remaining characters so we will add them to the array
    
    for i in range(i,n):
        C[k] = A[i]
        k+=1
    
    for j in range(j,m):
        C[k] = B[j]
        k+=1
    
    # Now we want to copy the sorted list formed from the two list into the actual array
    k = 0
    for i in range(start,end+1):
        arr[i] = C[k]
        k+=1
    

def mergeSort(arr,start,end):
    
    # Checking if there are more number of elenents than One in our current list
    if start < end:
        # If there are then we divide from the middle and recurse till we divide the list into lists of element
        mid = (start+end) // 2
        
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        
        # After we have sorted both the sides then we two way merge sort on both the lists so we can merge this complete list
        twoWayMerge(arr,start,mid,end)
        
mergeSort(arr,0,len(arr)-1)
print(arr)