def findMinimumCost(s: str):
    stack = list()
    
    if len(s) % 2 != 0 : return -1 
    
    for i in range(len(s)):
        char = s[i]
        
        if char == '{':
            stack.append(char)
        else:
            if len(stack) == 0:
                stack.append(char)
            elif stack[len(stack)-1] == '{':
                stack.pop()
            elif stack[len(stack)-1] != '{':
                stack.append(char)
    a = 0
    b = 0
    
    print(stack)
    for _ in range(len(stack)):
        char = stack.pop()
        if char == '{':
            a+=1
        else:
            b+=1
    
    return (((a+1) // 2) + ((b+1) // 2))  

s = '{}{}{}}}}}}}{{{{{{{{{{{{'
print(findMinimumCost(s))