import collections


class RemoveDuplication:
    def remove_duplicate(self, s: str) -> str: #알파벳 순서로 정렬하여 어떤 문자가 먼저 와야하는 지 판별
        # for char in sorted(set(s)):
        #     substr = s[s.index(char):]
        #     if set(substr) == set(s):
        #         return char + self.remove_duplicate(substr.replace(char, ''))
        #
        # return ''
        counter, seen, stack = collections.Counter(s), set(), []
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)

input = "bcabc"
removed = RemoveDuplication()
print(removed.remove_duplicate(input))