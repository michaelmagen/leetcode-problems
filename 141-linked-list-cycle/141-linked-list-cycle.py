# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c = head
        visited = set()
        while c:
            if c and c in visited:
                return True
            elif c:
                visited.add(c)
            c = c.next
        return False
        