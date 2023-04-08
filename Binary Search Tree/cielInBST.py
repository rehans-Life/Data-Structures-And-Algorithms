def findCeil(root, x):
    ans = -1
    while root:
        # If value of node is equal to the given integer then thats our answer
        # cause thats going to be smallest integer greater than or equal to the
        # given integer.
        if root.data == x:
            return root.data
        # If we find a node greater than the given integer hence that could be
        # our possible answer sow e store and we move towards its left cause
        # we want to find the smallest greater integer and that could be on the
        # left of the root.
        elif root.data > x:
            ans = root.data
            root = root.left
        # If value is less than the given integer hence we want to search for
        # greater values and that would be on the right of this node.
        else:
            root = root.right
    return ans