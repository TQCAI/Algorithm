from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        f = [1]  # 以 i 结尾的区间序列的最大值
        N = len(intervals)
        for i in range(1, N):
            f.append(
                max(
                    (f[j] for j in range(i)
                     if intervals[j][1] <= intervals[i][0]),
                    default=0)
                + 1)
        return N - max(f)
