from math import inf
class NodeValue:
    def __init__(self,size,mini,maxi) -> None:
        self.size = size
        self.min = mini
        self.max = maxi

def isLeaf(root):
    if not root.left and not root.right:
        return True
    else:
        return False

def largestBST(root):
    
    def helper(root):
        if not root:
            return NodeValue(0,inf,-inf)
        
        if isLeaf(root):
            return NodeValue(1,root.val,root.val)
        
        leftTree = helper(root.left)
        rightTree = helper(root.right)
        
        if leftTree.max < root.val and rightTree.min > root.val:
            return NodeValue(leftTree.size+rightTree.size+1,min(leftTree.min,root.val),max(rightTree.max,root.val))
        else:
            return NodeValue(max(leftTree.size,rightTree.size),-inf,inf)

    return helper(root).size
