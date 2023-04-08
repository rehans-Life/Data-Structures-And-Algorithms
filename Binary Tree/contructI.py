from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Index pointers to start and end of the inorder and preorder traverels of the 
        # binary tree we are contructing they are going to change as we traverse the binary
        # trees
        inStart,preStart = 0,0
        inEnd, preEnd = len(inorder)-1,len(preorder)-1

        # Im going to hash each node to its indexes in the inorder array so that i can access the
        # roots indexes easily in the inorder array.
        index = dict()

        for i,node in enumerate(inorder):
            index[node] = i 
            
        # Recursivley finding the root of each tree what we would need is there inorder traversel
        # and pre order traversel we are going to denote using the index pointers
        def helper(inStart,inEnd,preStart,preEnd):

            # Base Cases: If the start pointers exceeded end pointers then there are no elements
            # in the tree so we return None
            if inStart > inEnd and preStart > preEnd:
                return None

            # PRESTART pointer is always going to be pointing at the root of the current subtree.
            root = preorder[preStart]

            # Acessinng the index of the root in my inorder traversel
            inRoot = index[root]

            # Accesing the number of nodes in the left subtree portion in my current tree
            numsLeft = inRoot - inStart

            # Now i can easily find the preorder and inorder traversels of the left subtree
            # as well the right subtree

            # The in order traversel of the left subtree is going to start from the current 
            # inStart and is going to end at the index one behind the root
            inEndLeft = inRoot-1

            # And its preOrder is going to be at one infront of the root and end at the point
            # which is equivalent to the point which is equal to the number of the elements
            # behind the root in the inorder traversel.
            preStartLeft = preStart+1
            preEndLeft = preStart+numsLeft

            # The inOrder traversel of the right subtree is going to be starting from the one 
            # index infront of the current root and end at the inEnd
            inStartRight = inRoot+1

            # Same for pre its going to start from where the left subtrees preOrder ended.
            preStartRight = preStart+numsLeft+1

            # Creating the root node for current tree
            rootNode = TreeNode(root)

            # Then we contruct both the left and right subtrees in the similar way and return
            # there roots and connect them to the left and right pointers of there parent.
            rootNode.left = helper(inStart,inEndLeft,preStartLeft,preEndLeft)
            rootNode.right = helper(inStartRight,inEnd,preStartRight,preEnd)

            return rootNode

        return helper(inStart,inEnd,preStart,preEnd)