class MinStack:

    def __init__(self):
        
        # Creating two stacks one which is going to store going to store all the elements of the stack
        self.stack = list()
        
        # This stack is going to store the minimum element out of all the elements that have been inserted
        # into the stack.
        self.minElementStack = list()

    def push(self, val: int) -> None:
        
        # Push function add element to the top of the stack.
        self.stack.append(val)
        
        # If the stack was previously empty and this is the first element thats being inserted then we insert it 
        # directly into the min element stack cause this is the minimum element at this point.
        
        # OR if the element being inserted into the stack is lesser than or equal to the current value which is on 
        # the top of the min element stack then we insert this element on the top.
        
        if not len(self.minElementStack) or self.getMin() >= val: 
            self.minElementStack.append(val)

    def pop(self) -> None:
        
        # Pop removes the top element from the top of the stack.
        elementPopped = self.stack.pop()
        
        # If that element being removed from the top of the stack is also the min element hence it would be on the top
        # of the minElementStack as well hence i remove it from top of the minElementstack as well.
        if self.getMin() == elementPopped:
            self.minElementStack.pop()

    def top(self) -> int:
        # Returns the top element.
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        # Returns teh minimum element from the stack.
        return self.minElementStack[len(self.minElementStack)-1] if len(self.minElementStack) != 0 else -1      

    def __str__(self) -> str:
        return str(self.stack)

minStack = MinStack()
minStack.push(4)
minStack.push(-4)
minStack.push(-2)
minStack.push(1)
minStack.pop()
minStack.pop()
minStack.pop()
print(minStack.getMin())