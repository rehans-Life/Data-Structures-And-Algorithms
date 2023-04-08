class Solution:
    def searchBST(self, root, val: int):
        while root and root.val != val: root = root.left if root.val > val else root.right
        return root