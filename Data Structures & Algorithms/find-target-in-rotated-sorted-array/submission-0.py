from typing import Final

class Solution:
    _NOT_FOUND_INDEX: Final[int] = -1

    def _find_offset_k(self, nums: List[int]) -> int:
        left_ptr, right_ptr = 0, len(nums) - 1
        while left_ptr < right_ptr:
            if nums[left_ptr] <= nums[right_ptr]:
                left_ptr = right_ptr
                right_ptr = len(nums) - 1
            right_ptr = left_ptr + ((right_ptr - left_ptr) // 2)
        return (right_ptr+1)%len(nums)

    def _find_target(self, nums: List[int], target: int, offset: int) -> int:
        left_ptr, right_ptr = 0, len(nums) - 1
        while left_ptr <= right_ptr:
            middle_ptr = left_ptr + (right_ptr - left_ptr) // 2
            # Found
            if nums[(middle_ptr+offset)%len(nums)] == target:
                return (middle_ptr+offset)%len(nums)
            # Move left ptr
            if nums[(middle_ptr+offset)%len(nums)] < target:
                left_ptr = middle_ptr + 1
            else: # Move right
                right_ptr = middle_ptr - 1
        return self._NOT_FOUND_INDEX


    def search(self, nums: List[int], target: int) -> int:
        """
        Brute Force — O(n)
        1. Iterate over nums
        2. Check if nums[i] is target
        3. Return it
        ———
        Performant — O(log(n)) using Binary Search
        1. Find the offset k
        2. Peform Binary Search, always increasing target index +k times — to consider the offset

                   m
        [1,3,5]
         0 1 2 3 4 5 6
        [5,1,3] | target = 1 (k=1)
         l
                      r
             m
        """
        # 0. Base case
        if len(nums) == 1:
            return 0 if nums[0] == target else self._NOT_FOUND_INDEX

        # 1.
        k_offset = self._find_offset_k(nums)

        # 2.
        found_index = self._find_target(nums, target, k_offset)

        return found_index
