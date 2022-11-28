from typing import List


class Temperatures:
    def daily_temper(self, t: List) -> List:
        stack = []
        output = [0] * len(t)
        for cur, val in enumerate(t):
            while stack and t[stack[-1]] < val:
                last = stack.pop()
                output[last] = cur - last
            stack.append(cur)
        return output


T = [73, 74, 75, 71, 69, 72, 76, 73]
temp = Temperatures()
print(temp.daily_temper(T))