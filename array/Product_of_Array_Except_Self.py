from typing import List


class ProductArray:
    def product_except_self(self, nums: List[int]) -> List[int]:
        # left
        result = [1]
        p = 1
        for i in range(len(nums)-1):
            p *= nums[i]
            result.append(p)
        # right
        pr = 1
        for j in range(len(nums)-1, -1, -1):
            result[j] *= pr
            pr *= nums[j]

        return result

nums = [1, 2, 3, 4]
product = ProductArray()
print(product.product_except_self(nums))