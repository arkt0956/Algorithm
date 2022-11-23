import collections
from typing import List

dicts = collections.defaultdict(int)


class TwoSum:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            partner = target - v
            if partner in dicts:
                return [dicts[partner], i]
            else:
                dicts[v] = i

input = [2, 7, 11, 15]
target = 9

tsum = TwoSum()
print(tsum.two_sum(input, target))
