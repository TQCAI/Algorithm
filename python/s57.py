from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = newInterval
        i = 0
        N = len(intervals)
        res = []
        while i < N and intervals[i][1] < l:
            res.append(intervals[i])
            i += 1
        while i < N and intervals[i][0] <= r:
            l = min(intervals[i][0], l)
            r = max(intervals[i][1], r)
            i += 1
        res.append([l, r])
        res += intervals[i:]
        return res
