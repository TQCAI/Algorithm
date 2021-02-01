from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        # 最靠左的右边点
        pos = points[0][1]
        cnt = 1
        for point in points:
            # 这个点左边比【最靠左的右边点】还大
            if point[0] > pos:
                pos = point[1]
                cnt += 1
        return cnt
