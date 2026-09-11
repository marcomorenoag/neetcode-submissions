class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        {
            p: 5,
            w: 6,
            k: 3,
            e: 4,
        }
        max_str = 4

         0123456
        "pwwkepw"
            l
               r
        """
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1
        
        max_str = 1
        l_ptr, r_ptr = 0, 0
        char_to_idx_map: dict[str, int] = {}

        while r_ptr < len(s):
            if (
                s[r_ptr] in char_to_idx_map and
                char_to_idx_map[s[r_ptr]] >= l_ptr
            ):
                l_ptr = char_to_idx_map[s[r_ptr]] + 1
            else:
                max_str = max(max_str, r_ptr - l_ptr + 1)
            char_to_idx_map[s[r_ptr]] = r_ptr
            r_ptr += 1
        
        return max_str