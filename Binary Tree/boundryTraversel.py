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
root6.left = root5
root2.left = root6
root2.right = root7
root7.left = root8
root7.right = root9

# Im going to do a inorder traversel from the root's left till the deepest node on its left subtree
def leftBoundry(root,ans):
    
    # Which is going to store the currNode im traversing through
    currNode = root
    
    while currNode:
        # If the currNode im on is not a leaf then im going to include its value in the answer
        
        # Thats because im going to add all the leaf nodes seperately into the ans array after ive traversed
        # the left boudnry.
        
        if not isLeaf(currNode): 
            ans.append(currNode.val)
        
        if not currNode.left: 
            currNode = currNode.right 
        else: 
            currNode = currNode.left 

# This function is going to find all the leaf nodes within the tree and add them to the answer.
def allLeaves(root,ans):
    
    if not root:
        return 
    
    # If current root is a leaf then add its value in the ans
    if isLeaf(root): 
        ans.append(root.val)
    
    # Finding the leaf nodes on the left and on the right of the root.
    
    # And you can note that we finding the leaf nodes on the left of root first then
    # the right of root cause thats the order of our boundry traversel.
    allLeaves(root.left,ans)
    allLeaves(root.right,ans)

# Now i need to traverse the right boudnry in reverse till the root for that we can persue an post order traversel
# in iterative way where we go in reverse which is root -> right -> left where we dont include the left part.
def rightBoundry(root,ans):
    
    currNode = root
    stack = list()
        
    while currNode:
        
        if not isLeaf(currNode): 
            stack.append(currNode.val)
            
        if not currNode.right:
            currNode = currNode.left
        else:
            currNode = currNode.right  
        
    while len(stack):
        ans.append(stack.pop())  
    
# If the node doesnt have a left and right child then its a Leaf obviously so i return True.
def isLeaf(node): return True if not node.left and not node.right else False

def boundryTraversel(root):
    # An array to store the node values within the boundry traversel.
    ans = []
    
    if not root: 
        return ans
    
    ans.append(root.val)
    
    # A function to traverse the left boundry of root
    
    # The left boundry is defined as the the path from the root till its left most node 
    # And its basically till the deepest node on its left subtree.
    leftBoundry(root.left,ans)
    
    # After we have traversed the left boudndry we need to include all the leaf nodes then from
    # left to right of the tree
    allLeaves(root,ans)
    
    # After including the leaf nodes then we need to traverse the right boundry of the root
    # in reverse starting the right deepest node to the root this path is considered as the right
    # boundry.
    rightBoundry(root.right,ans)
    
    return ans

print(boundryTraversel(root))