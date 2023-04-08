# Brute Force 

# Space Complexity: O(n)
# Time Complexity: O(n)

def alternate(arr,l):

    positive = list()
    negative = list()
    result = list()

    for num in arr:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)
    
    i = 0
    p = len(positive)
    n = len(negative)

    while i < p and i < n:
        result.append(positive[i])
        result.append(negative[i])
        i+=1

    if i < p:
        while i < p:
            result.append(positive[i])
            i+=1
    
    if i < n:
        while i < n:
            result.append(negative[i])
            i+=1
    
    return result

# print(alternate([9,4,-2,-1,5,0,-5,-3,-5,-7],8))

# Unordered Solution

# Space Complexity: O(1)
# Time Complexity: O(n)

def alternateI(arr,n):

    i = 0

    for j,num in enumerate(arr):
        if num >= 0:
            temp = arr[i]
            arr[i] = num
            arr[j] = temp
            i+=1    
            
    j = 1
    while j < n and i < n:
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        i+=1
        j+=2

    return arr
# print(alternateI([9,4,-2,-1,5,0,-5,-3,-7,3,45,3,2,],13))

# Ordered Solution

# Time Complixity: O(n)
# Space Complexity: O(1)

def rearrange(arr, n):
        
        # Linearly Traversing in the array
        for i in range(n):
            # First making the check for the even index 
            if i%2 == 0:
                # At even index we should have positive values if we dont then 
                # we need to find the first positive element from this current 
                # spot and right rotate it to this index to make sure we have the
                # right value at the right spot
                if arr[i] < 0:
                    # Pointer that im going to traverse to find the first positive
                    # element 
                    j = i+1 
                    while j < n and arr[j] < 0:
                        j+=1
                    # If while finding the positive element i had gone out of 
                    # bound then that means that there no positive elements 
                    # left to place at this index so i come out of the 
                    # loop
                    if j >= n:
                        break
                    # Or else i right rotate the element at j index to the i index
                    for x in reversed(range(i+1,j+1)):
                        temp = arr[x-1]
                        arr[x-1] = arr[x]
                        arr[x] = temp
            else:
                # At odd index we should have negative values if we dont then 
                # we need to find the first negative element from this current 
                # spot and right rotate it to this index to make sure we have the
                # right value at the right spot. 
                if arr[i] >= 0:
                    # Pointer that im going to traverse to find the first negative
                    # element
                    j = i+1
                    while j < n and arr[j] >= 0:
                        j+=1
                    
                    if j >= n:
                        break
                    
                    for x in reversed(range(i+1,j+1)):
                        temp = arr[x-1]
                        arr[x-1] = arr[x]
                        arr[x] = temp
        return arr
print(rearrange([3,1,-2,-5,2,-4],6))