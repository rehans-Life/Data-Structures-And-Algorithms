# Time Complexity: O(h)
# Spce Compleixty: O(1)

from typing import Optional

class TreeNode:
    def __init__(self,val) -> None:
        self.val = val

def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:        

        if not root:
            return TreeNode(val)
            
        node = root        
        while True:
            if node.val > val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
        
        return root