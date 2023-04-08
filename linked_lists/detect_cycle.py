def detectCycle(head) :
    # Write your code here.
    p1 = head
    p2 = head
    
    while p1 != None and p1.next != None:
        
        p1 = p1.next.next
                
        if p1 == p2:
            return True
        
        p2 = p2.next
        
    return False