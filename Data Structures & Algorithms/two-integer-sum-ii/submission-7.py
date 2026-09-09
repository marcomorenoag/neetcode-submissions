import logging

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum == target:
                break
            elif current_sum < target:
                l += 1
            else:
                r -= 1
        return [l+1, r+1]

def main() -> None:
    pass

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()