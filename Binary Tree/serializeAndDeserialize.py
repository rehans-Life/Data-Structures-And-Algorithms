from queue import Queue

class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):

        s = ""

        if not root:
            return  s
        
        queue = Queue()
        queue.put(root)

        while not queue.empty():

            node = queue.get()

            if not node:
                s+= 'n,'
            else:
                s+= f'{node.val},'

            if node:
                queue.put(node.left)
                queue.put(node.right)
        
        return s
        

    def deserialize(self, data):
        
        if data == "":
            return None

        s = data.split(',')
        s.pop()

        queue = Queue()
        root = TreeNode(int(s[0]))
        queue.put(root)

        for i in range(1,len(s),2):
            
            node = queue.get()
            
            if s[i] != 'n':
                nodeLeft = TreeNode(int(s[i]))
                node.left = nodeLeft
                queue.put(nodeLeft)
            
            if s[i+1] != 'n':
                nodeRight = TreeNode(int(s[i+1]))
                node.right = nodeRight
                queue.put(nodeRight)
        
        return root
