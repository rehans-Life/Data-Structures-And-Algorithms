def largestPowOf2(n):
        x = 0
        while ((1<<x) <= n): 
            x+=1
        
        return x-1
        

def countSetBits(n):
        def helper(n):
        
            if n == 0: return 0
            
            x = largestPowOf2(n)
            
            beforeLargestPow2Bits = (1<<(x-1)) * x if x > 0 else 0
            lastSetBitsFromPow2toN = (n - (1<<x)) + 1
            
            rest = n-(1<<x)
            remainingSetBitsTillN = countSetBits(rest)
            
            ans = beforeLargestPow2Bits + lastSetBitsFromPow2toN + remainingSetBitsTillN
            
            return ans
        
        return helper(n)