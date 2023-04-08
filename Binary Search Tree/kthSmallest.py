class Solution:
    def kthSmallest(self, root, k: int) -> int:

        count = 0

        def dfs(root):

            nonlocal count

            if not root: return 
            
            leftChild = dfs(root.left)
            
            # If we are receiving a value in return then its the kth the smallest element so
            # return it 
            if leftChild: return leftChild

            count+=1

            # Once count hits k then that means your traversing your kth smallest eleement
            # cause inorder the elemenets are inserted in sorted order.
            if count == k: return root.val

            rightChild = dfs(root.right)

            # If we are receiving a value in return then its the kth the smallest element so
            # return it 
            if rightChild: return rightChild
        
        ans = dfs(root)
        
        return ans if ans else 0