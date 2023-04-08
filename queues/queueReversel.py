from queue import Queue

# Approach 1

# Time Complexity: O(n)
# Space Complexity: O(n)

q = Queue()
q.put(5)
q.put(4)
q.put(3)
q.put(1)
q.put(6)
q.put(2)
q.put(6)
q.put(7)

def reverseQueue(queue):
    
    stack = list()
    
    # Take all the elements from the queue and put them in a stack
    for _ in range(queue.qsize()):
        stack.append(queue.get())
    
    # Take all elements from the stack and put them back into the queue.
    for _ in range(len(stack)):
        queue.put(stack.pop())

reverseQueue(q)

for _ in range(q.qsize()):
    print(q.get())

# Recursive Approach

# Time Complexity: O(n)
# Space Complexity : O(n) --> Stack Size in Memory.

def reverseQueueI(queue):
    
    if queue.qsize() == 1:
        return
    
    temp = queue.get()
    reverseQueue(queue)
    queue.put(temp)
    
reverseQueueI(q)

for _ in range(q.qsize()):
    print(q.get())