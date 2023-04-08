
# This function is going to take in the node to be deleted itself.

def helper(root):
    
    # If the left subtree of the node to be deleted doesnt exist then we have to 
    # directly connect the right subtree of the node to be deleted to the parent node 
    # of the node to be deleted.
    
    if not root.left:
        return root.right
    
    # If left subtree does exist then i want to find the rightmost node in the left
    # subtree cause its going to be the greatest node in the left subtree which is 
    # going to be less than the right subtree nodes
    
    # And i know the right most nodes right pointer will be empty and we want to connect
    # it to nodes which are greater than it and hence it would make sense to connect
    # the right subtree nodes to its right
    
    # Find the right most by traversing the right boundry of the leftsubtree
    node = root.left
    
    while node.right:
        node = node.right
        
    # Connecting the rightmost node to the right subtree of the node to be deleted
    node.right = root.right
    
    # Then returning the root of the left subtree which im going to connect to the 
    # parent node.
    return root.left

def deleteInBST(root,key: int):
    
    # In case when the root in itself is told to be deleted then the left subtrees
    # root in itself is going to become the new root and is going to the right subtree
    # connected to it hence i can just return the output of the helper function itself.
    if root.val == key:
        return helper(root)
    
    dummy = root
        
    while root:
        # If the current nodes value is greater than the node to be deleted hence
        # before going to the left im going to check what if its direct child is 
        # the node to be deleted cause if it is then this is the parent node of the 
        # node to be deleted hence i need to remove its pointer from that node
        # and move it to its left subtrees root 
        if root.val > key:
            leftChild = root.left
            if leftChild and leftChild.val == key:
                # Im going to move the left pointer of the parent node to the left subrees
                # root of the node to be deleted for that i use helper function.
                root.left = helper(leftChild)
                break
            else:
                root = leftChild
                
        else:
            # Similary approach when the current nodes value is less but this
            # time its the right child i check and i move the right pointer
            rightChild = root.right
            if rightChild and rightChild.val == key:
                root.right = helper(rightChild)
                break
            else:
                root = rightChild

    return dummy
    