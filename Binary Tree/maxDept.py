class Node:
    def __init__(self,val: int,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
root = Node(1)
root1 = Node(2)
root2 = Node(3)
root3 = Node(4)
root4 = Node(5)
root5 = Node(8)
root6 = Node(6)
root7 = Node(7)
root8 = Node(9)
root9 = Node(10)
root.left = root1
root.right = root2
root1.left = root3
root1.right = root4
root4.left = root5
root2.left = root6
root2.right = root7
root7.left = root8
root7.right = root9

def maxDept(root):
    
    # If root is None then its doesnt have a height so we return 0
    if not root:
        return 0

    # Finding the height of the left and right subtrees height from
    # this root
    leftSubtreeHeight = maxDept(root.left)
    rightSubtreeHeight = maxDept(root.right)
    
    # Adding the max of the two subtrees height to the current root
    # height 1.
    currHeight = 1 + max(leftSubtreeHeight,rightSubtreeHeight)
    
    # Return the current height of this subtree.
    return currHeight

print(maxDept(root))