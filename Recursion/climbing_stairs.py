def countDistinctWays(nStairs: int) -> int:
    
    def helper(n,i=0):
        nonlocal counter        
        # When i equals to n thats means we have reached our nth stair so we increment
        # the counter.
        if i == n:
            counter+=1
            return
        
        # Two Decisions.
        
        # One thing to look out for one case of when we are only one step behind our 
        # nth stair so then in that case we will only give ourselves the option to take
        # one step.
        
        # 1. We take only one step from our current point
        helper(n,i+1)
        
        # 2. We take two steps from our current point
        
        # We should only be able to take two steps if we are not just one stair behind
        # our file stair
        if i < n-1:
            helper(n,i+2)
    
    #  Write your code here.
    # A counter which is going to increment everytime we reach our Nth stair
    counter = 0
    helper(nStairs)
    return counter
    
print(countDistinctWays(10))