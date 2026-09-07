import logging
from dataclasses import dataclass, field

@dataclass
class Solution:
    _first_word_hash_map: dict[str, int] = field(init=False, default_factory=dict)
    _second_word_hash_map: dict[str, int] = field(init=False, default_factory=dict)

    def _hash_map_builder(self, word: str, target_map: dict[str, int]) -> None:
        for letter in word:
            # TODO: refactor this with default map and just add it
            if letter in target_map:
                target_map[letter] += 1
            else:
                target_map[letter] = 1

    def _are_maps_diff(self, first_map: Map, second_map: Map) -> bool:
        return first_map == second_map

    def isAnagram(self, s: str, t: str) -> bool:
        # Build hash maps
        self._hash_map_builder(s, self._first_word_hash_map)
        self._hash_map_builder(t, self._second_word_hash_map)

        # Perform comparison
        are_equal = self._are_maps_diff(self._first_word_hash_map, self._second_word_hash_map)
        logging.debug(f'are_equal?: {are_equal}')
        return are_equal



def main() -> None:
    """
    Naiv Sol -> pick s[i] and look for matching in all t
    Perf Sol ->
        1. Iterate over all s and store a hash map char -> appearances
        2. Iterate over all t and build its own hash map
        3. Iterate over both Hash Maps to confirm exact same keys and values
    """
    solution = Solution()
    s = "racecar"
    t = "carrace"
    is_anagram = solution.isAnagram(s, t)
    logging.debug(f'is anagram?: {is_anagram}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
