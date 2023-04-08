def largestRectangleArea(histogram):
    
    n = len(histogram) 
    stack = list()    
    output = [0] * n
   
    for i in reversed(range(n)):
       
        if len(stack) == 0:
            output[i] = len(histogram)
            
        elif histogram[stack[len(stack)-1]] < histogram[i]:
            output[i] = stack[len(stack)-1]
            
        else:
            while len(stack) > 0 and histogram[stack[len(stack)-1]] >= histogram[i]:
               stack.pop()
               
            if len(stack) == 0:
                output[i] = len(histogram)
            else:
                output[i] = stack[len(stack)-1]
                
        stack.append(i)
            
    stack.clear()
    
    for i in range(n):
        
        if len(stack) > 0 and histogram[stack[len(stack)-1]] < histogram[i]:
            output[i]-=(stack[len(stack)-1]+1)
            
        elif len(stack) > 0 and histogram[stack[len(stack)-1]] >= histogram[i]:
            
            while len(stack) > 0 and histogram[stack[len(stack)-1]] >= histogram[i]:
                stack.pop()
                
            if len(stack) > 0:
                output[i]-=(stack[len(stack)-1]+1)
        
        stack.append(i)
        
    for i in range(n):
        output[i]*=histogram[i]
    
    return max(output)

print(largestRectangleArea([2,4]))