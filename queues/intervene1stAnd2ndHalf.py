# Your suppose to convert the queue into such 
# where the elements of the 1st half of the queue
# intervene the second half elements of the queue.

from queue import Queue

q = Queue()
q.put(11)
q.put(12)
q.put(13)
q.put(14)
q.put(15)
q.put(16)
q.put(17)
q.put(18)
q.put(19)
q.put(20)

def intervene1stAnd2ndHalf(q):
    
    stack = []
    
    half = q.qsize() // 2 
    
    # Adding the elements inside of the first half into the stack.
    while q.qsize() > half:
        stack.append(q.get())
    
    # Adding the elements of the first half back into the queue but
    # they are going to be inserted in reverse order due to the nature
    # of the stack.
    while len(stack):
        q.put(stack.pop())
    
    # Putting the elements of the first half in the back of the queue
    # again so i can insert the elements of the first half back into the
    # stack so that they can be converted into there original form 
    # again when inserted into the stack again.
    for _ in range(half):
        q.put(q.get())
        
    # Inserting the elements back into the queue so that they can be
    # converted into their original form cause previously they were 
    # converted into reverse order.
    while q.qsize() > half:
        stack.append(q.get())
        
    # Now i start intervening the corresponding elements from both the 
    # halfs in order inside of the queue
    while len(stack):
        # Taking the corresponding elements fron elements from the 1st
        # and the 2nd half and placing them in order in the back of the 
        # queue.
        q.put(stack.pop())
        q.put(q.get())

intervene1stAnd2ndHalf(q)
print([q.get() for _ in range(q.qsize())])