# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Efficient way - O(n)
        1. Iterate from head until curr.next is None (tail)
        2. At each node, update the curr.next and curr.next.next
        ———
        """
        if (head is None):
            return None
        
        prev = head
        current = head.next
        prev.next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev