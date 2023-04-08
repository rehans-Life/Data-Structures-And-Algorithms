def intersection(firstHead,secondHead):	
    # Placing Pointer (p1) at the head of my first linked lists
    p1 = firstHead
    
    # Placing Pointer (p2) at the head of my second linked lists
    p2 = secondHead
    
    # Setting up the iteration and the reason why ive set the condition as True in the 
    # while loop is because the function is going to end within the while loop itself. 
    while True:

        # p2 and p1 will be equal when both of them are pointing towards the intersection node or they will both be None when there is no intersection Node
        if p1 == p2:
            # When there is a intersection Node p1 will not be None in that
            # we will return the intersection nodes data or else if p1 is None             # then there was no intersection Node so we return -1.  
            return p1.data if p1 != None else -1

        # If the p1 ever reaches None then set p1 as the head Node of the second linked
        # list cause initially it pointed at linked list 1
        if p1 == None:
            p1 = secondHead
            continue
            
        # Similarly if p2 ever reaches None then p2 as the head node of first linked
        #list
        if p2 == None:
            p2 = firstHead
            continue
        
        # Traversing p1 to the next node
        p1 = p1.next
        
        # Traversing p2 to the next node
        p2 = p2.next

def findIntersection(firstHead, secondHead):
    # Placing Pointer (p1) at the head of my first linked lists
    p1 = firstHead
    
    # Placing Pointer (p2) at the head of my second linked lists
    p2 = secondHead
    
    # Setting up the iteration and when our Nodes are equal then exit out of the loop. 
    while p1 != p2:

        # If p1 is None then setting to the head of the second linked list else
        # just traversing it by one node.
        p1 = secondHead if p1 == None else p1.next

        # If p2 is None then setting it to the head of the first linked list else
        # just traversing it by one node.
        p2 = firstHead if p2 == None else p2.next

    # If there was a intersection Node then output its data or else if there was
    # no intersection which mean p1 is None then we return -1
    return p1.data if p1 != None else -1