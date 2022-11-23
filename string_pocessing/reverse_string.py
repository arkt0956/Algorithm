from typing import *
import functools
import collections
import heapq
import itertools
import re
import sys
import math
import bisect


class Restring:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


ex1 = ["h", "e", "l", "l", "o"]
ex2 = ["h", "a", "n", "n", "a", "h"]

rstrs = Restring()
rstrs.reverseString(ex1)
print(ex1)
print(ex2)
