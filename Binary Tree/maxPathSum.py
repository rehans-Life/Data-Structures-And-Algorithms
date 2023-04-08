from math import inf

class Solution:
    def maxPathSum(self, root) -> int:

        # A variable to store our candidates for our max sums 
        maxSum = -inf

        # A recursive function for dfs
        def helper(root):
            nonlocal maxSum

            # If root is None then sum is Zero
            if not root:
                return 0

            # If not None then i need to find the sumation of left subtrees maximum sumation path
            # and I need to find its right subtrees maximum sumation path as well so i can compute
            # the max path sum from this node

            # If max path from a subtree is negaitve then i dont consider it cause its only going to decrease my
            # sum

            # If the max sum from a subtree we completely ignore cause thats only going to decrease my maxSum
            # while im trying to maximize it.

            leftMaxPath = max(0,helper(root.left))
            rightMaxPath = max(0,helper(root.right))

            # Then i compute the path sum from this node and check if its our answer or not cause it is a
            # candidate for it 
            currPathSum = leftMaxPath + rightMaxPath + root.val
            maxSum = max(maxSum,currPathSum)

            # I return the path sum from this node which is greater of the two so its parent traverses its 
            # path with the maximum sum cause i need to maximize my path sum
            return root.val + max(leftMaxPath,rightMaxPath)

        helper(root)
        return maxSum

