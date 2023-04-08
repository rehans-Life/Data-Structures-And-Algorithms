# To be able to place the element in its sorted position we need
# to keep the elements greater than it above and the once which
# are less than it we place them below
    
# So we keep recursively moving elements from the top until we 
# land on a element which is less than or there might not be 
# any elements which are less than it so we recurse till empty
# and then we add our number on top of the stack

def sortedInsert(stack,num):
    
    if not len(stack) or stack[len(stack)-1] <= num:
        stack.append(num)
        return
    
    # until then we keep removing elements which are greater than it
    temp = stack.pop()
    sortedInsert(stack,num)
    stack.append(temp)

def sortStack(stack):
    
    # When stack is empty we return.
    if not len(stack):
        return
    
    # We keep popping elements from the top and recursing until
    # our stack goes empty
    temp = stack.pop()    
    sortStack(stack)
    
    # And then when we are coming back we place the elements in there
    # correct spot.
    sortedInsert(stack,temp)
    
stack = [-3,14,18,-5,30]
# sortStack(stack)
# print(stack)
