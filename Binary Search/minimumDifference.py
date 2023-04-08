# In this question you are given a sorted array and a key 
# value and you need to find the element inside of your
# array which gives the minimum absolute difference when
# divided by the key.

# Points To Know Observer:

# 1) If the key itself is present in our array then we can 
# return the key itself cause its going to give us the 
# minimum difference of zero 

# 2) If the key itself is not present then its possible
# neighbours that would be there if it did exist would be the
# candidates to give us the minimum difference cause they
# are closest to the given key.

# How To Solve:

# Its pretty simple cause since its a sorted array if we run
# a simple binary search for the key and if we find it then we
# can just return itself. But if we dont end up finding it through
# our binary search then the start and end pointers will be pointng
# at the two possible neighbours of the key if it did existed in our
# array and we know these two are the next two candidates for giving
# us the minimum difference other than the key itself so whichever
# one out of the two gives us a lesser difference we return that. 

def minimumDifferenceElement(arr,key):
    
    start = 0
    end = len(arr)-1
    
    while start <= end:
        
        mid = (start+end) // 2
        
        # If we find the key itself then we know its going to give us 
        # the minimum difference so we just return that.
        if arr[mid] == key:
            return key
        # Else if mid value is greater then we wanna search in its left
        # side to find the key
        elif arr[mid] > key:
            end = mid-1
        # Else if key is greater than the mid value then we wanna search
        # on the right side of the middle index to actually find the key. 
        else:
            start = mid+1
    
    # If the loop ends without us finding an element in the array equal
    # to the key we end the loop.
    
    # But now my end and start pointers are pointing at the possible
    # neighbours of key if it did existed in our array and we know these
    # are next two candidates that can give us the minimum difference
    # against key if key is not present
    
    # Im returning the one which is returning the minimum difference 
    if (arr[start] - key) < (arr[end] - key):
        return arr[start]
    else:
        return arr[end]
    
print(minimumDifferenceElement([6,12,15,20],5))
        
        
        
        
        
    
    
    
    
    
    
    
    



