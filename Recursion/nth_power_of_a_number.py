# Raising a number x to a power of n using recursion.

def power(x,n):

#     # If we raising a number to a power of 1
#     # then in that case we would return the 
#     # same number cause any number raise to a 
#     # power of 1 is the same number itself.

    if n == 1:
        return x    

#     # If we are able to find out the number raise to
#     # the power one less than the power given as 
#     # argument and multiply the output by the same 
#     # number we can get the number raise to the power
#     # given as argument.

    return x * power(x,n-1)

print(power(5,3))

def divideAndPower(x,n):

    # If we raising a number to a power of 1
    # then in that case we would return the 
    # same number cause any number raise to a 
    # power of 1 is the same number itself.

    if n == 1:
        return x    

    middle_power = n // 2

    return divideAndPower(x,n-middle_power) * divideAndPower(x,middle_power)

print(divideAndPower(5,3))