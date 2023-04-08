from typing import Optional

class Node:
    def __init__(self,val: int,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
root = Node(1)
root1 = Node(2)
root2 = Node(3)
root3 = Node(4)
root4 = Node(5)
root5 = Node(8)
root6 = Node(6)
root7 = Node(7)
root8 = Node(9)
root9 = Node(10)
root.left = root1
root.right = root2
root1.left = root3
root1.right = root4
root4.left = root5
root2.left = root6
root2.right = root7
root7.left = root8
root7.right = root9

diameter = 0

class Solution:
    def diameterOfBinaryTree(self, root: Optional[Node]) -> int:

        diameter = 0

        def helper(root):

            nonlocal diameter

            if not root:
                return 0

            leftSubtreeHeight = helper(root.left)
            rightSubtreeHeight = helper(root.right)

            diameter = max(diameter,leftSubtreeHeight+rightSubtreeHeight)

            return 1+max(leftSubtreeHeight,rightSubtreeHeight)

        helper(root)
        return diameter