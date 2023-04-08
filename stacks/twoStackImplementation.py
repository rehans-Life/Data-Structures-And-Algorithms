class Stack:
    
    def __init__(self,size: int) -> None:
        
        # Initiating the array to store the elements of the stack.
        self.stack = [0] * size
        
        # top1 is going to denote the fitst stack and elements are going to be 
        # added to it from left to right.
        self.top1 = -1
        
        # top2 is going to denote the second stack and elements are going to be 
        # added to it from right to left.
        self.top2 = size
        
        self.size = size
        
    def push1(self,val: int):
        
        # Only if there is space between them we are going to insert elements into
        # it.
        if (self.top2 - self.top1) > 1:
            self.top1+=1
            self.stack[self.top1] = val
        
    def push2(self,val: int):
        
        if (self.top2 - self.top1) > 1:
            self.top2-=1
            self.stack[self.top2] = val
    
    def pop1(self):
        
        # We will only be pop the elements if there exist any.
        if self.top1 != -1:
            ans = self.stack[self.top1]
            self.top1-=1
            return ans
        else:
            return 'Underflow'
    
    def pop2(self):
        
        if self.top2 != self.size:
            ans = self.stack[self.top2]
            self.top2+=1
            return ans
        else:
            return 'Underflow'
    
    
stack = Stack(7)
stack.push1(10)
stack.push2(11)
stack.push1(5)
stack.pop2()
stack.push1(15)
stack.push2(20)
stack.push2(10)
print(stack.stack)