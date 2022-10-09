# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None # pointer to prev node 
        c = head # pointer to current node
        
        # if only one node in list or empty return list 
        if not head or not head.next:
            return head
        
        n = head.next # pointer to next node
        
        #iterate thorugh list
        while c:
            # make curr point to prev
            c.next = p 
            # move all three pointers down one spot in list
            p = c 
            c = n
            # when n is null we do not want to access n.next
            if n and n.next:
                n = n.next
            else:
                n = None

        return p
            