
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root) -> list[int]:
        inorder = []

        currNode = root

        while currNode:

            if not currNode.left:
                inorder.append(currNode.val)
                currNode = currNode.right
            else:
                prev = currNode.left
                while prev.right and prev.right != currNode:
                    prev = prev.right
    
                if prev.right == None:
                    prev.right = currNode
                    currNode = currNode.left
                else:
                    prev.right = None
                    inorder.append(currNode.val)
                    currNode = currNode.right

        return inorder
        