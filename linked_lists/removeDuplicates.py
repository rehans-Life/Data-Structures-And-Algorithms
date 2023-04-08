class Solution:
    def deleteDuplicates(self, head):

        if head == None or head.next == None:
            return head

        head.next = self.deleteDuplicates(head.next)

        if head.val == head.next.val:
            return head.next

        return head

def deleteDuplicates(self,head):
    
    temp = head

    while temp != None:
        
        while temp.val == temp.next.val:
            temp.next = temp.next.next 
        
        temp = temp.next