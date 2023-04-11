class Solution:
    def countBitsFlip(self,a,b):
        count = 0
        
        while a != 0 or b != 0:
            if (a&1 == 0 and b&1 != 0) or (a&1 != 0 and b&1 == 0):
                count+=1
            
            a = a>>1
            b = b>>1
        
        return count
    
    
class Solution:
    def setSetBit(self, x, y, l, r):
        y = y>>(l-1)
        y = y<<(l-1)
        y = y&((1<<r)-1)
        return x|y