class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
head = Node(1)

secondNode = Node(0)

head.next = secondNode

thirdNode = Node(1)

secondNode.next = thirdNode

def binaryToDecimalI(head):

    length = 0
    temp = head

    while temp != None:
        length+=1
        temp = temp.next

    temp = head
    i = 1
    ans = 0

    while temp != None:
        ans += temp.value * (2 ** (length - i))
        temp = temp.next 
        i+=1

    return ans

print(binaryToDecimalI(head))

def binaryToDecimal(head):

    # Creating a variable which is going to store my answer.
    ans  = 0

    # Initiating my temp variable to the head node.
    temp = head

    while temp != None:

        # Since a node next to the previous node which i considered to be the last node exists if i enter this while loop
        # So i multiply the previus answer by two this will increment each previous nodes value by multiple of 2.
        ans *= 2

        # Since im assuming my current node to be the last node now then i multiply its value by 2 raise to the power 0 and i 
        # increment my asnwer by the output
        ans += temp.value * (2**0)

        # Then i point my temp variable to the next node in the list if there exists one.
        temp = temp.next 