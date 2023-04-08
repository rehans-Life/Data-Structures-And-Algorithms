# So your basically going to do all traversels in one traversel of the 
# binary tree.

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

def allInOne(root):
    
    # A stack which is going to store the nodes along with numbers 
    # ranging from 1 to 3 
    
    # Number 1 denoting that im traversing the node before it left 
    # and right subtree 
    
    # Number 2 denoting that im traversing the node after traversing
    # its left subtree but before traversing its right subtree.
    
    # Number 3 denoting that im traversing the node after traversing
    # through its left and right subtree.
    
    stack = list()
    
    # We include the root node with value set as 1
    stack.append([root,1])
    
    # Arrays to store the node values in preorder, postorder inorder 
    # traversel.
    preOrder = []
    postOrder = []
    inOrder = []
    
    while len(stack):
        
        # Now what you do is take out the top value from the stack
        node = stack[len(stack)-1]
        
        # Then you check the number of node if its 1 that means your 
        # traversing the node without traversing its left and right subtree
        # Hence im following the order of the preOrder traversel here so
        # i add the node's value in my preOrder list
        if node[1] == 1:
            preOrder.append(node[0].val)
            # Then you increment its number to 2 and add the its left
            # child on top of it so that when you traverse through this
            # same node the second time you traversing it after you have
            # traversed its left subtree then in that case that would be 
            # inOrder traversing and you can add the node in your inorder
            # list then.
            node[1]+=1
            if node[0].left:
                stack.append([node[0].left,1])
        
        # Then you check number of node if its 2 that means you traversing
        # node without traversing its right subtree but you traversed the 
        # left tree in that case you can include the node inside of your
        # inorder traversel
        elif node[1] == 2:
            inOrder.append(node[0].val)
            # Then you increment number to 3 and then add the right
            # child on top of it so that when you see the node again
            # with number 3 you know you have already traversed its left
            # and right child and now you can include it in your postOrder
            # list.
            node[1]+=1
            if node[0].right:
                stack.append([node[0].right,1])
            
        else:
            postOrder.append(node[0].val)
            stack.pop()
            
    return preOrder,inOrder,postOrder

print(allInOne(root))            
            
