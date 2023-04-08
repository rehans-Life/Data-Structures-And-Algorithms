class Solution:
    def factorial(self, N):
        
        if N == 0:
            return N
        
        fact = 1
        
        for i in range(1,N+1):
            fact*=i
        
        return [int(digit) for digit in str(fact)]
