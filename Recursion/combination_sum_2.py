# Combination Sum II

# => [1,4,5,3]

# In this problem we have different conditions in 
# relation to our previous question.

# Our conditions here are:

#  1) We cannot reuse elements unlike last time.

#  2) We can only check the given sum for unique
#  combinations. So if there are repeating elements
#  that are going generate duplicate combinations so
#  we need to avoid these cases.

#  3) We also need only those combinations whose sum
#  is equal to the given sum.

# => [1,1,1,3,4] => i = 4
# => array[i] == array[i+1] => i = 1 
# => array[i] == array[i+1] => i = 2
# => i = 2 

# => [1,4,5,1] => [1,1,4,5]

def combinationSumII(array,k,i=0,combination=[],ans=[],sumation=0):
     
    # Sorting the array to place each repeating element
    # exist consecutively in the array.
     
    array.sort()

    # We append the combination whose sum is equal to our
    # given sum and we also stop going further down into
    # that subtree because if we go further down into this
    # subtree then we will only be appending more elements
    # into the combination which is going to increase
    # the sum so the sum of combinations that we generate by 
    # going further down into this subtree will only be 
    # greater than our given sum.
    if sumation == k:
        ans.append(combination.copy())
        return
    
    # Whenever we reach to a point where our combination
    # is generating a sumation which is greater than given
    # sum then we stop that subtree of the recursion tree
    # from expanding because we know further down we will
    # only be incrementing elements to it which is going
    # to increase the sum even more than it already is
    # Hence if we make further calls it will be pointless
    # since they will only generate combinations whose
    # sum will be higher than the given sum so we end the 
    # tree here itself.
    if sumation > k:
        return
    
    # If pointer reaches the end of the array we end
    # the function and push the current combination
    # generated to our answer.
    if i == len(array):
        return
    
    # We append the ith element inside of the combination
    # which is going to generate all possible combinations
    # for the subArray with ith element in each combination.
    combination.append(array[i])
    combinationSumII(array,k,i+1,combination,ans,sumation + array[i])

    # We keep incrementing the pointer to the point 
    # until we are the pointing towards the last instance
    # of the repeating element.
    combination.pop()
    while i < len(array) - 1 and array[i] == array[i+1]:
        i+=1  
    # Recursively calling the function this time not 
    # including the pointer element inside of our 
    # combination and also making the call while 
    # pointing towards a unique element which is not
    # equal to our previous pointer element.
    combinationSumII(array,k,i+1,combination,ans,sumation)

    return ans

print(combinationSumII([1,3,4,1],4))

def combinationSum2(arr, n, target):
    # write your code here
    ans=[]
    def helper(arr,n,target,i=0,combination=[],sumation=0):
        
        if sumation == target:
            ans.apppend(combination.copy())
            return
        
        if sumation > target:
            return
        
        if i == n:
            return
        
        #[1,5,7,1] => [1,1,1,5,7]
        arr.sort()
        
        combination.append(arr[i])
        helper(arr,n,target,i+1,combination,sumation+arr[i])
          
        combination.pop()
        while i < n-1 and arr[i] == arr[i+1]:
            i+=1
        helper(arr,n,target,i+1,combination,sumation)
       
    helper(arr,n,target)  
    return ans
print(combinationSum2([1,4,5,1],4,4))