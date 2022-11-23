from typing import *
import functools
import collections
import heapq
import itertools
import re
import sys
import math
import bisect


class Palindrome:
    def isPalindrome(self, s: str) -> bool:
        words = [word for word in re.sub('[^a-z0-9]', '', s.lower())]
        return words == words[::-1]

    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> List[str]:
            while left > 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        # 길이가 너무 짧을때 / 전체가 Palindrome 일 때
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""
        for i in range(len(s)):
            result = max(result, expand(i,i+1),expand(i,i+2),key=len)

        return result


ex1 = "A man, a plan, a canal: Panama"
ex2 = "race a car"

palin = Palindrome()
# print(palin.isPalindrome(ex1))
# print(palin.isPalindrome(ex2))

ex3 = "babad"
ex4 = "cbbd"

print(palin.longestPalindrome(ex3))
print(palin.longestPalindrome(ex4))
