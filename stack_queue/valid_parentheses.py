class ValidParentheses:
    def is_valid(self, s: str) -> bool:
        stack = []
        dicts = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        for char in s:
            if char in dicts:
                stack.append(char)
                continue
            if not stack or dicts[stack[-1]] != char:
                return False
            stack.pop()

        return len(stack) == 0


input = ")([]{}"
target = ValidParentheses()
print(target.is_valid(input))
