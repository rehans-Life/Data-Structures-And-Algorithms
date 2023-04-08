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

def preOrderIterative(root):
    
    # Stack which is going to store the nodes within our tree
    stack = list()
    
    # Initially we have the root on top of the stack
    stack.append(root)
    
    # Answer list to store the nodes values obtained through preOrdered traversel.
    ans = list()
    
    while len(stack):
        # I pop the top node from the stack
        node = stack.pop()
        
        # Then if it is has a right child i insert on top of the stack
        if node.right:
            stack.append(node.right)
            
        # Then if it also has a left child then i insert on top of the
        # right child because the flow is Root -> Left -> Right.
        # So i want to consider the left child over the right child
        if node.left:
            stack.append(node.left)
            
        # Then i include the value of this node within the ans
        ans.append(node.val)
        
    return ans

print(preOrderIterative(root))