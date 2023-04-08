from queue import Queue
from typing import Optional,List
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

# Iterative Approach

def rightView(root):
    
    # Im going to be making a level order traversel therefore i need to 
    # maintain a queue data structure where ill store the children nodes
    # of the nodes im traversing at a particular level so in that in order
    # traverse the nodes at the next level for that i can just take the 
    # nodes out of my queue.
    queue = Queue()    
    
    # Array to store the value of nodes that can be viewed from the right
    # of the binary tree.
    res = []
    
    # Adding the root node initially into the queue
    queue.put(root)
    
    while not queue.empty():
        
        # Getting the queue size initally so i can only remove the nodes
        # that currently exist in the queue this is so that i dont traverse
        # the child nodes that im going to be adding cause i need to save
        # them up for traversing the next level.
        qSize = queue.qsize()
        
        for i in range(qSize):
    
            node = queue.get()
            
            # Im going to be traversing from right to left for each
            # level hence i can say the first node that i traverse
            # for each level is going to be rightmost node
            
            # And i know for each level only the right most node 
            # can only be viewed from the right view.
            
            # Hence since it can be viewed therefore i can add the node
            # to my answer.
                    
            if i == 0: res.append(node.val)
            
            # Adding the right child first then the left child so that
            # i can traverse each level from right to left.
            if node.right: queue.put(node.right)
            if node.left: queue.put(node.left)
    
    return res

print(rightView(root))


# Recursive Approach

class Solution:
    def rightSideView(self, root: Optional[Node]) -> List[int]:
        
        ans = []

        if not root:return ans

        def helper(node,level):
            nonlocal ans
            
            if not node:
                return 

            # If the level where the node exists is equal to the length of the answer array
            # therefore its the first node that exists that im traversing through this level
            # And since im traversing the right side first therefore the first node that i
            # found for each level is going to be its right most node and since its the 
            # right most of the level hence it can be seen from the right view at 
            # this level
            if level == len(ans):
                ans.append(node.val)

            
            # First going towards the right then then going to the left cause i need to 
            # traverse the right most nodes of each level first
            helper(node.right,level+1)
            helper(node.left,level+1)
        
        helper(root,0)
        return ans
