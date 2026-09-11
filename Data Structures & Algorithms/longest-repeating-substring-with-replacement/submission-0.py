from collections import defaultdict

class Solution:
    """
    0123456
    AABABBA | k = 1
        l
           r
    res = 4
    {
        A: 1,
        B: 2,
    }
    """
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies_map = defaultdict(int)
        max_freq_seen, res = 0, 0
        l, r = 0, 0

        while r < len(s):
            frequencies_map[s[r]] += 1
            max_freq_seen = max(max_freq_seen, frequencies_map[s[r]])

            while (r - l + 1) - max_freq_seen > k:
                frequencies_map[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res
