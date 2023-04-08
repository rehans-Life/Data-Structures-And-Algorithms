def minSwaps(arr,n):
    
    swaps = 0    
    temp = list()
    
    # Storing the elements from the array into a list but this time as a pair in the index at which they are originally located at.
    for i,num in enumerate(arr):
        temp.append((num,i))
    
    # Sorting the elements from the list
    temp.sort()
    
    i = 0
    
    # Converting the sorted array back to its original form and counting how many swaps it takes to convert the array back because its 
    # going to be equal to the minimum swaps its going to take the original array to its sorted version.
    while i < n:
        originalIndex = temp[i][1]
        # If the element is in its correct position already then keep it there itself and check for other elements
        if  i != originalIndex:
            # If its not in its correct position then swap it back to its original position.
            temp[i],temp[originalIndex] = temp[originalIndex],temp[i]
            swaps+=1
        else:
            i+=1
    
    return swaps

arr = [5,9,4,3,10,1]
n = len(arr)
print(minSwaps(arr,n))