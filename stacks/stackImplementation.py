class Stack:
    def __init__(self,size: int) -> None:
        
        self.stack = [0] * size
        self.top = -1
        
    def push(self,val: int):
        
        if self.top == len(self.stack) - 1: 
            return 'Stack Overflow'
        
        self.top+=1 
        self.stack[self.top] = val
        
    def pop(self):        
        if self.top == -1:
            return 'Underflow'
        else:
            ans = self.stack[self.top]
            self.top-=1
            return ans
    
    def getTop(self):
        
        if self.top == -1:
            return 'Stack Empty'
        else:
            return self.stack[self.top]

stack = Stack(5)
stack.push(12)
stack.push(9)
stack.push(1)
stack.push(1)
stack.push(14)
print(stack.push(23))
print(stack.getTop())