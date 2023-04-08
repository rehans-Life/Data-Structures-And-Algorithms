def validParentheses(s: str):
    
    # Stack is going to store the all the opening paretheses
    # inside of our string and when they are closed by there 
    # corresponding closing bracket we remove it from the stack
    # because i know the next bracket needs to be closed
    stack = []
    
    # A hashmap to map all closing brackets to there corresponding
    # opening brackets
    dic = {
        '}':'{',
        ')':'(',
        ']':'['
    }
    
    # Then iterating through each parentheses in the map
    for i in range(len(s)):
        char = s[i]
        
        # if current parentheses is a opening parentheses then i add
        # to the top of the stack.
        if char == '[' or char == '{' or char == '(':
            stack.append(char)
        else:
            
            # If the first character is a closing parentheses itself
            # then the string is invalid because a closing should come
            # after the opening parentheses
            if len(stack) == 0:
                return False
    
            # If it is a closing parentheses then it should be of the
            # same type of opening parentheses which is on the top of
            # the stack.
            if stack[len(stack)-1] == dic[char]:
                # If the they are of the same type then i can remove
                # the opening parentheses from the top of the stack
                # because i've successfully closed it right.
                stack.pop()
            else:
                # If they are not of the same type then im not closing
                # the correct parentheses hence that means that string
                # is not valid since the opening parentheses is not 
                # being closed by the correct closing parentheses
                # therefore the string is not valid
                return False
            
    # It could also end up happening that we only had opening parentheses
    # in our string and we just added them to the stack and ended the 
    # loop In that case also the string is invalid cause every opening 
    # parentheses should be closed by a corresponding closing parentheses    
    
    # In case when every opening parentheses was closed by its corresponding
    # closing parentheses of same type then the stack would empty
    # If a opening was left out then it wouldnt and we know then the string
    # is invalid
    if len(stack) == 0:
        return True
    else:
        return False
        
print(validParentheses('[][]'))