class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        strs = ["Hello","World"]
        """
        if len(strs) == 0:
            return 'NONE'

        string = '/t'.join(strs)
        return string

    def decode(self, s: str) -> List[str]:
        if s == 'NONE':
            return []
        strings = s.split('/t')
        return strings
