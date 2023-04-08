# The idea behind a descending binary search is that this time during
# division we need to remember that the numbers are arranged in the array
# in descreasing order so from greatest to smallest.

def descendingBinarySearch(arr,n,num):
    
    # We are setting up two pointers for denoting the range we are 
    # searching in currently.
    start = 0
    end = n-1
    
    while start <= end:
        
        # We need to calculate our mid index in the range that we 
        # are searhing in currently.
        mid = (start+end) // 2
        
        # Checking if our mid indexed number is equal to the 
        # number we sreaching for.
        if arr[mid] == num:
            return mid

        elif arr[mid] < num:
            # If the number we are searching for is greater than the 
            # middle indexed number than that means that the number lies
            # on the left of the middle index in the array why because
            # in a descending sorted array the numbers greater than 
            # the middle number will be on its left side so now we shrink
            # our range on to that portion of the array and for that
            # we need to bring our end pointer to that portions end 
            # and then we apply the same operation on that portion as well.
            end = mid-1
        else:
            # If the number we are searching for is less than our current            
            # range's middle number that means it could exists on its 
            # right side since the array is sorted array in descending
            # order hence numbers less than our current middle exists
            # right side hence we would apply our search on that part
            # of the array
            start = mid+1
            
    return -1
print(descendingBinarySearch([40,39,21,19,15,11,11,7,5],9,19))        
             