class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    def __str__(self):
        return str({
            'value':self.value,
            'next':self.next
        })

head = Node(1)
secondNode = Node(2)

# Storing a reference to the second node inside of the next attribute inside of my head node.
head.next = secondNode

thirdNode = Node(3)

# Storing a reference to the third node inside of the next attribute of my second node
secondNode.next = thirdNode

fourthNode = Node(4)

thirdNode.next = fourthNode

def reverseLinkedListI(head):
    prev=None
    curr=head
    nex=curr.next     
    while curr != None:
        curr.next = prev
        prev=curr
        curr=nex
        if curr != None:
            nex = curr.next

reverseLinkedListI(head)

def reverseLinkedListII(head):

       if head == None:
           return None        
        
       def helper(head):

          if head.next == None:
                return head

          reverseHead = helper(head.next)

          head.next.next = head
          head.next = None
            
          return reverseHead
       return helper(head)
       