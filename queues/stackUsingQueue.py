from queue import Queue

class Stack:
    def __init__(self) -> None:
        self.q1 = Queue()
        self.q2  = Queue()
    
    def push(self,x: int):
        
        # We first insert the element into the Queue2
        self.q2.put(x)
        
        # Then we place all elements of q1 on top of 
        # this newly inserted element in q2. 
        
        # So that it becomes the top of the Queue so that
        # the order of the stack is maintained inside of the
        # Queue.
        
        while self.q1.qsize():
            self.q2.put(self.q1.get())        
        
        # Then we bring all elements back into q1 here the 
        # last inserted element is on top of the Queue hence
        # when we pop we pop the last inserted which means
        # the order of stack is maintained.
        
        while self.q2.qsize():
            self.q1.put(self.q2.get())
        
    def pop(self) -> int:
        if self.q1.empty(): return 'Stack Underflow'
        return self.q1.get()
    
    def top(self) -> int:
        if self.q1.empty(): return 'Stack Empty'
        return self.q1

stack = Stack()
stack.push(12)
stack.push(14)
stack.push(15)
stack.push(16)
stack.push(10)
stack.push(4)
stack.push(3)
stack.push(1)
stack.push(2)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())