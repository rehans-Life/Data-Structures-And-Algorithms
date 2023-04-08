def minMerge(arr,n):
    
    # First i maintain two pointers in the array
    # Pointer i will be placed in the start of the array.
    # Pointer j will be placed in the end of the array.
    
    # And i will start checking each of the corresponding
    # elements and see if they are equal or not.
    
    i = 0
    j = n - 1
    
    # A variable which is going to count how many merges
    # did i actually make in order to convert the array into
    # a palindrome.
    merges = 0    
    
    while i < j:
        
        # First case could be that the corresponding elements
        # are already equal hence there is no need to merge
        # anything and i will move the pointers to check
        # the next corresponding elements
        if arr[i] == arr[j]:
            i+=1
            j-=1
        
        # However if they are not equal then i need to check
        # which one is lower cause i would need to merge the 
        # lower one with its adjacent element so that there
        # is a chance it becomes equal to its corresponding 
        # element.
        elif arr[i] < arr[j]:
            arr[i+1] = arr[i] + arr[i+1]
            # Since im merging the elements i need to increment 
            # the counter
            merges+=1
            i+=1
        
        else:
            arr[j-1] = arr[j] +arr[j-1]
            # Since im merging the elements i need to increment 
            # the counter
            merges+=1
            j-=1
            
    
    return merges            
        
print(minMerge([6, 5, 6, 5, 5, 5],6))
        
        
        
        