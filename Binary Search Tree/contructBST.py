from math import inf

class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.right = right
        self.left = left

def contructBST(preorder):
    
    i = 0
    
    def helper(maxi=inf):    
        
        nonlocal i
        
        if i == len(preorder):
            return None
            
        if preorder[i] < maxi:
            
            node = TreeNode(preorder[i])
            i+=1
            
            node.left = helper(node.val)
            node.right = helper(maxi)
            
            return node
        else:
            return None
    
    return helper()

root = contructBST([9,5,3,2,1,4,7,6,8,12,11,13])

inorder = list()

def preorder(root):
    
    if not root:
        return
    
    inorder.append(root.val)
    
    preorder(root.left)
    preorder(root.right)
    
preorder(root)
print(inorder)