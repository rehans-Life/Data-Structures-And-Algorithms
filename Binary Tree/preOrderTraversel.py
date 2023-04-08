# Pre Order traversel through a binary tree

# It follows the order of Root -> Left Subtree -> Right Subtree.

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

def preOrder(root,ans=[]):
    
    # If the root node is None so we cant traverse anymore into it so we stop
    if root == None:
        return
    
    # We first traverse the root node then we traverse the left subtree
    # of that node and then we move to the right node
    
    # We do this for every single root node of the subtree. 
    
    ans.append(root.data)
    
    # We include the root then we recursively traverse through the left
    # subtree in the same way
    preOrder(root.left,ans)
    
    # After we finsih traversing the left subtree then we traverse the
    # right subtree of the root node.
    preOrder(root.right,ans)
    
    return ans
print(preOrder(root))