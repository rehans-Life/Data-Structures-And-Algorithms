from queue import Queue

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

def timeToBurnTree(root, start):
    
    if not root:
        return 0

    # First we need to setup the parent pointers via a hashmap and bfs
    parent = dict()
    queue = Queue()
    queue.put(root)
    target = root

    while not queue.empty():
        node = queue.get()

        # Hashing the children of the node to the node itself cause its there
        # parent
        if node.left:
            queue.put(node.left)
            parent[node.left] = node
        
        if node.right:
            queue.put(node.right)
            parent[node.right] = node
        
        # Also searching for the target while doing the bfs
        if node.right and node.right.data == start:
            target = node.right
        
        if node.left and node.left.data == start:
            target = node.left

    # Then we need to traverse using bfs starting from the target node and 
    # move in all directions upwards, left and right
    # And keep traversing until queue goes empty

    queue = Queue()
    queue.put(target)

    # Maintaing a set for nodes that have already been burned so we dont traverse
    # back to them
    burned = set()
    burned.add(target)

    # Variable to store the seconds it took to burn
    seconds = 0

    while not queue.empty():
        
        # We need to burn only the nodes that are in the queue during the traversel
        # cause those nodes will take one second to burn there children
        qSize = queue.qsize()

        for _ in range(qSize):
            node = queue.get()

            # Im going to move in all directions of the node and burn the parent and both the
            # children if they are not already burned
            if node.left and node.left not in burned:
                burned.add(node.left)
                queue.put(node.left)
            
            if node.right and node.right not in burned:
                burned.add(node.right)
                queue.put(node.right)
            
            if node in parent and parent[node] not in burned:
                burned.add(parent[node])
                queue.put(parent[node])

        # If nodes were actually burned then we incrmeent seconds
        if not queue.empty(): 
            seconds+=1

    return seconds


print(timeToBurnTree(root,root4))