class Solution:

    def leftHeight(self,root):
        count = 0
        node = root
        while node:
            count+=1
            node = node.left
        return count
    
    def rightHeight(self,root):
        count = 0
        node = root
        while node:
            count+=1
            node = node.right
        return count

    def countNodes(self, root) -> int:
        
        # If root of subtree is None then height is zero
        if not root:
            return 0
        
        # If root exists we check left height and right height cause if they are then 
        # the bottom level of the subtree is completely filled up 
        lh = self.leftHeight(root)
        rh = self.rightHeight(root)

        # If bottom level is completely filled then we can easily calculate the number
        # of nodes on the level just by using the formula 2^h - 1
        if lh == rh:
            return 2**lh-1
        
        # If thats not the case we have to go to the left side get the number of nodes
        # on that side and then do the same thing for the right side as well
        leftNodes = self.countNodes(root.left)
        rightNodes = self.countNodes(root.right)

        # We can just sum both sides of nodes up then add 1 and get the answer
        return 1 + leftNodes + rightNodes