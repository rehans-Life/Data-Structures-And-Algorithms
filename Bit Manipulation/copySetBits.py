class Solution:
    def setSetBit(self, x, y, l, r):
        
        for i in range(l-1,r):
            if y&(1<<i):
                x = x|(1<<i)
        
        return x