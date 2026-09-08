import re
import logging

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_without_spaces = s.replace(" ", "")
        sanitized_string = "".join(re.findall(r'\w', string_without_spaces))
        init_ptr, end_ptr = 0, len(sanitized_string) - 1
        logging.debug(f'sanitized_string: {sanitized_string} | init_ptr: {init_ptr} | end_ptr: {end_ptr}')

        while init_ptr <= end_ptr:
            if sanitized_string[init_ptr].lower() != sanitized_string[end_ptr].lower():
                return False
            init_ptr += 1
            end_ptr -= 1
        return True
        
logging.basicConfig(level=logging.INFO)