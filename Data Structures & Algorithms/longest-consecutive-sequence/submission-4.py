import logging

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [2,20,4,10,3,4,5]
         i
         j
        nums[j] == highest_num_seen+1
        highest_num_seen = 5
        counter = 4
        max_consecutive = max(max_consecutive, counter)

        TC: O(n^2)
        ---
        [2,3,4,4,5,10,20]

        TC: O(n*log(n))

        ---
        1. Traverse the array and build a Hash Set
        2. Traverse the array, check whether nums[i]+1 exists into the HS
            2.1. If does, push nums[i]+1 in a new list/queue
            2.2. Otherwise, continue
        3. Return the length of the list/queue
        
        """
        # 1.
        hash_set = set(nums)
        longest = 0

        # 2. & 3.
        for num in nums:
            if num - 1 not in hash_set:
                offset = 0
                while (num + offset) in hash_set:
                    offset += 1
                longest = max(longest, offset)
        return longest

def main() -> None:
    pass
    # sol = Solution()
    # nums = [2,20,4,10,3,4,5]
    # sol.longestConsecutive(nums)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()