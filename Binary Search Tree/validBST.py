from math import inf
def validateBST(root,mini=-inf,maxi=inf):
    if not root:
        return True    
    return root.val > mini and root.val < maxi and validateBST(root.left,mini,root.val) and validateBST(root.right,root.val,maxi)