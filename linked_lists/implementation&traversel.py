# Creating a Node class which is going to be initiated with a value and next instance attributes value stores
# the value which is going to be stored by the node and the next attribute is initially set to None cause it needs
# to be manually set to point towards the next node which is created within the linked list.
  
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
head = Node(1)
secondNode = Node(2)

# Storing a reference to the second node inside of the next attribute inside of my head node.
head.next = secondNode

thirdNode = Node(3)

# Storing a reference to the third node inside of the next attribute of my second node
secondNode.next = thirdNode

fourthNode = Node(4)

thirdNode.next = fourthNode

def traversal(head):

    # Storing the head inside of a tempory variable cause i have to keep changing temp continously.  
    temp = head

    while temp != None:
        # Printing the nodes value to which temp is currently pointing too.
        print(temp.value)

        # After printing the current nodes value im going to set temp to the next node in the list
        # so upon next iteration i can print its value. 
        temp = temp.next
