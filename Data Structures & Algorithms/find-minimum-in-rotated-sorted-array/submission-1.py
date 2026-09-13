import logging

class Solution:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
    
    def _find_offset(self, nums: List[int]) -> int:
        # 1.1.
        left_ptr, right_ptr = 0, len(nums) - 1
        while left_ptr < right_ptr:
            if nums[left_ptr] <= nums[right_ptr]:
                left_ptr = right_ptr
                right_ptr = len(nums) - 1
            right_ptr = left_ptr + ((right_ptr - left_ptr) // 2)
        return (right_ptr + 1) % len(nums)

    def findMin(self, nums: List[int]) -> int:
        """
        Q&A
        1. Possible to have duplicates in nums?
        2. Possible to have nums with only a single num?
        3. Elements always increased by 1 or a k constant?
        ---
        Brute Force Solution — O(n)
        1. Iterate thru nums, keeping track of min_val
        2. Return min_val at the end
        ---
        Performant Solution — O(log(n))
         0 1 2 3 4
        [1,2,3,4,5]
        [5,1,2,3,4]
        [3,4,5,1,2]

        [2,3,4,5,1]
               l
               r  
        1. Find the rotation amount (aka offset)
            1.1. Set two pointers l and r
            1.2. while l < r: check nums[l] > nums[r]
                1.2.1. If true:
                    Move r to (r-l)//2
                1.2.2. Otherwise: ordered!
                    offset = len(nums) - (r-l+1)
        2. Return nums[(r+1)%len(nums)]
        """
        # 0. Base Cases
        if len(nums) == 1:
            return nums[0]
        
        # 1.
        offset = self._find_offset(nums)
        logging.debug(f'offset: {offset}')
        
        # 2. Add safety (using %) for avoiding idx overflow
        return nums[offset]


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG)