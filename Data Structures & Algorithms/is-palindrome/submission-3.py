class Solution:
    def _is_alphanum(self, c: str) -> bool:
        is_upper_case = ord('A') <= ord(c) <= ord('Z')
        is_lower_case = ord('a') <= ord(c) <= ord('z')
        is_number = ord('0') <= ord(c) <= ord('9')
        return is_upper_case or is_lower_case or is_number

    def isPalindrome(self, s: str) -> bool:
        l_ptr, r_ptr = 0, len(s) - 1
        while l_ptr < r_ptr:
            while l_ptr < r_ptr and not self._is_alphanum(s[l_ptr]):
                l_ptr += 1
            while r_ptr > l_ptr and not self._is_alphanum(s[r_ptr]):
                r_ptr -= 1
            if s[l_ptr].lower() != s[r_ptr].lower():
                return False
            l_ptr += 1
            r_ptr -= 1
        return True