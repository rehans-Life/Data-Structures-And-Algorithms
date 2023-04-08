from typing import List
def nearestSmaller(arr: List[int]):
    
    n = len(arr)
    
    stack = list()
    
    output = [0] * n
    
    for i in reversed(range(n)):
        
        if len(stack) == 0:
            output[i] = -1
        elif stack[len(stack)-1] < arr[i]:
            output[i] = stack[len(stack)-1]
        else:
            while len(stack) and stack[len(stack)-1] >= arr[i]:
                stack.pop()
            
            if len(stack) == 0:
                output[i] = -1
            else:
                output[i] = stack[len(stack)-1]

        stack.append(arr[i])
    
    return output
        
print(nearestSmaller([2,5,2,3,1,8,7]))