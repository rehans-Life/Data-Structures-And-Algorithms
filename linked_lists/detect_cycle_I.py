def detectCycle(self, head):
        #    Write your code here
        #    Return the node where the cycle begins
        p1 = head
        p2 = head
        
        # If p1 becomes None or if its points to a node whose pointer is None
        # then that means we exit out of the while cause we finished traversing
        # through the linked list and we have also found out that it is not a 
        # cycle linked list
        while p1 != None and p1.next != None:            

            p1 = p1.next.next
            
            # Finding the meeting point of p1 and p2 if the linked list is a cycle.
            if p1 == p2:
                break  
            
            p2 = p2.next  
        
        if p1 == None or p1.next == None:
            return -1
        
        # Now our p1 and p2 are bothing pointing towards their meeting points
        # So we can create a new point pt1 to start traversing from that meeting
        # point
        pt1 = head
        
        # Creating another pointer which is going to start from our head node
        pt2 = p2
        
        # The reason why we need the second pointer is that because the point
        # where they both meet is going to be our starting point.
        
        # We keep traversing them until they meet 
        while pt1 != pt2:
            pt1 = pt1.next
            pt2 = pt2.next
        
        # After they have met then that means they are both pinting towards the
        # starting nodes of our cycle.
        return pt1