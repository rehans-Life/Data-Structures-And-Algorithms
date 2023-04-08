class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def merge2Lists(l1,l2):
    dummy = ListNode()
    tail = dummy

    if l1 == None:
        return l2
    
    if l2 == None:
        return l1

    while l1 != None and l2 != None:
        
        if l1.val < l2.val:
            tail.next = l1
            tail = l1
            l1 = l1.next
        else:
            tail.next = l2
            tail = l2
            l2 = l2.next

    if l2 == None:
        tail.next = l1
    
    if l1 == None:
        tail.next = l2
    
    return dummy.next


def mergeKLists(lists):

    if not lists or len(lists) == 0:
        return None 
    
    # My Lists size is going to keep on reducing after iteration of this while loop when it reaches one which means i now have only
    # one sorted linked lists in my lists array and i can just return it.
    while len(lists) > 1:

        # We will be storing all the mergedLists which are merged in pairs of two inside of this array
        mergedLists = []

        # Since i need to merge in pairs of two I will be taking two steps after each iteration so after each iteration my i value is 
        # pointing towards the next unused linked lists that i need to merge.
        for i in range(0,len(lists),2):
            l1 = lists[i]

            # This is the condition for having odd numbers of linked lists given to merge because there will always be one list that wont
            # be able to form a group of two with another node.
            l2 = lists[i+1] if (i+1) < len(lists) else None

            # Appending the sorted merged pair into the linked lists.
            mergedLists.append(merge2Lists(l1,l2))
        
        # In order to merge the remaining merged linked lists i set my lists equal to my mergedLists so it the next iteration i can
        # merge the remaining pairs as well.
        lists = mergedLists
    
    # Returning the final merged sorted linked lists.
    return lists[0]
