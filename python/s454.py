from typing import List
import collections


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        counter = collections.Counter(u + v for u in A for v in B)
        res = 0
        for u in C:
            for v in D:
                tmp = -(u + v)
                if tmp in counter:
                    res += counter[tmp]
        return res
