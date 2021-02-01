from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        right = intervals[0][1]
        N = len(intervals)
        cnt = 1
        for i in range(1, N):
            if intervals[i][0] >= right:
                cnt += 1
                right = intervals[i][1]
        return N - cnt
