# A node consists of data field to store the data of the node 
# Then it consists of a left and right pointer to point to the left
# and right child of the node.

class Node:
    def __init__(self,val: int,left=None,right=None) -> None:
        self.data = val
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return str({'data':self.data,'left':self.left,'right':self.right})

root = Node(5)
root.left = Node(6)
root.right = Node(7)
root.left.left = Node(8)
root.left.right = Node(9)

print(root)