def mergeLists(list1,list2):
    if list1 == None:
        return list2
    
    if list2 == None:
        return list1
    
    if list1.val < list2.val:
        list1.next = mergeLists(list1.next,list2)
        return list1
    else:
        list2.next = mergeLists(list1,list2.next)
        return list2

def mergeListsI(list1,list2):
    l1 = list1
    l2 = list2
    ans = None
    tail = None

    if l1.val < l2.val:
        ans = l1
        tail = l1
        l1 = l1.next
    else:
        ans = l2
        tail = l2
        l2 = l2.next
 
    while l1 != None and l2 != None:

        if l1.val < l2.val:
            tail.next = l1
            tail = l1
            l1 = l1.next
        else:
            tail.next = l2
            tail = l2            
            l2 = l2.next
    
    if l1 == None:
            tail.next = l2
        
    if l2 == None:
        tail.next = l1   

                    