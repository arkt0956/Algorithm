from typing import *
import functools
import collections
import heapq
import itertools
import re
import sys
import math
import bisect


class LogOrder:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit, letter = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)

        letter = sorted(letter, key=lambda x: (x.split()[1], x.split()[0]))
        return letter + digit


loging = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let1 own kit dig", "let3 art zero"]

orderLog = LogOrder()
print(orderLog.reorderLogFiles(loging))