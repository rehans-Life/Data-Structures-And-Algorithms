# You have to find the nearest smallest element on the left of a certain element in the array

def nearestSmaller(arr):
    
    # A stack which is going to store all useful elements on the left of an element in it
    stack = list()
    
    # An output array which is going to the nearest smaller element on the left of an element at
    # that elements index in the array
    output = list()
    
    for num in arr:
        
        # If the stack is empty then there no elements on the left of the element
        if len(stack) == 0:
            output.append(-1)
            
        # If the top element of the stack is less than current element then its the nearest integer
        # smaller to this number.
        elif stack[len(stack)-1] < num:
            output.append(stack[len(stack)-1])
            
        # If the element is greater then keep removing elements until the top element is lesser than the
        # current element then that would be your asnwer 
        
        # You might also find no elements to be less than so in that case your stack goes empty and hence
        # in that case you can append -1.
        else:
            while len(stack) > 0 and stack[len(stack)-1] >= num:
                stack.pop()
                
            if len(stack) == 0:
                output.append(-1)
            else:
                output.append(stack[len(stack)-1])

        stack.append(num)
    
    return output
    
print(nearestSmaller([2,5,2,3,1,8,7]))