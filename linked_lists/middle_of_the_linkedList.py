# Middle Node of a Linked List can easily be found if we know the length of the linked list cause then i can divide the length
# by 2 and that would be the number of times i need to traverse in order to get to the middle node.

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
head = Node(1)

secondNode = Node(2)
head.next = secondNode

thirdNode = Node(3)
secondNode.next = thirdNode

fourthNode = Node(4)
thirdNode.next = fourthNode

fifthNode = Node(5)
fourthNode.next = fifthNode

# Going to find the length of the Linked List.
def len(head):
    i=0
    temp = head
    while temp != None:
        i+=1
        temp = temp.next
    return i

def middleNode(head,length):
    temp = head
    middleIndex = length // 2
    i=0
    while i < middleIndex:
        temp = temp.next
        i+=1
    return {'value':temp.value}

print(middleNode(head,len(head)))

# One iteration a
def middleNode(head):
    temp1 = head
    temp2 = head

    # If temp1 is equal to None which denotes temp1 has reached the end in even numbers of nodes case then we stop cause at this point
    # our temp2 will be pointing at the middle node.

    # If temp1 is at the last node which we can check by checking the if the next attribute is None or not and if it is then it denotes
    # that temp1 has reached the end in odd numbers case so we stop cause at this point our temp2 will be pointing at the middle node.
    
    while temp1 != None and temp1.next != None:
        temp2 = temp2.next
        temp1 = temp1.next.next
    
    return temp2