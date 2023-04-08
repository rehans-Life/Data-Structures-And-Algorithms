from typing import Optional
class TreeNode: pass
class Solution:
    def __init__(self) -> None:
        self.stack1 = list()
        self.stack2 = list()

    def bottomRight(self,root):
        while root:
            self.stack2.append(root)
            root = root.right

    def bottomLeft(self,root):
        while root:
            self.stack1.append(root)
            root = root.left

    def next(self):
        node = self.stack1.pop()
        if node.right: self.bottomLeft(node.right)

    def before(self):
        node = self.stack2.pop()
        if node.left: self.bottomRight(node.left)
    
    def top1(self): return self.stack1[len(self.stack1)-1].val
    
    def top2(self): return self.stack2[len(self.stack2)-1].val

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        self.bottomRight(root)
        self.bottomLeft(root)

        while self.top1() < self.top2():
            InNext = self.top1()
            InBefore = self.top2()
            if InNext + InBefore == k:
                return True
            elif InNext + InBefore > k:
                self.before()
            else:
                self.next()
        
        return False