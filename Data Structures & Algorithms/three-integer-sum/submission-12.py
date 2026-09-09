import logging
from typing import Tuple

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        nums[i] + nums[j] + nums[k] == 0
        -nums[i] == nums[j] + nums[k]
        ---
        [-1,0,1,2,-1,-4]
        """
        triplets: set[Tuple[int, int, int]] = set()
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                nums_sum = nums[j] + nums[k]
                target = nums[i] * -1
                if nums_sum == target:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums_sum > target:
                    k -= 1
                else:#nums_sum < target:
                    j += 1
        return [list(t) for t in triplets]


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
