def isBalanced(root) -> bool:

        if not root:
            return True

        def helper(root):
            
            # Base Case : If root is None then we can return 0
            if not root:
                return 0

            # If not none then we need to find the height of its left and right
            # subtree to be able to calculate the height of the current subtree

            # So i make recursive calls for its left and right subtree to find there
            # heights:

            leftSubtreeHeight = helper(root.left)

            # If the any of the recursive calls returns -1 then that means the binary tree
            # is not balanced therefore im going to return -1 for all recursive calls
            if leftSubtreeHeight == -1:
                return -1

            rightSubtreeHeight = helper(root.right)

            # If the any of the recursive calls returns -1 then that means the binary tree
            # is not balanced therefore im going to return -1 for all recursive calls
            if rightSubtreeHeight == -1:
                return -1

            # Since im trying to check if the binary tree is balanced or not then i need to 
            # make sure that the absolute difference between the heights of the left and right subtree
            # for the current node is not greater than 1 cause if it is then the binary tree
            # is not balanced and hence i need to return false then.
            if abs(leftSubtreeHeight-rightSubtreeHeight) > 1:
                return -1
            else:
                # If this node is balanced then im going to compute its height and send it to its 
                # parent so i can perform a similar check for its parent as well
                return 1 + max(leftSubtreeHeight,rightSubtreeHeight)

        # If the function returns -1 then this returns false cause then -1 != -1 but it returns a 
        # height that means all nodes were balanced therefore it returns the height of the tree
        # in that case height != -1 is true so i return true
        return helper(root) != -1