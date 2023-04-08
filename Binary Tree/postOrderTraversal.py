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

# Post Order Traversel

# It follows the mechanism of Left -> Right -> Root.

# So basically for each node you traverse it left subtree first then the right subtree then only
# after that you consider the node itself.

ans= []

def postOrder(root):
    
    # If the root itself is None then we can traverse further so we stop
    if root == None:
        return 
    
    # Then we first traverse the left subtree for the node
    postOrder(root.left)
    
    # Then we traverse the right subtree for the node
    postOrder(root.right)
    
    # Then after that we consider the root itself
    ans.append(root.data)

postOrder(root)
print(ans)