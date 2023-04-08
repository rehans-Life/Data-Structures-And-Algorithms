class MyCircularDeque:

    def __init__(self, k: int):

        self.deque = [0] * k
        # Initially since no elements have been inserted therefore both index pointers are at
        # -1
        self.front = -1
        self.rear = -1
        self.size = k

    def insertFront(self, value: int) -> bool:

        # Insert Front is when i want to insert a element infront of my current element which is at the front
        # of the queue

        # If my queue is full then i can insert in the front.
        if self.isFull():
            return False
        
        # First case could be that im pushing the first element inside of the queue using this method
        # then we just move pointers to 0th index
        if self.front == -1:
            self.front = self.rear = 0
            self.deque[self.front] = value
        
        # If my front is at the 0th index and im trying to add an element infront of my current front
        # index then basically i will add it in the end of the array due to the cyclic nature of the
        # queue
        elif self.front == 0:
            self.front = self.size - 1
            self.deque[self.front] = value

        # Then last case is when my front is in the middle then i move it backwards and place it there
        else:
            self.front-=1
            self.deque[self.front] = value
        
        return True
        

    def insertLast(self, value: int) -> bool:

        # Insert last is for inserting the element at the rear/end of the queue
        
        # If queue is full then we cant insert 
        if self.isFull():
            return False

        # We are inserting the first element of the queue when our pointers are initialized at -1
        if self.rear == -1:
            self.rear = self.front = 0
            self.deque[self.rear] = value
        
        # We are inserting an element while our rear is at the last index then in that case we take
        # our index pointer at 0th index and place our element cause our queue is circular
        elif self.rear == self.size-1:
            self.rear = 0
            self.deque[self.rear] = value
        
        # Else our rear is somwhere in the middle so we just increment it and place our value there
        else:
            self.rear+=1
            self.deque[self.rear] = value

        return True

    def deleteFront(self) -> bool:

        if self.isEmpty():
            return False

        # First case is when there is only one element in the queue and we are deleting it
        if self.rear == self.front:
            self.rear = self.front = -1
        
        # When we are deleting when our front is at the last index
        elif self.front == self.size - 1:
            self.front = 0

        # Normal case is when our front is at middle index in our array then we can incrment and move on.
        else:
            self.front+=1

        return True
        

    def deleteLast(self) -> bool:
        
        # We deleting the last element from the queue or we are deleting from the rear of the queue
        
        # If queue empty then we cant remove
        if self.isEmpty():
            return False

        # There could be only one element inside of the queue and we are deleting it so we initialize our 
        # pointers back to -1
        if self.rear == self.front:
            self.rear = self.front = -1
        
        # Our rear could be at the 0th index and we are removing it then in that case we bring it back to 
        # n-1 cause thats where the cycle continues from.
        elif self.rear == 0:
            self.rear = self.size-1
        
        # Normal case is where rear is somewhere in the middle and we can safely move it backwards 
        else:
            self.rear-=1

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.front]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.rear]

    def isEmpty(self) -> bool:
        # If our index pointers are at -1 then queue is empty
        if self.front == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:

        # When front is at the 0th index while rear is at the last index then that means
        # the queue is full and we cant insert any more elements into it

        # Also since the queue is cyclice when my rear is directly behind my front pointer
        # then our queue is full as well.

        if (self.front == 0 and self.rear == self.size - 1) or self.rear == self.front-1:
            return True
        else:
            return False
