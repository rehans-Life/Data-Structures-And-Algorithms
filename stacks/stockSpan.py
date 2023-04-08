def stockSpan(arr):
    
    n = len(arr)
    
    # Maintaning a stack to find the nearest greater element on the left af a element inside of the 
    # array.
    stack = list()
    
    # Ouput array which is going to store the number of elements which are less than or equal to a given element
    # including itself
    ouput = list()
    
    for i in range(n):
        
        # When stack is empty
        if len(stack) == 0:
            ouput.append(i+1)
        
        # When the top element in my stack is greater than my ith element
        elif arr[stack[len(stack)-1]] > arr[i]:
            ouput.append(i - stack[len(stack)-1])
        
        # When the top element is smaller than the ith element
        else:
            
            while len(stack) > 0 and arr[stack[len(stack)-1]] <= arr[i]:
                stack.pop()
            
            if len(stack) == 0:
                ouput.append(i+1)
            else:
                ouput.append(i - stack[len(stack)-1])
        
        stack.append(i)
    
    return ouput

print(stockSpan([10,4,5,90,120,80]))