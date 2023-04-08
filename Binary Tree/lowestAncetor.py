# Your given two nodes and you need to find there lowest common ancestors

def lca(root,p,q):
    
    def helper(node):
        
        # We have to stop when we find a none or one of the given nodes
        if not node or node == p and node == q:
            return node
        
        # If the given node is not one of our nodes then we check if it is
        # the ancesotr
        
        # It will be an ancestor when we go through both of its sides and find
        # the both the given nodes on both sides so basically when we find
        # non null values
        leftNode = helper(node.left)
        rightNode = helper(node.right)
        
        # If both null the  we return null to parent to denote this side does
        # not consist of the given nodes
        
        # If you find one of them then you return it to the parent 
        
        # If you find both sides as non null vale then current node is that LCA 
        # so return it
        
        if not leftNode:
            return rightNode
        elif not rightNode:
            return leftNode
        else:
            return node
        
    return helper(root)