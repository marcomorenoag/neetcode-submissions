import logging

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Not enough items
        if len(nums) < 2:
            return []

        # Assumption that always there's a pair
        if len(nums) == 2:
            return [0,1]

        # k = num -> v = index
        num_to_index_map: Dict[int, int] = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_to_index_map:
                return [num_to_index_map[complement], i]
            num_to_index_map[nums[i]] = i


def main() -> None:
    """
    Naive Sol -> for each num in nums, check all the combinations/sums with the rest of nums - O(n^2)
    Perf Sol -> assuming that nums are ordered incrementally
        1. Two indices i & j
        2. Perform sum of nums[i] + nums[j]
        3. If sum is < target, move j++, otherwise (sum > target) move i++

        nums=[3,2,3]
        t=6
        {
            0: 3,
            1: 4,
            2: 3,
        }
        {
            3: [0, 2],
            2: [1],
        }

        [4,5,6,7,8] 13
        t - i
        i -> delta t - nums[i]
        {
            0: 9, -> 3
            1: 8, -> 4
            2: 7, -> 3
            3: 6,
            4: 5,
        }
        {
            3: [0, 1],
            2: 1,
        }
        {
            4: 0,
            5: 1,
            6: 2,
            7: 3,
            8: 4,
        }
    """
    solution = Solution()
    nums = [3,4,5,6]
    t = 7
    logging.debug(f'result: {solution.twoSum(nums, t)}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()