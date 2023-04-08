# Finding the Nth index value in a fibonacci sequence.

# 0, 1, 1 ,2, 3, 5, 8, 13, 21 =>Is a fibonacci Sequence.

def fibonacci(n):

    # Base Cases on the basis of the constant
    # values in a fibonacci sequence which are 
    # at index 0 and 1.

    # Cause if they are asking us the fibonacci
    # number at index of 0 its 0 so we return 0
    
    if n == 0:
        return 0
    
    # If the person is asking for the fibonacci 
    # number at index of 1 then its 1 so we return 1.

    elif n == 1:
        return 1

    # If the index is not 0 or 1 then we use the 
    # formula to find the fibonacci number at that index   
    
# formula: fibonacci at (n - 1) + fibonacci at (n - 2)   

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))