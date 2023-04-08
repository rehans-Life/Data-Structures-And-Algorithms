def sumOfNaturalNumbers(n):

   # The base case because if someone passes in the n value
   # as 1 then that would mean they are asking us whats the first
   # natural number.

    if n == 1:
        # In that case we just return one because thats the 
        # first natural number.
        return 1

    return n + sumOfNaturalNumbers(n-1)

print(sumOfNaturalNumbers(5))