from typing import *
import functools
import collections
import heapq
import itertools
import re
import sys
import math
import bisect


class Mostword:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub('\W', ' ', paragraph)
        words = [word for word in words.lower().split() if word not in banned]
        dicts = collections.defaultdict(int)
        for word in words:
            dicts[word] += 1

        return max(dicts, key=dicts.get)


iparagraph = "The main opposition Democratic Party of Korea (DPK) ratcheted up pressure on the presidential office " \
             "during a National Assembly audit of the office, \
            Tuesday, to replace Cabinet members, including the interior and safety minister, " \
             "and ranking police officers for their inadequate response to the Itaewon crowd crush." \
             "During a separate meeting by the National Assembly Special Committee on Budgets and Accounts, DPK Rep. " \
             "Jun Hye-sook questioned Prime Minister Han Duck-soo, citing complaints made by young Koreans " \
             "that there was no government overseeing the safety of citizens at the moment of the tragedy. " \
             "The prime minister replied that there was no government at the moment of the incident, " \
             "because those keeping public order in the Yongsan area were reacting inappropriately."

ibanned = ["DPK","the","of","and"]

target_word = Mostword()
print(target_word.mostCommonWord(iparagraph,ibanned))
