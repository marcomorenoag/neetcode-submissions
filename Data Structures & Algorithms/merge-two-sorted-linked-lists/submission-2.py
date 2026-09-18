# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        '''
        - Two pointers, one at each list
        - Check what's the lowest value, append it and move the ptr
        - Repeat until both are exhausted
        '''
        l1_head = list1
        l2_head = list2
        l1_tail = l1_head
        l2_tail = l2_head

        # Merge both lists into list1
        while l1_head and l2_head:
            # print(f'{l1_head=} | {l2_head=} | {tail=}')
            if l1_head.val < l2_head.val:
                # tail = l1_head
                l1_head = l1_head.next
            else:
                next_node = l1_head.next
                l1_head.next = l2_head
                # tail = l2_head
                pivot = l2_head.next
                l2_head.next = next_node
                l2_head = pivot
        print(f'{l1_head=} | {l2_head=} | {tail=}')

        # Remaining items in list2
        # if not l1_head and l2_head:
        #     tail.next = l2_head
        # if not l2_head and l1_head:
        #     tail.next = l1_head

        return list1
    
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Base cases
        if not list1 and not list2:
            return None
        
        if list1 and not list2:
            return list1

        if list2 and not list1:
            return list2

        # Dynamic logic
        merged_list = None
        l1 = list1
        l2 = list2

        if list1.val < list2.val:
            merged_list = ListNode(list1.val)
            l1 = l1.next
        else:
            merged_list = ListNode(list2.val)
            l2 = l2.next
        head = merged_list

        while l1 and l2:
            if l1.val < l2.val:
                merged_list.next = ListNode(l1.val)
                l1 = l1.next
            else:
                merged_list.next = ListNode(l2.val)
                l2 = l2.next
            merged_list = merged_list.next
        
        if l1 and not l2:
            merged_list.next = l1
        if l2 and not l1:
            merged_list.next = l2

        return head

