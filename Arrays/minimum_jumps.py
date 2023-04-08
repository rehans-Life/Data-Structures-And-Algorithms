# Recursive Approach

# Space Complexity: O(idk)
# Time Complexity: O(n)

import math

def minJumps(arr, n):
            
            minimum_jumps = math.inf
            
            def helper(i=0,jumps=0):
                nonlocal minimum_jumps
                
                if i >= n - 1:
                    minimum_jumps = min(minimum_jumps,jumps)
                    return
                
                if arr[i] == 0:
                    return -1
                
                for j in range(1,arr[i]+1):
                    helper(i+j,jumps+1)
            
            helper()
            return minimum_jumps

print(minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9],11))

