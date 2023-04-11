class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0): 
            sign = -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        qoutient = 0
        
        while dividend >= divisor:
            q = 0
            while dividend > (divisor << q):
                q+=1
            q = q-1 if q > 0 else q
            qoutient+=(1<<q)
            dividend-=(divisor<<q)

        qoutient = qoutient if sign == 1 else -qoutient

        if qoutient > 2147483647:
            return 2147483647
        elif qoutient < -2147483648:
            return -2147483648
        else:
            return qoutient

