# The deletion of a particular node when you are given the node to be deleted itself is done by replacing
# the data and next attribute values of the node to be deleted by the data and next attribute values of the 
# node next to it.

def deleteNode(node):
    # Write your code here.
    
    # Storing the next node from the node to be deleted inside of a tempory variable
    temp = node.next
    
    # Setting the value of node to be deleted to the node next to it
    node.data = temp.data
    
    # Also change the reference of the node to be deleted to the 
    # next nodes reference
    node.next = temp.next
    
    del temp