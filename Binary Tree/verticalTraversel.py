from typing import List
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
root2.left = root6
root2.right = root7
root4.left = root5
root4.right = root8

def verticalTraversal(root) -> List[List[int]]:
        # Queue for the level order traversels where im going to store the child nodes
        # of the node im traversing so in the next traversel i can traverse the nodes
        # of my next level just by taking them out of the queue
        queue = Queue()

        cols = dict()

        queue.put([root,0,0])

        while not queue.empty():

            node = queue.get()

            row = node[1]
            col = node[2]

            # Adding the child nodes of the node im traversing back into the queue so i can traverse
            # through the nodes of my next just by taking them out of queue.

            # The left child is going to be at one column behind its parent node and row below its parent
            # node
            if node[0].left:
                queue.put([node[0].left,row+1,col-1])

            # The right child is going to be at one row below and one column ahead its parent
            if node[0].right:
                queue.put([node[0].right,row+1,col+1])

            # Adding the node into the map
            if col not in cols:
                cols[col] = dict()
            
            if row not in cols[col]:
                cols[col][row] = list()

            cols[col][row].append(node[0].val) 

        ans = []

        for col in sorted(cols.keys()):
            vals = []

            for row in cols[col].values():
                vals.extend(sorted(row))
            
            ans.append(vals)


        return ans

print(verticalTraversal(root))