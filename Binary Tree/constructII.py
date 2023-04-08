from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Pointers to denote the where the inorder and postorder traversel of the the binary tree starts
        # ends
        inStart,postStart = 0,0
        inEnd,postEnd = len(inorder)-1,len(postorder)-1

        # Hash the nodes to there index in the inorder array so we can easily find the index of the root
        # in the inorder array
        index = dict()
        for i,node in enumerate(inorder):
            index[node] = i

        def helper(inStart,inEnd,postStart,postEnd):

            # If the start pointers exceed the end pointers we return None cause no elements in that
            # tree
            if inStart > inEnd and postStart > postEnd:
                return None
            
            # The root node the current binary tree is always going to be at end of the postEnd
            # I can access its index in inorder through the hashmap
            root = postorder[postEnd]

            # Index of root in the inorder array
            rootIndex = index[root]

            # Finding the inorder and postorder of the left and right subtree 

            # The left subtrees inorder traversel will end at root index - 1 starting from the current start
            inEndLeft = rootIndex-1

            # Caculating the number of nodes in the left subtree by checking the numbers of nodes
            # in its inorder traversel
            numsLeft = rootIndex - inStart

            # The post order traversel will start from the current start and go up until the 
            # postStart+ its number of nodes minus 1
            postEndLeft = postStart + numsLeft -1

            # Inorder for right traversel will go from on ahead of root till end
            inStartRight = rootIndex + 1
            
            # The starting will go one ahead of where left subtrees traversel ended till one behind the
            # the root
            postStartRight = postStart+numsLeft
            postEndRight = postEnd-1
        
            # Creating the root node of the tree
            node = TreeNode(root)

            # Recursively applying the same procedure and the getting there root nodes and attaching 
            # them to the left and right pointers of this root
            node.left = helper(inStart,inEndLeft,postStart,postEndLeft)
            node.right = helper(inStartRight,inEnd,postStartRight,postEndRight)

            return node

        return helper(inStart,inEnd,postStart,postEnd)