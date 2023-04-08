def doubleHelix(arr1,arr2,n,m):
    i = 0
    j = 0
    
    maxSum = 0
    
    currSum1 = 0
    currSum2 = 0
    
    while i < n and j < m:
        
        if arr1[i] == arr2[j]:
            maxSum+=(max(currSum1,currSum2)+arr2[j])
            currSum1 = 0
            currSum2 = 0
            i+=1
            j+=1
        elif arr1[i] > arr2[j]:
            currSum2+=arr2[j]
            j+=1
        else:
            currSum1+=arr1[i]
            i+=1
    
    if i < n:
        while i < n:
            currSum1+=arr1[i]
            i+=1
        maxSum+=max(currSum1,currSum2)
    
    if j < m:
        while j < m:
            currSum2+=arr2[j]
            j+=1
        
        maxSum+=max(currSum1,currSum2)
    
    return maxSum


arr1= [5,12,16,28,36,48,58,68,72]
arr2 =[10,15,16,24,26,29,48,68,69]
print(doubleHelix(arr1,arr2,len(arr1),len(arr2)))