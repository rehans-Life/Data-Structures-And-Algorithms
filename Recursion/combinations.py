def combinations(n :int,k :int):
    combination=[]
    ans=[]
    def helper(n,k,startingRange=1):
        if len(combination) == k:
            ans.append(combination.copy())
            return

        if startingRange > n:
            return  

        combination.append(startingRange)
        helper(n,k,startingRange+1)

        if startingRange == n and len(combination) < k:
            return

        combination.pop()
        helper(n,k,startingRange+1)
        
    helper(n,k)
    return ans

print(combinations(9,2))