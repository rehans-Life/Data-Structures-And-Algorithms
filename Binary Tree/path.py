# Your given a root of a binary tree and value B you need to return the
# path from the root to the node with value B

def findPath(root,B):
    
    # An array to store our path.
    path = []
    
    # We are going to make a inorder traversel to find the path cause
    # it includes the root first
    def helper(node):
        
        # If node is none, this means we have hit a breakpoint and we still
        # havent found the node of interest and therefore we are going to
        # return False denoting that this path wont help us reach our node
        # of interest
        if not root:
            return False
        
        # Then we include our current node value inside of our path
        path.append(node.val)
        
        # Then if this nodes value is equal to node we want to find the 
        # path till then we stop here and return True
        if node.val == B:
            return True
        
        # If its not the node till where we need to traverse till
        # then we go to its left and check if there path on its 
        # left which takes to the node of interest
        leftPathExists = helper(node.left)
        
        # If the path on the left exists then we return True without
        # checking the right path cause we have already found our path
        if leftPathExists:
            return True
        
        # If the path on the left doesnt exists only then we check the right
        # side of the node and see if a path exists there as well.
        rightPathExists = helper(node.right)
        
        if rightPathExists:
            return True
        
        # If from both sides we wont reach our node of interest from this
        # node then we will remove this node from our path and return
        # false cause we cant reach to our node of interest from our node.
        path.pop()
        
        return False