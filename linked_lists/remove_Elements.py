class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
def removeNodes(head, k):
    
    if not head or head.next == None:
        return head
    
    # Write your code here.
    dummy = Node(-1)
    dummy.next = head    
    temp = dummy
    
    while temp != None:
        
        while temp.next != None and temp.next.data == k:
            temp.next = temp.next.next
            
        temp = temp.next
        
    return dummy.next

def removeNodesI(head, k):
    if not head:return head
    head.next = removeNodes(head.next,k)
    return head if head.data != k else head.next