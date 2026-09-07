import logging
import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 0. Base cases
        if k < 1:
            return []
        if len(nums) == 1 and k == 1:
            return nums
        # 1
        num_to_freq_map: Dict[int, int] = defaultdict(int)
        for num in nums:
            num_to_freq_map[num] += 1
        logging.debug(f'num_to_freq_map: {num_to_freq_map}')
        freq_to_num_map: Dict[int, List[int]] = defaultdict(list) # reversed map
        for key,val in num_to_freq_map.items():
            freq_to_num_map[val].append(key)
        logging.debug(f'freq_to_num_map: {freq_to_num_map}')

        # 2 & 3
        max_heap_frequencies = []
        for frequency in num_to_freq_map.values():
            heapq.heappush(max_heap_frequencies, -frequency)
        logging.debug(f'max_heap_frequencies: {max_heap_frequencies}')

        # 4
        top_k_nums = []
        counted = 0
        already_visited = set()
        """
        top_k_nums = [7]
        counted = 0
        k = 1
        """
        while counted < k:
            top_freq = heapq.heappop(max_heap_frequencies) * -1
            top_nums = freq_to_num_map[top_freq]
            logging.info(f'top_freq: {top_freq} | top_nums: {top_nums} | counted: {counted} | k: {k}')
            for top_num in top_nums:
                if top_num in already_visited:
                    continue
                already_visited.add(top_num)
                top_k_nums.append(top_num)
                counted += 1
                if counted >= k:
                    break
        return top_k_nums
        
        

def main() -> None:
    """
    Hash Map
    k: num -> v: frequency
    {
        1: 1,
        2: 2,
        3: 3,
    }
    Max Heap -> store the frequency
      3
     / \
    2   1
    ---
    1. Build the Hash Map
    2. Iterate over HM to get frequencies
    3. Build a Max Heap of the frequencies
    4. Extract from MH the first K
    5. Map the extracted MH to the nums using the HM
    """
    # sol = Solution()
    # nums = [1,2,2,3,3,3]
    # # k = 2
    # res = sol.topKFrequent(nums, k)
    # logging.debug(f'response: {res}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)
    main()