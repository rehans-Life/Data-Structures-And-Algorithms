def allMissingAndDuplicates(arr,n):
    
    i = 0
    
    while i < n:
        
        correctPosition = arr[i] - 1
        
        # If the ith element is not in its correct position then it that case we swap it with the element in the correct position
        if i != correctPosition:
            # But we only swap it with the element in its correct position only if its correct position doesnt already have the
            # correct element because if it does then this is a duplicate
            if arr[i] != arr[correctPosition]:
                arr[i],arr[correctPosition] = arr[correctPosition],arr[i]
            else:
                i+=1
        else:
            # If element is already in its correct position then we move on
            i+=1

    # Now we traverse through the sorted array and find the missing and duplicating elements
    missingNums = list()
    duplicateNums = list()
    
    for j in range(n):
        # If at the jth location we dont have the correct element then that means that element just didnt existed in the array 
        # and now since this index was empty a duplicate element was placed inside of it 
        if arr[j] != j+1:
            missingNums.append(j+1)
            duplicateNums.append(arr[j])
    
    return missingNums,duplicateNums

arr = [6,2,5,6,8,9,9,1,2]
n = len(arr)

print(allMissingAndDuplicates(arr,n))