import logging
from collections import defaultdict

class Solution:
    def _gen_hash(self, s: str) -> Dict[str, int]:
        hash_t = defaultdict(int)
        for c in s:
            hash_t[c] += 1
        return hash_t

    def minWindow(self, s: str, t: str) -> str:
        # Base cases
        if len(t) == 0:
            return ""
        
        # Building two hash maps    
        target_frequency_map = self._gen_hash(t)
        window = defaultdict(int)

        l = 0
        chars_accomplished, chars_needed = 0, len(target_frequency_map)
        res: Tuple[int, List[int, int]] = (float('inf'), [])
        # logging.debug(f'target_frequency_map: {target_frequency_map} | chars_needed: {chars_needed}')

        for r in range(len(s)):
            char = s[r]
            window[s[r]] += 1

            if char in target_frequency_map and window[char] == target_frequency_map[char]:
                chars_accomplished += 1

            # logging.debug(f'window: {window} | chars_accomplished:{chars_accomplished}')
            while chars_accomplished == chars_needed:
                # Update result
                if (r - l + 1) < res[0]:
                    res = ((r - l + 1), [l, r])

                # Pop from left and move left ptr
                window[s[l]] -= 1
                if s[l] in target_frequency_map and window[s[l]] < target_frequency_map[s[l]]:
                    chars_accomplished -= 1
                l += 1

        # Extract and expand targeted indexes
        # logging.debug(f'res: {res}')
        if (res[0] == float('inf') and len(res[1]) == 0):
            return ""
        [l, r] = res[1]
        return s[l:r+1]

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
