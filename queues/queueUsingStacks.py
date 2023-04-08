# Approach 1:

# Time Complexity: O(n)
# Space Complexity: O(2n)

class Queue:
    def __init__(self,size):
        self.s1 = []
        self.s2 = []
        self.size = size
    
    def push(self,x: int):
        # Taking all elements of stack1 and placing them inside of stack2
        for _ in range(len(self.s1)):
            self.s2.append(self.s1.pop())
        
        # Placing the new element in the end of the stack1
        self.s1.append(x)
        
        # Bring all elements back from the stack2 to stack1
        for _ in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        
    def pop(self):
        self.s1.pop()
    
    def top(self) -> int:
        if len(self.s1) == 0: return 'Queue is Empty'
        return self.s1[len(self.s1)-1]

queue = Queue(6)
queue.push(12)
queue.push(14)
queue.push(16)
queue.push(18)
print(queue.top())

# Optimised Approach

# Amortised Time Complexity: O(1)
# Space Complexity: O(2n)

class MyQueue:

    def __init__(self):
        # Input stack is going to be used for inserting elements into the queue
        self.input = list()
        # Output stack is going to be used for performing pop operation and getting
        # top element out of the stack.
        self.output = list()

    def push(self, x: int) -> None:
        # When elements are added they added into the input stack.
        self.input.append(x)

    def pop(self) -> int:
        # In order to pop elements we will take all elements from input stack and place
        # them in output stack so we get all elements from input stack in reversed order
        # hence now the first element inserted which was in the bottom of the input stack
        # is in the top of the output stack and we can easily remove it.

        # If we already have taken elements from input stack in that case we perform operations
        # on the existing elements that we have in output stack cause they are the first inserted 
        # elements

        if len(self.output):
            # If elements already there then top element in the output stack is the first inserted element.
            return self.output.pop()
        else:
            # If elements not there then take elements from input and place them in output.
            for _ in range(len(self.input)):
                self.output.append(self.input.pop())

            # Now the first inserted element is at the top of the stack so just pop it out
            return self.output.pop()

    def peek(self) -> int:
        # If elements already there in output stack then top element is at the top of the output stack
        # cause it took elements from input stack in reversed order which means first inserted element
        # as at the top of the stack now.
        if len(self.output):
            return self.output[len(self.output)-1]
        else:
            for _ in range(len(self.input)):
                self.output.append(self.input.pop())
            return self.output[len(self.output)-1]

    def empty(self) -> bool:
        if not len(self.input) and not len(self.output):
            return True
        else:
            return False
