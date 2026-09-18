# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def _find_middle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _slice_list(self, head: ListNode, cutoff: ListNode) -> None:
        tail = head
        while tail.next != cutoff:
            tail = tail.next
        tail.next = None

    def _reverse_in_place_list(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def _merge_lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode()
        tail = head

        # print(f'\nDEBUG @ _merge_lists: {head=} | {tail=} | {list1=} | {list2=}')
        while list1 and list2:
            tail.next = list1
            list1 = list1.next
            tail = tail.next

            tail.next = list2
            list2 = list2.next
            tail = tail.next


        # print(f'\nDEBUG @ _merge_lists: {head=} | {tail=}')
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return head.next
    
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 0. Base cases
        if head is None:
            return

        if head.next is None:
            return
        
        # 1. Find the middle
        middle = self._find_middle(head)
        # print(f'\n#1. Find the middle: {head=} | {middle=}')

        # 2. Slice the first half before the middle
        self._slice_list(head, middle)
        # print(f'\n#2. Slice the first half before the middle: {head=} | {middle=}')

        # 3. Reverse the second half
        reversed_second_half_head = self._reverse_in_place_list(middle)
        # print(f'\n#3. Reverse the 2nd half: {reversed_second_half_head=}')
        
        # 4. Merge both halves
        merged_lists_head = self._merge_lists(head, reversed_second_half_head)
        # print(f'\n#4. Merge both halves: {merged_lists_head=}')

        head = merged_lists_head
        return