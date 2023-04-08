class TreeNode:
    pass
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

            if not root:
                return 
            
            # If I know both the nodes are on the left then i know the LCA will be the left of this node
            # So i go in that direction
            if root.val > q.val and root.val > p.val:
                return self.lowestCommonAncestor(root.left,p,q)
            
            # If both the nodes are greater are on the right then i know the LCA will be on the right side
            # so i go in that right direction.
            if root.val < q.val and root.val < p.val:
                return self.lowestCommonAncestor(root.right,p,q)
            
            # If none of these cases meet hence i know in all other cases this is my LCA            
            return root
        
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return None

        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val < q.val or root.val < p.val and root.val > q.val:
                return root
            elif root.val == p.val or root.val == q.val:
                return root