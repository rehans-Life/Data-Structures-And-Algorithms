def twoWayMerge(A,B):
    # When the array has odd number of elements then the second array could be empty cause a consective pair wasnt formed with one of the 
    # elements so we gaurd against that case if the second array is empty we return the first sorted array itself. 
    if not B:
        return A
    
    n = len(A)
    m = len(B)
    
    # Two pointers one for array A and one for Array B
    i = 0
    j = 0
    
    # Output Array which is going to store the merge sorted lists
    C = [0] * (m+n)
    
    # K pointer to point at its empty spaces where we can insert elements inside of 
    k = 0
    
    # Running a while loop until either of the index pointers go out of there respective arrays.
    while i < n and j < m:
    
    # If A of i is smaller than B of j then we insert A of i in the kth position then we move the ith pointer to the next element
    # and vice versa for B.    
        if A[i] < B[j]:
            C[k] = A[i]
            i+=1
        else:
            C[k] = B[j]
            j+=1
    
    # Incrementing k to the point at the next empty index inside of our output array
        k+=1
        
    # There could be remaining elements at the end of the loop in either of the arrays so we run to loops two add there remaining elements
    # inside of the array,
    for i in range(i,n):
        C[k] = A[i]
        k+=1
    
    for j in range(j,m):
        C[k] = B[j]
        k+=1
    
    return C    
    
def mergeSortIterative(A):
    
    # Converting each element inside of the array into its own lists. And we know an array with one element is considered sorted
    # Therefore A now contains n number of sorted lists.
    A = list(map(lambda x: [x],A))
    
    # Running a while as long as there is more than one sorted lists inside of A 
    while len(A) > 1:
        
        # Upon each interation of this loop we will run a for loop to merge each consecutive pair of sorted lists inside of
        # our A array to bring down the number of sorted lists inside of it 
        
        # But we will store the result of the for loop in a seperate array and then set it to A cause we wanna set it to A after iterating
        # through array A completely.
        B = []
        
        
        # Since we are merging each consecutive pair hence we will take steps of two.
        for i in range(0,len(A),2):
            
            list1 = A[i]
            
            # In odd number of elements we will not be able to form a complete pair for an element
            list2 = A[i+1] if (i+1) < len(A) else []
            
            # Applying two way merge sort on each pair of sorted lists and append the results to an temp array
            B.append(twoWayMerge(list1,list2))
        
        # Updating the array in the middle of the loop can mess up our loop thats why we are storing the loop inside of our
        # temporary array and then setting it to array.    
        A = B
    
    # Returning the One sorted lists which is inside of our Array
    return A[0]
        
print(mergeSortIterative([9,3,7,5,6,4,8,2,2,10,1]))