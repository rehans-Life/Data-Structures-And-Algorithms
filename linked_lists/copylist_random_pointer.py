class Node:
    def __init__(self,val=0):
        self.val = val
        self.prev = None
        self.nxt = None

def copyRandomList(self,head):

        # Traversal to connect each Node to its copy.
        temp = head
        while temp:
            nxt = temp.nxt
            copyNode = Node(temp.val)
            copyNode.nxt = nxt
            temp.nxt = copyNode
            temp = copyNode.nxt
        
        # Traversal to find each nodes random pointer
        temp = head
        while temp:
            temp.nxt.random = temp.random.next
            temp = temp.nxt.nxt
        
        # Traversal to detach both the lists
        temp = head
        dummy = Node()
        tail = dummy

        while temp:
            tail.nxt = temp.nxt
            tail = tail.nxt
            temp.nxt = tail.nxt
            temp = temp.nxt

        return dummy.nxt