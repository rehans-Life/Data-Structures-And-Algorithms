# Approach II to traverse in post order using Iteration this uses one
# stack.

# Flow in post Order -> Left -> Right -> Root
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

def postOrderIterative(root):
    
    # We maintain a stack which is going to allow us to make a iterative
    # post order traversel.
    stack = list()
    
    # A node pointer known as currNode which is going to point the 
    # current node we are trying to traverse through.
    
    # It's initially going to be the root.
    
    currNode = root
    
    # Then we need a another node pointer for checking if a node
    # whose left side is traversed does it have a right node that
    # needs to be traversed as well cause we can only consider the
    # current if both its left and right side are traversed
    rootRight = None
    
    ans = []
    
    # We run a while that runs until the stack goes empty and
    # currNode is null both these conditions should be met for
    # this traversel to stop.
    while currNode or len(stack):
        
        # We check if currNode is not None 
        if currNode:
            # If its not none then we add it in our stack and we move 
            # to its left by setting currNode as left of my current Node
            stack.append(currNode) 
            currNode = currNode.left
        
        # If currNode is None thats means the node which is on top of our
        # stack its left is completely traversed or we can say its None
        # In that case we check its right
        else:
            rootRight = stack[len(stack)-1].right
            
            # If its right is null thats means the node which is not top of
            # our stack its left and right are traversed are completely 
            # traversed so we can add it in our traversel.
            if not rootRight:
                node = stack.pop()
                ans.append(node.val)    
                # Since we comletely traversed through this node we check
                # if this node was the right node of its root if it was
                # then we traversed through its right subtree we could
                # add it in our answer.
                rootRight = node
                
                while len(stack) and rootRight == stack[len(stack)-1].right:
                    # If the node we finished traversing is the right node 
                    # Of the top node of our stack then we include it in our 
                    # ans.
                    node = stack.pop()
                    ans.append(node.val)
                    # We set current node we just added as root right to
                    # perform a check on its right as well
                    rootRight = node
                
            else:
                # If right exists though we set it as currNode cause we
                # gotta traverse it first then only we can consider the 
                # root node as our answer.
                currNode = rootRight
    
    return ans    
                    
print(postOrderIterative(root))
            
            
            
def postOrderIterative(root):

    stack = list()
    
    currNode = root
    rootRight = None
    
    ans = []
    
    while currNode or len(stack):
        
        if currNode:
            stack.append(currNode) 
            currNode = currNode.left
        else:
            rootRight = stack[len(stack)-1].right
            
            if not rootRight:
                node = stack.pop()
                ans.append(node.val)    
                rootRight = node
                
                while len(stack) and rootRight == stack[len(stack)-1].right:
                    node = stack.pop()
                    ans.append(node.val)
                    rootRight = node
            else:
                currNode = rootRight
            
    return ans    