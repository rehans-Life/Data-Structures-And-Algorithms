def reverseKElements(queue,k):
    
    # A stack to reverse the first k elements inside of the queue
    stack = list()
    
    # Then we iterate k number of times and put the portion of first
    # k elements into the stack to be reversed.
    for _ in range(k):
        stack.append(queue.get())
    
    # Then we bring those k elements back in reverse order and append
    # them in the end of queue.
    for _ in range(len(stack)):
        queue.put(stack.pop())
    
    # Then we bring the n-k elements which are in the front into their
    # original positions by removing them from the front and bring 
    # them in end of the queue.
    for _ in range((queue.qsize()-k)):
        queue.put(queue.get())
    