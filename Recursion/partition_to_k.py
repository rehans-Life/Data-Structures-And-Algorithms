# Partition to K equal sum subsets.

def partition(arr,k):

    # If its not possible to generate k number of subsets
    # of equal sum for an array we return automatically
    # return false and we can determine that by checking
    # if the sum is completely divisible ky k or not
    
    if sum(arr) % k != 0:
        return False

    # The sum that a subset should have in order to be
    # considered as a valid subset of the array.
    targetSum = sum(arr) / k
    
    # Creating an array to mark and check what elements 
    # we have used up and elements have not been used
    # yet
    used = [False] * len(arr)

    def helper(arr,k,i=0,sumation=0):
        
        # If k becomes zero then that means I have 
        # generated k number of subsets whose sum
        # is equal to our targetSum
        if k == 0:
            return True 

        # If the sumation of a subset matches our target
        # sum then we make a recursive call to 
        # generate the next the subset.
        if sumation == targetSum:
            
            # Moving the pointer back to begining of the
            # array
             
            # Also setting the sumation to zero
            # since we are creating a new subset now

            return helper(arr,k-1,0,0)
        
        # If sumation exceeds target sum we stop cause
        # that means we are not creating a valid subset. 
        if sumation > targetSum:
            return False

        # If we are not able to create a valid subset
        # until our pointer reaches the end of the array
        # we return False                
        if i == len(arr):
            return False

        # Checking if the ith element has been already 
        # been used or not.

        # Cause only if i havent used it then only i 
        # can only it in the subset or else i only have
        # the option to not include it.
        if not used[i]:
            # After using the element I set that element
            # as used by setting its index value in my 
            # used array to True
            used[i] = True
            option1 = helper(arr,k,i+1,sumation+arr[i])
        
            # Calling the recursive function for not including
            # our ith element

            # Since im not including the ith element when
            # calling this recursive function i set its index
            # back to False
            used[i] = False
            option2 = helper(arr,k,i+1,sumation)
            
            # If either of them are able to generate valid
            # subsets we return True if both return false
            # we also return False
            return option1 or option2
        else:
            # In cases when we had only one choice
            # we just return whatever that one choice
            # returned to us.
            return helper(arr,k,i+1,sumation)
    return helper(arr,k)
print(partition([5,7,9],3))