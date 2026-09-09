import logging

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        [1,8,6,2,5,4,8,3,7]
         i               j
        width = j - i
        large = min(height[i], height[j])
        max_container = 8
        """
        max_container = 0
        l, r = 0, len(height) - 1
        while l < r:
            width = r - l
            large = min(height[l], height[r])
            area = width * large
            max_container = max(max_container, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_container

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)