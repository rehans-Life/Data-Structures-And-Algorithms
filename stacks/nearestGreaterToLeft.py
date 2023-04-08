def greaterToLeft(arr):
    
    n = len(arr)
    
    # A stack which is going to store the elements which exist on the left of a certain element.
    stack = list()
    
    # An array which is going to store the nerest greater element to a element on its left at its 
    # index 
    ouput = list()
    
    for i in range(n):
        
        if len(stack) == 0:
            ouput.append(-1)
        elif stack[len(stack)-1] > arr[i]:
            ouput.append(stack[len(stack)-1])
        else:
            while len(stack) > 0 and stack[len(stack)-1] <= arr[i]:
                stack.pop()
            
            if len(stack) == 0:
                ouput.append(-1)
            else:
                ouput.append(stack[len(stack)-1])
    
        stack.append(arr[i])
    
    return ouput

print(greaterToLeft([5,2,6,2,3,4,7]))