# We basically need to find all possible combinations within the range 1 to 9 whose sumation is equal to K and there length is equal
# to N

def combinationSumIII(k,n,i=1,combination=[],ans=[],sumation=0):

    if len(combination) == k:
        if sumation == n:
            ans.append(combination.copy())
        return 
    
    if sumation > n:
        return
    
    if i == 10:
        return


    # This will find all possible combinations from range starting from 1 more than our current pointer till 9 within which '
    # the pointer value will be included in all combinations
    combination.append(i)
    combinationSumIII(k,n,i+1,combination,ans,sumation+i)

    # This will generate all possible combinations starting from range one more than the pointer value till 9 
    # Combinations generated will not have the pointer value within them.
    combination.pop()
    combinationSumIII(k,n,i+1,combination,ans,sumation)

    return ans
print(combinationSumIII(3,10))

def combinationSum3(K: int, N: int):
        
    # Write your code from here.
    ans=[]
    def helper(k,n,i=1,combination=[],sumation=0,length=0):
        
        if length == k:
            if sumation == n:
                ans.append(combination.copy())
            return
        
        if sumation > n:
            return
        
        if i == 10:
            return
        
        combination.append(i)
        length+=1
        helper(k,n,i+1,combination,sumation+i,length)
        
        combination.pop()
        length-=1
        helper(k,n,i+1,combination,sumation,length)
    
    helper(K,N)
    return ans
print(combinationSum3(3,10))