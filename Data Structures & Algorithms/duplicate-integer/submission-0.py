import logging
from dataclasses import dataclass, field

@dataclass
class Solution:
    _visited_nums: Set[int] = field(init=False, default_factory=set)

    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if num in self._visited_nums:
                return True
            self._visited_nums.add(num)
        return False

def main() -> None:
    """
    Naive sol -> pick nums[i], compare it against all the others
    More eff ->
        1. Iterate over each list's element
        2. Store them in a Hash Set
        3. Check whether exists there, then return True. Otherwise False
        ---
        Time: O(n) -> n = len(nums)
        ?Space: O(n) -> n = len(nums)
    """
    solution = Solution()
    nums = [1, 2, 3, 3]
    contains_duplicated = solution.hasDuplicate(nums)
    logging.debug(f'\nContains_duplicated?: {contains_duplicated}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.debug('Kick off')
    main()