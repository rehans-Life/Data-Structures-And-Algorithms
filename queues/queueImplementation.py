from collections import deque
from queue import Queue

queue = deque()

queue.append(12)
queue.append(15)
queue.append(20)

# This method pops the elements from the front of the queue in O(1) operation.
queue.popleft()
queue.popleft()

# print(queue)

q = Queue()
q.put(10)
q.put(4)
q.put(7)
q.put(9)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
q.put(10)
print(q.empty())