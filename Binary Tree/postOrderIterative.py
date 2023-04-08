# First Method - 2-Stacks approach

# So the intuition behind this approach is that we traverse the binary tree in a 
# reverse post order so basically im going from top level to bottom level 
# right to left and the flow is root -> right -> left so basically completely
# opposite of the actual post order which goes from bottom -> top level, 
# left -> right subtree and then left -> right -> root for each node.

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

def postOrderIterativeI(root):
    
    # Its going to store the child left and right child of the node that i remove
    # for each node.
    stack1 = list()
    stack1.append(root)
    
    # Stack which stores the node values traversed in reverse postorder way so that
    # we can just reverse the stack values and get our values in reverse post order.
    stack2 = list()
    
    # We keep iterating until stack1 goes cause thats when iteration is completed.
    while len(stack1):
        
        # I pop the top node out of stack1 and place it in stack2        
        node = stack1.pop()
        
        stack2.append(node.val)
    
        # Since im making a revere post order traversel so i need to traverse
        # the right sbutree before the left subtree because the flow of traversel
        # is root -> right -> left. So thats why im inserting the right child on top
        # of the left child.
        
        if node.left:
            stack1.append(node.left)
        
        if node.right:
            stack1.append(node.right)    
        
    return list(reversed(stack2))

print(postOrderIterativeI(root))
