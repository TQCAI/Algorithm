from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        left = intervals[0][0]
        right = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            itv = intervals[i]
            # 1. 找到覆盖区间
            if left <= itv[0] and right >= itv[1]:
                res += 1
            # 2. 找到相交区间，合并
            if right >= itv[0] and right <= itv[1]:
                right = itv[1]
            if right < itv[0]:
                left = itv[0]
                right = itv[1]
        return len(intervals) - res

