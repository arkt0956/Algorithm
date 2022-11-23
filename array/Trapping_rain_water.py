from typing import List


class TrappingWater:
    def trapping_rain_water(self, height: List[int]) -> int:
        count_rain: int = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        while left < right:
            if left_max <= right_max:
                count_rain += left_max - height[left]
                left += 1
                if height[left] > left_max:
                    left_max = height[left]
            else:
                count_rain += right_max - height[right]
                right -= 1
                if height[right] > right_max:
                    right_max = height[right]

        return count_rain

    def use_stack(self, height: List[int]) -> int:
        volume = 0
        stack = []
        left = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break
                distance = i - stack[-1] - 1
                water = min(height[i], height[stack[-1]]) - height[top]
                volume += distance*water
            stack.append(i)
        return volume


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

trap = TrappingWater()
print(trap.use_stack(height))