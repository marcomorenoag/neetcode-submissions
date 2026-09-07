import logging
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1.
        grouped_anagrams_map: Dict[int, List[str]] = defaultdict(list)
        for string in strs:
            freq_chars = [0] * 26
            for char in string:
                idx = ord(char) - ord('a')
                freq_chars[idx] += 1
        # 2.
            grouped_anagrams_map[tuple(freq_chars)].append(string)
        # 3.
        grouped_anagrams = [anagrams for anagrams in grouped_anagrams_map.values()]
        return grouped_anagrams  

def main() -> None:
    """
    NS: all possible combinations -> O(n^2)
    PS:
        1. Calculate a hash value for the sum of letter ASCII codes
        2. That's the key, the value is the actual array of anagrams
        3. Iterate over all values and store them in a linear list
    """
    solution = Solution()
    strs = ["act","pots","tops","cat","stop","hat"]
    result = solution.groupAnagrams(strs)
    logging.debug(f'result: {result}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()