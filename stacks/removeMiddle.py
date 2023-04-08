def removeMiddle(stack):
    
    n = len(stack)
    
    tempStack = list()
    
    mid = n // 2
    
    for _ in range(mid+1,n):
        tempStack.append(stack.pop())
    
    stack.pop()
    
    for _ in range(len(tempStack)):
        stack.append(tempStack.pop())
        
    return stack

print(removeMiddle([4,2,9,5,3]))

print('()' == '()') # => '()' => '()'
print('[)' == ')[')