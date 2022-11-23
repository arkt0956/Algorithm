import sys
import time
from typing import List

start = time.time()


class TradeStock:
    def max_profit(self, nums: List[int]) -> int:
        min_value = sys.maxsize
        profit = 0
        # for i, num in enumerate(nums):
        #     if min_value > num:
        #         min_value = num
        #         profit = max(nums[i:]) - min_value
        for num in nums:
            min_value = min(min_value, num)
            profit = max(profit, num - min_value)
        return profit


prices = [7, 1, 5, 3, 6, 4]
stock = TradeStock()
print(stock.max_profit(prices))

print("성능: ", time.time() - start)