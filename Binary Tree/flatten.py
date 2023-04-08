# Note: The only special thing about this algorithm is how we are able to connect
# the topmost node of the right subtree to the bottom most right node of the 
# left subtree 

# Rest all is just connecting the parent node to there left children.

class Solution:
    def flatten(self, root) -> None:
        # This is going to store the previous node where i stopped at 
        prev = None

        # Recursive functions thats going to follow the order of RIGHT LEFT ROOT
        def helper(node):
            nonlocal prev
            # Base if root None then return we cant go further
            if not node:
                return

            # I traverse the right side first then move to the 
            # left side                
            helper(node.right)
            helper(node.left)

            # When i stop at this node i wanna connect it to the previous node i
            # stopped at
            node.right = prev
            node.left = None

            # Then set this as the previous node where i stopped at 
            prev = node
        
        helper(root)
        
    def flattenStack(self,root):
        stack = list()
        stack.push(root)
        currNode = None
        
        while len(stack):
            # Take the top most node out and set it to the current node
            currNode = stack.pop()
            
            if currNode.left: stack.append(currNode.left)
            if currNode.right: stack.append(currNode.right)
            
            # If the node has children im going to connect the nodes right pointer to them or else
            # imma connect to the topmost node of the right subtree or else it could be that im on the last
            # node so its null
            
            if len(stack):
                currNode.right = stack[len(stack)-1]
            
            stack.left = None
    
# Optimal Space Complexity: O(1)

# Note: The only special thing about this algorithm is how we are able to connect
# the topmost node of the right subtree to the bottom most right node of the 
# left subtree 

# Rest all is just connecting the parent node to there left children.

class Solution:
    def flatten(self, root) -> None:
       # This is going to maintain the current node we are traversing
        currNode = root

        while currNode:
            # If the current node has a left subtree hence we want to do some
            # things in order to align the pointers.
            if currNode.left:
                # First we find the bottom most right node in the left subtree
                # of the current node
                prev = currNode.left
                while prev.right:
                   prev = prev.right
                
                # Then we know the right subtree is going to be included
                # in the linked only after the right bottom most node
                # left subtree because the nodes should be arranged in 
                # inorder traversel in the linked lists

                # And the right subtree are only included within the preorder
                # traversel after the left subtrees traversel ends Hence the right
                # pointer of the right most node in left subtree should be at the
                # root node of the right subtree cause thats where the inorder
                # traversel for the let subtree ends
                prev.right = currNode.right

                # In the linked lists the next node should be the left subtrees
                # root.
                currNode.right = currNode.left
                currNode.left = None
            
            # Then we move to the right to do the same cause right pointer
            # is at the left subtrees root
            currNode = currNode.right