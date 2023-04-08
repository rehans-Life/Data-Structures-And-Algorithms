class NQueues:
    
    def __init__(self,size,k) -> None:
        # This array is going to store the values within the queue
        self.arr = [0] * size
        # This array stores the indexes of the front elements of each queue.
        # This gets updated as elements are popped from the front of the queue.
        self.front = [-1] * k
        # This array stores the indexes of the rear elements of each queue
        # It gets updated as an element is added onto a queue
        self.rear = [-1] * k
        # If the value at that index as a value in it in the array then it stores
        # the index of the next element that comes after it in the queue
        # If value is empty at this index then it stores the value of next free
        # index in the free.        
        self.next = [i+1 for i in range(size)]
        self.next[size-1] = -1 
        # An index pointer which is point at the empty index in our array
        self.freespot  = 0
        self.size = size
        
    def push(self,x: int,q :int):
        
        # Checking if the array is not full Note: If freespot is -1 then
        # array is full
        if self.freespot == -1:
            return 'Queue Overflow'
        
        # Step 1: Getting the index of the freespot where we can place 
        # the element at in the array
        index = self.freespot
        
        # Moving the freespot index pointer to the next free index after
        # the current index
        self.freespot = self.next[index]
        
        # If this is the first element being added into the queue then 
        # in the front array index of this queue it would be -1 right now
        if self.front[q-1] == -1:
            # If it is first element in the queue so in the front array
            # at this queues index i will set it equal to this index
            # cause this is the first element right now of this queue.
            self.front[q-1] = index
        else:
            # Else if the queue has started already then basically i 
            # need to make the current rear element of this queue point
            # at this element now cause there element after it now in 
            # the array
            self.next[self.rear[q-1]] = index
            
        # Since i just inserted this element into the queue hence
        # this element is the new rear element
        self.rear[q-1] = index
        
        # Actually placing the value at the index
        self.arr[index] = x
        
        # Since i just placed a value into the index therefore i need
        # to update the index value in the next array and since this
        # index is the rear of the queue therefore the value after
        # this index is none therefore we place -1 in it
        self.next[index] = -1
    
    def pop(self,q: int):
        
        # Checking the queue they are trying the delete from is empty or not
        if self.front[q-1] == -1:
            return 'Queue Is Empty'
        
        # Getting the front elements index of the queue cause we always pop first 
        # element from the queue
        index = self.front[q-1]
        
        # Moving the front index pointer to the next element in the queue
        # cause we are popping this element out
        self.front[q-1] = self.next[index]
        
        # Since this spot is empty its going to point at the next empty index
        # and be set as the current freespot within the queue
        self.next[index] = self.freespot
        
        # This index is the current freespot spot now.
        self.freespot = index
        
        ans = self.arr[index]
        
        self.arr[index] = -1
        
        return ans
        
nqueue = NQueues(8,3)
nqueue.push(5,2)
nqueue.push(10,2)
nqueue.push(15,3)
nqueue.push(20,2)
nqueue.push(30,1)
nqueue.push(35,3)
nqueue.push(15,1)
nqueue.push(12,2)
print(nqueue.pop(2))
nqueue.push(50,1)
print(nqueue.arr)