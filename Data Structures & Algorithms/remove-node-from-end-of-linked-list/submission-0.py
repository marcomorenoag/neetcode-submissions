# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _get_total_nodes(self, head: ListNode) -> int:
        total_nodes = 0
        tail = head
        while tail:
            total_nodes += 1
            tail = tail.next
        return total_nodes

    def _remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        curr = head
        prev = None
        visited_nodes = 1
        while visited_nodes < n:
            visited_nodes += 1
            prev = curr
            curr = curr.next
        prev.next = curr.next

    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        '''
        Things needed:
        1. Tail of the linked list?
        2. Count jumps between nodes starting from tail towards the head
        3. At "n", remove it
        '''
        if head is None:
            return None
        
        # Find the total nodes of the linked list
        total_nodes = self._get_total_nodes(head)
        if total_nodes == 1:
            return None
        
        target_nth_node = total_nodes + 1 - n # Adding 1 b/c needed to count the tail

        # Base case: attempting to remove the head, then directly return its next
        if target_nth_node == 1:
            return head.next

        # Traverse the list until nth node to be removed
        self._remove_nth_from_end(head, target_nth_node)
        
        return head
