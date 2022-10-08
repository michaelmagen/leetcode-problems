# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node to avoid initial empty list edge case
        dummy = ListNode()
        # keep track of the tail of the list
        tail = dummy 
    
        #iterate through lists
        while list1 and list2:
            # add lower value from lists
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
          # since we have added something to list move our tail pointer
            tail = tail.next
            
        # we have gone through one list completely, add the other list add the end
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
    
        return dummy.next
                
        