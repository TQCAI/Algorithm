from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for itv in intervals:
            if res and itv[0] < res[-1][1]:
                res[-1][1] = max(res[-1][1], itv[1])
            else:
                res.append(itv)
        return res
