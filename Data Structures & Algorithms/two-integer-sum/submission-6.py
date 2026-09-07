import logging

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # k = num -> v = index
        num_to_index_map: Dict[int, int] = {}

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in num_to_index_map:
                return [num_to_index_map[complement], i]
            num_to_index_map[num] = i


    def _twoSum(self, nums: List[int], target: int) -> List[int]:
        # Not enough items
        if len(nums) < 2:
            return []

        # Assumption that always there's a pair
        if len(nums) == 2:
            return [0,1]
        
        map_of_complements: Dict[int, int] = {}
        map_num_to_index: Dict[int, List[int]] = {}

        for idx in range(len(nums)):
            num = nums[idx]
            complement = target - num
            map_of_complements[idx] = complement

            '''if num not in map_num_to_index:
                map_num_to_index[num] = idx'''
            map_num_to_index.setdefault(num, [idx])

        i, j = 0, 1
        for k, v in map_of_complements.items():
            # Check if complement exists in map_num_to_index
            i = k
            logging.debug(f'i: {i}')
            if v in map_num_to_index:
                for num in map_num_to_index[v]:
                    if num != i:
                        j = num
                # if i == j and len(map_num_to_index[v]) > 1:
                #     j = map_num_to_index[v][1]
                return [i, j]
        return [i, j]


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