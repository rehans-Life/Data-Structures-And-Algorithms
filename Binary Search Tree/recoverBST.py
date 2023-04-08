
class Solution:
    def recoverTree(self, root) -> None:
        # Node Pointers for the first disrutpion thats going to happen during
        # the inorder traversel
        first = None
        middle = None

        # One node pointer for the second disruption if it happens
        last = None

        # Node pointer for storing the previous node i traversed in my inorder traversel. 
        prev = None

        def helper(root):

            nonlocal prev,last,first,middle

            if not root:
               return 

            helper(root.left)

            # Disruption happens when current node is smaller than the node previous to it
            if prev and prev.val > root.val:
                # First Disruption
                if not first and not middle:
                    first = prev
                    middle = root
                else:
                    # Second Disruption
                    last = root

            # Before going to the right the previous becomes the current node since we stopped
            # at it
            prev = root

            helper(root.right)

        helper(root)

        if not last:
            first.val,middle.val = middle.val,first.val
        else:
            first.val,last.val = last.val,first.val
