# You have insert an Element at the bottom of the stack

def insertBottom(stack,num: int):
        
    # Recursive function thats going to keep removing elements until
    # the stack is empty.

    def helper():
        
        # When the stack is empty then insert the element at the bottom.
        if len(stack) == 0:
            stack.append(num)
            return 
        
        temp = stack.pop()
        helper()
        
        # If the element has been added then keep adding all the elements
        # that have been removed back into the stack.
        stack.append(temp)
    
    helper()
    return stack

print(insertBottom([2,3,4,5,6],9))