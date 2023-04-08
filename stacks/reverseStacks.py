def reverseStack(stack):

    def bottom(num):

        if not len(stack):
            stack.append(num)
            return

        temp = stack.pop()
        bottom(num)
        stack.append(temp)

    def reverse():

        if len(stack) == 1:
            return

        temp = stack.pop()
        reverse()
        bottom(temp)
    
    reverse()

    return stack

print(reverseStack([10,12,13,-3,-1,9,4,7,8,9]))