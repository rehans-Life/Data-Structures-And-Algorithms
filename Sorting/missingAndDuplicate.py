# Maths - Optimal 

# Space Complexity: O(1)
# Time Complexity: O(n)

def missingAnDuplicate(arr,n):
    sumArr = sum(arr)
    sqrSumArr = sum(map(lambda x: x**2,arr))
    sumRange = 0
    sqrSumRange = 0
    
    for i in range(1,n+1):
        sumRange+=i
        sqrSumRange+=(i**2)
    
    eq1 = sumRange-sumArr
    eq2 = sqrSumRange-sqrSumArr
    
    eq3 = eq2/eq1
    
    miss = (eq3+eq1) / 2
    dup = eq3 - miss
    
    return miss,dup

arr = [1,4,6,5,2,6]
n = len(arr)
print(missingAnDuplicate(arr,n))

# Swap Sort - Optimal.

# Time Complexity: O(n)
# Space Complexity: O(1)

def missingAndDuplicate(arr,n):
    
    i = 0
    
    while i < n:
        
        correctIndex = arr[i] - 1
        
        if i != correctIndex:
            if arr[correctIndex] != arr[i]:
                arr[i],arr[correctIndex] = arr[correctIndex],arr[i]
            else:
                i+=1
        else:
            i+=1
            
    for j in range(n):
        if arr[j] != j+1:
            missingNum = j+1
            duplicateNum = arr[j]
        
    return missingNum,duplicateNum
        
print(missingAndDuplicate(arr,n))