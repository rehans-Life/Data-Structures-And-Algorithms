from queue import Queue
from typing import List,Optional

class Node:
    def __init__(self,val: int,left=None,right=None) -> None:
        self.data = val
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

# In level order traversel you traverse through the binary tree level by level starting frmo level 1 to the last level and within
# each level you traverse from left to right.

    
def levelOrderI(root: Optional[Node]) -> List[List[int]]:

        # A queue in which im going to store the child nodes of the nodes i will be traversing through
        # of a particular level so that in the next iteration i can traverse through the nodes of the 
        # next level using the queue in the next iteration.
        queue = Queue()

        # Initially we add the root node within the queue because we have to start traversed through.
        queue.put(root)

        # A ans array which is going to store arrays each array will denote the value of the nodes
        # i traversed in a particular level. 
        ans = []

        # We run a while loop that runs until queue goes empty cause then we wouldve traversed through
        # all the levels by then
        while not queue.empty():
            
            level = []

            # We get the current size of the queue so we can remove all current level nodes from it
            qSize = queue.qsize()

            # We run a while until we have taken all the nodes of the current level out.
            while qSize:

                # We take the nodes of this out of the queue 
                node = queue.get()

                # Then we check first if they have a left child cause we traverse from left to right if it
                # does we add it in the queue for the next itration same thing for the right child as well
                if node.left:
                    queue.put(node.left)

                if node.right:
                    queue.put(node.right)

                # Then we add the value of the current within the level arr as well which is going to the value
                # of nodes of current level
                level.append(node.data)

                qSize-=1
            
            # We add the value of the nodes we traversed in the current level to our answer
            ans.append(level)

        return ans
    
print(levelOrderI(root))