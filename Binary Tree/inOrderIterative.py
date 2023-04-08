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

def inOrderIterative(root):
    
    # A stack to maintain and store the nodes of the tree
    stack = list()
    
    # A node pointer to point at the next left node of a particular node
    # And the reason for that is that we need to move left first then
    # root after that we go to the right
    
    # Initially we start on with the root.
    node = root
    
    # An array to store node values in inOrder traversel.
    ans = []
    
    # As long as the stack is not empty or our node is also pointing at
    # a valid node then we keep running this while loop.
    while len(stack) or node:
        
        # First thing we do is if our node is not currently NONE which
        # means we can go more left so we add the node to our stack
        # and move left
        
        if node:
            stack.append(node)
            node = node.left
        
        # Second thing we do is if our node is currently NONE which
        # means we cant go left anymore but now we have to consider the 
        # root of this NONE which is on top of the stack cause after
        # left ends we go to the root and traverse it 

        else:
            root = stack.pop()
            ans.append(root.val)
            # And then after traversing the root we move to the right of it
            # So we set node pointer to the right node
            node = root.right
     
    return ans        

print(inOrderIterative(root))