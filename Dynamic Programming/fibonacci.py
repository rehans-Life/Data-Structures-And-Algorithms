# Memoization

# Time Complexity: O(n)
# Space Complexity: O(n + n)

def fibonacci(n):
    # A dp array of size n+1 to be able to store the solutions to all
    # the subproblems.
    
    # All subproblems are marked with -1 to denote they have yet to be 
    # solved.
    
    dp = [-1] * (n+1)
    
    def f(n):
        
        # If n is 1 or 0 we already the fibnonacci no.s at those indexes
        # are 1 and 0 resp. so we just return n itself.
        if n <= 1: return n
        
        # If problem has already been solved we return the solution
        # to it via the array and not call for any more subproblems
        # to solve it again
        if dp[n] != -1: return dp[n]
        
        # If not already solved so we solve it and store its solution
        # in our dp array so that we dont solve it again
        dp[n] = f(n-1) + f(n-2)
        
        # Returning the solution to the subproblem to compute solutions
        # to other problems.
        return dp[n]
    
    return f(n)

# Tabulation

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def fib(self, n: int) -> int:

        # Covering the edge of n being 0 or 1
        if n <= 1:
            return n

        # In tablulation as well we declare an array of size n+1 so that we can store solutions to all 
        # subproblems.
        dp = [-1] * (n+1)

        # We start from solving the base cases and then go to  the actual solution in this approach

        # We know what is the fibonacci of 0 and 1 so we store it
        dp[0] = 0
        dp[1] = 1

        # And then move to the solution we start from 3 cause we already answer for 0 and 1
        for i in range(2,n+1):
            # We use the recurrence relation to compute the solution for i and store it in the dp array
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

# Space Optimisation

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def fib(self, n: int) -> int:
        
        # Edge case when n is 0 or 1 we dont have two previouses for it
        # and we know there values so we directly return.
        if n <= 1:
            return n

        # We know as per the recurrence relation in order to compute a finbonacci we need the previous
        # two so we take a bottom up approach start from 2 till n and keep shifting the variables.

        # Initially we start from 2 we know its previous two are 1 and 0
        prev2 = 0
        prev = 1

        for i in range(2,n+1):

            # We compute the ith fibonacci number via the two previous numbers stored
            curr = prev+prev2

            # Then we know in order to compute the next fibonacci number the previous is going
            # to be the current number that we found and first previous for current fibonacci number 
            # so we shift our variables accordinly
            prev2 = prev
            prev = curr
        
        # In the end our nth fibonacci number will at our first previous varible cause for n+1 where our loop
        # stopped it was the first previous for it.
        return prev