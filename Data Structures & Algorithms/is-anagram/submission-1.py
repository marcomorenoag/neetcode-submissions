import logging

class Solution:
    def _hash_map_builder(self, word: str) -> dict[str, int]:
        counts = {}
        for letter in word:
            counts[letter] = counts.get(letter, 0) + 1
        return counts

    def _are_maps_equal(self, first_map: dict[str, int], second_map: dict[str, int]) -> bool:
        return first_map == second_map

    def isAnagram(self, s: str, t: str) -> bool:
        # Base case
        if len(s) != len(t):
            return False
        
        # Build hash maps
        first_map = self._hash_map_builder(s)
        second_map = self._hash_map_builder(t)

        # Perform comparison
        are_equal = self._are_maps_equal(first_map, second_map)
        logging.debug(f'are_equal?: {are_equal}')
        return are_equal


def main() -> None:
    """
    Naiv Sol -> pick s[i] and look for matching in all t
    Perf Sol ->
        1. Iterate over all s and store a hash map char -> appearances
        2. Iterate over all t and build its own hash map
        3. Iterate over both Hash Maps to confirm exact same keys and values
        ---
        Time: O(s + t) -> O(n)
        Space: O(s + t) -> O(n)
    """
    solution = Solution()
    s = "racecar"
    t = "carrace"
    is_anagram = solution.isAnagram(s, t)
    logging.debug(f'is anagram?: {is_anagram}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
