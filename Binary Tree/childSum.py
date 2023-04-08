def childrenSum(root):
    
    # Base Case If i cant go further we return false.
    if not root:
        return
    
    # Then first thing i need to check for my current node is that is its childrens sum less than or greater
    # then its children before traversing its left or right side.
    
    # If greater than we replace its value with its childrens sum but if greater then we replace its children's value
    # with this node's value so that when they comeback there sum is greater there's parent node sum.
    
    childSum = 0
    
    if root.left: childSum+=root.left.val
    if root.right: childSum+=root.right.val
    
    if childSum < root.val:
        if root.left: root.left.val = root.val
        if root.right: root.right.val = root.val
    
    # Then we go to the bottom of the tree performing the same mechanism so that when we start coming back up and start replacing
    # each parent node with its children's sum there childrens sum is always greater
    childrenSum(root.left)
    childrenSum(root.right)
    
    # Now we replace the child sum value with there parents cause we its going to be greater than it
    childSum = 0
    
    if root.left: childSum+=root.left.val
    if root.right: childSum+=root.right.val
    
    if root.left or root.right:root.val: root.val = childSum