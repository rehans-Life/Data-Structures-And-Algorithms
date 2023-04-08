class Solution:
    def preorderTraversal(self, root) -> list[int]:

        preOrder = []
        currNode = root

        while currNode:
            if not currNode.left:
                preOrder.append(currNode.val)
                currNode = currNode.right
            else:
                prev = currNode.left
                while prev.right and prev.right != currNode:
                    prev = prev.right
                
                if prev.right == None:
                    prev.right = currNode
                    preOrder.append(currNode.val)
                    currNode = currNode.left
                else:
                    prev.right = None
                    currNode = currNode.right

        return preOrder