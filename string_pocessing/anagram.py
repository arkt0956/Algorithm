from typing import *
import functools
import collections
import heapq
import itertools
import re
import sys
import math
import bisect


class Anagram:
    def groupAnagrams(self, strs: List[str]) -> List[str]:
        dicts = collections.defaultdict(list)
        for str in strs:
            dicts[''.join(sorted(str))].append(str)
        return list(dicts.values())


input = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram = Anagram()
print(anagram.groupAnagrams(input))