import logging
from typing import Final

_OPENING_CHARS: Final[Set[str]] = { '(', '{', '['}
_CLOSE_TO_OPEN_CHAR_MAP: Final[Dict[str, str]] = {
    ')': '(',
    '}': '{',
    ']': '['
}

class Solution:
    def isValid(self, s: str) -> bool:
        """
        1. Iterate thru chars in s
        2. Add in a Stack, the opening chars
        3. Whenever a closing char appears, pop from Stack and compare them
        4. If invalid or at the end the Stack has elements, return False
        """
        if len(s) < 2:
            return False
        
        stack = []
        for c in s:
            if c in _OPENING_CHARS:
                stack.append(c)
            else:
                if len(stack) == 0 or _CLOSE_TO_OPEN_CHAR_MAP[c] != stack.pop():
                    return False
        return True and len(stack) == 0

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)