from collections import deque

class Node:
    def __init__(self,val: int,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
root = Node(1)
root1 = Node(2)
root2 = Node(3)
root3 = Node(4)
root4 = Node(5)
root5 = Node(8)
root6 = Node(6)
root7 = Node(7)
root8 = Node(9)
root9 = Node(10)
root.left = root1
root.right = root2
root1.left = root3
root1.right = root4
root4.left = root5
root2.left = root6
root2.right = root7
root7.left = root8
root7.right = root9

def maximumWidth(root):
    
    # A queue to store the child nodes of the nodes that i will be currently traversing at my level from left to right therefore 
    # in order traverse the nodes of the next level i can just the nodes out of the queue.
    queue = deque()
    
    # A variable to store the the max width level that ive found at different stages
    maxWidth = 0
    
    # Initally adding the root along with its index within the queue
    queue.append([root,0])
    
    # Until queue goes empty we keep iterating.
    while len(queue):
        # We are getting the current queue size so we can iterate through the nodes currently in the queue because those are the nodes
        # of the current level.
        qSize = len(queue)
        
        # The minimum index node is going to be the leftmost node of the level cause indexing is from left to right and starts from 1
        # and since traversel is from left to right therefore first node in the queue for each iteration is the leftmost node
        minIndex = queue[0][1]
        
        # Variables to store the indexes of the leftmost and rightmost nodes at the current level so i can calculate the length of the 
        # current level.
        first,last = 0,0
        
        # We run a loop that removes nodes that are currently in the queue before adding the children.
        for i in range(qSize):
            
            node = queue.popleft()
            
            # First node in the queue is the leftmost node of the level cause im traversing from left to right.
            # for each level hence i store its index to calculate the width of the level
            if i == 0: first = node[1]
            
            # The last node is the rightmost node since im traversing from left to right
            if i == qSize-1: last = node[1]
            
            # Then if the node has left child we add it first cause we wanna travers from left to right for each level
            # and we also calculate there indexes after decrementing the nodes index by the minimum index in the array
            if node[0].left: queue.append([node[0].left,(i-minIndex)*2 + 1]) 
            
            if node[0].right: queue.append([node[0].right,(i-minIndex)*2 + 2])
            
        # Then i check if the current levels width is the max width or not
        maxWidth = max(maxWidth,(last-first+1))
    
    return maxWidth

print(maximumWidth(root))            
            
            