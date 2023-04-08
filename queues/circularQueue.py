class CircularQueue:
    def __init__(self,size) -> None:
        
        self.queue = [0] * size
        # front is going to point at the front element in the array
        self.front = -1
        # rear is going to point at the last placed element inside of the array.
        self.rear = -1
        self.size = size
    
    def enqueue(self,x: int):
        
        # If front is at 0 and rear is at the last index then my queue is full 
        # And since the queue is circular when your rear is right behind your front
        # then in that case too your array is full.
        if (self.front == 0 and self.rear == self.size-1) or (self.rear == self.front-1):
            return 'Queue is Full'
        
        # This case is for when your inserting your first element
        if self.rear == -1:
            self.front+=1
            self.rear+=1
            self.queue[self.rear] = x
            
        # Case for when your adding your element and your rear is at the end of the array. 
        elif self.rear == self.size-1:
            self.rear = 0
            self.queue[self.rear] = x
            
        # last case is when your rear is somewhere in the middle
        else:
            self.rear+=1
            self.queue[self.rear] = x
            
    def dequeue(self):
        
        # If front is pointing at -1 then that means the queue is empty
        if self.front == -1:
            return 'Queue is Empty'
        
        ans = self.queue[self.front]

        # If front and rear are equal then that means your going to pop your last
        # element therefore you can reintialize your pointets back to -1 cause
        # your queue is going to empty then.
        if self.front == self.rear:
            self.front = self.reat = -1
            
        # If your front is at the last index then the next top is at the other side
        # of the array at 0th index
        elif self.front == self.size-1:
            self.front = 0
        
        # In else case its somewhere at the middle hence we can move it by one.
        else:
            self.front+=1
        
        return ans
    
circularQueue = CircularQueue(5)
circularQueue.enqueue(23)
circularQueue.enqueue(21)
circularQueue.enqueue(24)
circularQueue.enqueue(56)
circularQueue.enqueue(34) 
print(circularQueue.dequeue())
circularQueue.enqueue(36) 
circularQueue.dequeue()
circularQueue.enqueue(45)
print(circularQueue.enqueue(334))
print(circularQueue.queue)