import logging
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product_array = []
        prefix_partial_product_acc = 1
        for i in range(len(nums)):
            prefix_product_array.append(prefix_partial_product_acc * nums[i])
            prefix_partial_product_acc = prefix_product_array[i]

        postfix_product_array = [1] * len(nums)
        postfix_partial_product_acc = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix_product_array[i] = postfix_partial_product_acc * nums[i]
            postfix_partial_product_acc = postfix_product_array[i]
        logging.debug(f'prefix_product_array: {prefix_product_array} | postfix_product_array: {postfix_product_array}')
        
        result = []
        for i in range(len(nums)):
            prefix = prefix_product_array[i-1] if i > 0 else 1
            postfix = postfix_product_array[i+1] if i < len(nums) - 1 else 1
            result.append(prefix * postfix)
        return result

if __name__ == '__main__':
    """
    [1,2,4,6]
    [1,2,8,48] - LR / prefix
    [48,48,24,6] - RL / postfix

    [-1,0,1,2,3]
    safe_total = -6
    [0,0,0,0] -> [0,-6,0,0,0]

    NS: 
    """
    logging.basicConfig(level=logging.INFO)