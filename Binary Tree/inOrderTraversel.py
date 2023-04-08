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

# Inorder Traversel technique on a Binary Tree: Here we first traverse
# the left Subtree of a node then the node itself after that we traversing
# the nodes rightsubtree and we do this for every single subtree. 

# So the mechanism is Left -> Root -> Right

ans = []

def inorder(root):
    
    # If root is None that means we have reached the end of the tree
    # and cant in orderly traverse anymore.
    if root == None:
        return
    
    # First we traverse the leftsubtree of the node
    inorder(root.left)
    
    # Then we traverse the node itself
    ans.append(root.data)
    
    # Then we traverse the right substree
    inorder(root.right)

inorder(root)
print(ans)