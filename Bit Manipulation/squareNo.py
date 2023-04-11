def helper(n):

    if n == 0:
        return 0

    x = n >> 1

    if (n&1):
        return (helper(x) << 2) + (x << 2) + 1
    else:
        return helper(x) << 2

def calculateSquare(n):
    if n < 0: n = -n
    return helper(n)

def calculateSquare(n):

    if n < 0: n = -n
    
    twoPower = 0
    square = 0
    temp = n

    while temp:
        if temp&1:
            square += (n << twoPower)
        twoPower+=1
        temp = temp >> 1
    
    return square
