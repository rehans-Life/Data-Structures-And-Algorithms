class BSTIterator:
    def __init__(self,root) -> None:
        # A stack to store the inorder traversel of the BST
        self.stack = list()
        
        # A function that inserts all elements of the left boundry 
        # starting from a node
        self.bottomLeft(root)
        
    def bottomLeft(self,root) -> None:
        while root:
            self.stack.append(root)
            root = root.left
    
    def next(self) -> int:
        node = self.stack.pop()
        if node.right: self.bottomLeft(node.right)
        return node.val
    
    def hasNext(self) -> bool:
        return bool(len(self.stack))
    
class BSTIterator:
    def __init__(self,root) -> None:
        self.stack = list()
        self.bottomRight(root)
        
    def bottomRight(self,root)-> None:
        while root:
            self.stack.append(root)
            root = root.right
        
    def before(self) -> int:
        node = self.stack.pop()
        if node.left: self.bottomRight(node.left)
        return node.val

    def hasBefore(self):
        return bool(len(self.stack))