from typing import List

class Partition:
    def array_pair_sum(self, nums: List[int]) -> int:
        # nums.sort(reverse=True)
        # sum: int = 0
        # for i, v in enumerate(nums):
        #     if i % 2 != 0:
        #         sum += v
        # return sum
        return sum(sorted(nums)[::2])


array = [1, 4, 3, 2]
p = Partition()
print(p.array_pair_sum(array))