class Solution:
        def ithBitSet(self,n: int, i: int) -> bool: 
            return n&(1<<i) != 0
        
        def singleNumber(self, nums):
		  
            xor = 0
            for num in nums: xor^=num
        
            i = 0
            while xor&1 == 0:
                xor = xor>>1
                i+=1
            
            res1 = 0
            res2 = 0
        
            for num in nums:
                if self.ithBitSet(num,i):
                    res1^=num
                else:
                    res2^=num
        
            return sorted([res1,res2])