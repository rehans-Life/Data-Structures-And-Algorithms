def canPartition(arr, n):

    totalSum = sum(arr)
    
    # If arrays total sum is odd then it cant divided into two subsets 
    # of equal sum why because then i cant divide the total sum into equal
    # halfs
    if totalSum % 2 != 0: return False

    # All i need to check if i can get one subset whose sum is equal to
    # half of total arrays sum then the remaining elements within the
    # array are bound to give you the other half.
    
    k = totalSum // 2

    prev = [False] * (k+1)
    prev[0] = True
    
    if arr[0] <= k: prev[arr[0]] = True

    for i in range(1,n):
        temp = [False] * (k+1)
        temp[0] = True
        for target in range(1,k+1):
            if arr[i] <= target:
                temp[target] = prev[target-arr[i]]
            
            if not temp[target]:
                temp[target] = prev[target]
        
        prev = temp
    
    return prev[k]