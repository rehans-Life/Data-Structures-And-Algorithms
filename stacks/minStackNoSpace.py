class MinStack:
    
    def __init__(self) -> None:
        
        self.stack = list()
        self.minElement = 0
    
    def push(self,val: int) -> None:
        
        if not len(self.stack):
            self.minElement = val
            self.stack.append(val)
            
        else:
            if self.minElement >= val:
                newVal = 2*val - self.minElement
                self.stack.append(newVal)
                self.minElement = val
            else:
                self.stack.append(val)
            
    def pop(self) -> None:
        
        if self.stack[len(self.stack)-1] <= self.minElement:
            self.minElement = 2*self.minElement - self.stack[len(self.stack)-1]
            
        self.stack.pop()    
    
    def top(self) -> int:
        
        if self.stack[len(self.stack)-1] <= self.minElement:
            return self.minElement
        else:
            return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        if not self.minElement:
            return -1
        else:
            return self.minElement
        
minStack = MinStack()
minStack.push(3)
minStack.push(-2)
minStack.push(-2)
minStack.push(-5)
minStack.pop()
minStack.pop()
minStack.pop()
minStack.pop()
print(minStack.getMin())