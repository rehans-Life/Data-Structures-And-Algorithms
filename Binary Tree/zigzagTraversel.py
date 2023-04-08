from queue import Queue
from typing import List,Optional
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

def zigzagLevelOrder(root: Optional[Node]) -> List[List[int]]:

        # An array which is going to store arrays an each array denotes the value of the nodes that ive 
        # within a level
        ans = []
        
        if not root:
            return ans

        # A flag to tell me when should i reverse my traversel for level order traversel so that the ouput
        # is in zig zag order traversel
        
        # 0: Inidicates I need to traverse from left to right for the current level so in this case i keep 
        #the level 
        # order traverse for that level the same cause in zig zag order it would be the same.
        
        # 1: Indicates I need to traverse from right to left for the current level so in this case i reverse 
        # the level
        # order traversel that ive made for that level cause thats how it would be zig zag order.
        
        flag = 0
        
        # A queue which is going to store the children of the nodes that i traverse at each level so that i can
        # make a level order traversel for the next level as well by the taking the nodes out of the queue
        queue = Queue()
        queue.put(root)
        
        while not queue.empty():
            
            # Taking the size of the queue so i can remove the elements that are current inside of my queue
            qSize = queue.qsize()

            # To store the value of tne nodes that are currently on my level
            level = [0] * qSize 
            
            for i in range(qSize):
                
                node = queue.get()
                
                # If this node has left and a right child then i add them respectively inside of the queue
                # First left then right cause im making a level order traversel.
                if node.left:
                    queue.put(node.left)
                
                if node.right:
                    queue.put(node.right)
                    
                # As im adding the elements inside of the level array which stores the node values
                # at my current level if flag is 1 then im going to add elements in reverse order.
                index = i if flag == 0 else qSize - i - 1

                level[index] = node.val
            
            ans.append(level)

            # Setting the flag as one then i switch to 0 for my next level if its 1 then i switch to 
            # 0 for my next level.
            flag = 1 if flag == 0 else 0
            
        return ans