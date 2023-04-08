from typing import Optional
class TreeNode:
    pass
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # The bases cases are that both go None at the same time then you can return True
        # But if one goes None and the other hasnt therefore strcuture is not same so return
        # False
        if p == None or q == None:
            return (p == q)

        # Im doing a simulatneous preorder traversel so first im going to check if the root nodes are 
        # equal or not then im going to the left subtree of that node and then the right subtree from 
        # that node
        return (p.val == q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)