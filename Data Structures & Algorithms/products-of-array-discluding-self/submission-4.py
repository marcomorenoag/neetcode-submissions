import logging
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # NS
        # result = []
        # for i in range(len(nums)):
        #     total = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             j += 1
        #         else:
        #             total *= nums[j]
        #     result.append(total)
        # return result

        total_zeros = [num for num in nums if num == 0]
        if len(total_zeros) > 1:
            return [0] * len(nums)
        
        total = math.prod(nums)
        safe_total = math.prod([num for num in nums if num != 0])
        products = [total] * len(nums)
        logging.debug(f'total: {total} | safe_total: {safe_total} | products: {products}')
        for i in range(len(nums)):
            product = products[i]
            num = nums[i]
            if product == 0 and num == 0:
                products[i] = int(safe_total)
            else:
                products[i] = int(products[i] / nums[i])
        return products

if __name__ == '__main__':
    """
    [1,2,4,6]
    safe_total = 48
    [48,48,48,48] -> [48,24,12,8]

    [-1,0,1,2,3]
    safe_total = -6
    [0,0,0,0] -> [0,-6,0,0,0]

    NS: 
    """
    logging.basicConfig(level=logging.INFO)