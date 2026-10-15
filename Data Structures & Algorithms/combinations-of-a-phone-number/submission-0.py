from typing import Final

class Solution:
    _NUMBER_TO_LETTERS_MAP: Final[dict[str, str]] = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def letterCombinations(self, digits: str) -> list[str]:
        '''
        Time Complexity: O(N*4^N) where N is the amount of digits
        Space Complexity: O(N)
        '''
        total_digits = len(digits)
        if total_digits == 0:
            return []

        combinations = []

        def _backtracking(index: int, path: list[str]) -> None:
            # Base condition
            if len(path) == total_digits:
                combinations.append(''.join(path))
                return

            letters = self._NUMBER_TO_LETTERS_MAP[digits[index]]
            for letter in letters:
                path.append(letter)
                _backtracking(index + 1, path)
                path.pop()

        _backtracking(0, [])

        return combinations

    
