# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # Base cases
        if lists is None or len(lists) == 0:
            return None

        # Min Heap of size K
        heap = []
        for list_idx, list_head in enumerate(lists):
            if list_head:
                # print(f'{lists=} | {list_head=}')
                heapq.heappush(heap, (list_head.val, list_idx, list_head))
        
        # Traverse the lists while heap is defined — something to check
        pivot_node = ListNode()
        tail = pivot_node
        while heap:
            _, idx, node = heapq.heappop(heap) # Get the min val
            tail.next = node
            tail = tail.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, idx, node))

        return pivot_node.next