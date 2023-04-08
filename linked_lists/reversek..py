class Solution:

    def reverseGroup(self,s,e):
        prev = None
        curr = s
        nex = curr.next

        # If our current node becomes equal to the node next to our end node then we have to stop reversing 
        # cause that would mean that we have reversed the linked list till the end node.
        while curr != e.next:
            curr.next = prev
            prev = curr
            curr = nex
            if curr != None:
                nex = curr.next  # nex.next     

    def reverseKGroup(self, head, k: int):

        if head == None or head.next == None or k == 1:
            return head
        
        # We reverse from k number of nodes starting from the head node ourseleves and recursion
        # does the rest for us.

        # The node from where we want to start our reversal.
        s = head

        # The node till where we want to reverse the linked list.
        e = head

        # Our end node is pointing towards the head node but we need to move it k-1 steps ahead why not k
        # because we are already at our head node.
        i = 1

        while i != k:
            
            e = e.next

            # If we werent able to form a group of k that we are supposed too which we can identify if our e 
            # is even pointing to None or not. If it is then that means we werent able to form a group of k 
            # cause of not having enough nodes in the linked lists.

            # Then its given in the question to return that part of the linked list as it is.

            if e == None:
                return head

            i+=1
        
        
        # Reversing the rest of the linked list in groups of k
        nextHeadNode = self.reverseKGroup(e.next,k)

        # Reversing the first k number of nodes ourselves and then making recursion do the rest.
        self.reverseGroup(s,e)

        # Since our linked list is reversed our head node is the ending node now
        s.next = nextHeadNode    

        # Then we return the head node which is going to be our ending node.
        return e


# Revision:

class Solution:
    def reverseGroup(self,s,e):
        prev=None
        curr = s
        nex = curr.next

        while prev != e:
           curr.next = prev
           prev = curr
           curr = nex
           nex = curr.next # nex.next 

    def reverseKGroup(self,head,k):

        s = head

        e = head

        i = 0
        while i < (k-1):
            e = e.next
            i+=1 
        
        # If I reverse from the start to end before making the recursive
        # call for the part of the linked list after my end node
        
        # Then the pointer of end node will change therefore it will
        # no longer point towards the remaining part of the linked list
        # that is going to be reversed by the recursive call therefore 
        # I need to make the recursive call before i reverse the 
        # initial part of the linked list 

        nextHeadNode = self.reverseKGroup(e.next,k)

        self.reverseGroup(s,e)

        s.next = nextHeadNode

        # Returning the end node in the end cause its the head now
        # after reversal
        return e

# Approach II:

class Node:
    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next

def reverse(s,e):
    
    # Creating thee pointers one for the previous node one for the 
    # current node and one for the next node.
    p,c,n = None,s,s.next

    while p != e:
        c.next = p
        p = c
        c = n
        if c != None:
            n = c.next

def reverseKGroupsII(head,k):

    # Creating a dummy node to be placed in the start of my linked list
    # and its initially going to be the beforeStart Node.

    dummy = Node()
    dummy.next = head
    beforeStart = dummy

    # placing the end node at my head 
    e = head

    # We create a counter i which tells up till where we have traversed
    # inside of our array.
    i = 0

    # Creatig a while loop that ends when we reach the end of the while
    # loop.
    while e != None:
        
       i+=1 

       # Then we check if we have created a group of k elements or not 
       # by checking if the ith value is a multiple of k or not.

        # Now this is the case where we need to reverse the group
        # that we have created up until now

       if i%k == 0:
        
        # Creating pointers
        s = beforeStart.next
        temp = e.next

        # Perform reversal
        reverse(s,e)

        # We want to connect the reversed linked list back inside of the
        # linked list
        beforeStart.next = e
        s.next = temp

        # We want to create a setup for our forming our next group as well
        beforeStart = s
        e = temp
       
       else:
        # If we havent created a group of three by now we keep on 
        # incrementing the end so we want get to a group of three
        e = e.next 

    # After we have finished our iteration we return our head node
    # which is going to be next to the dummy node
    return dummy.next     




