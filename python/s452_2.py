from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[0])
        rng = points[0]
        cnt = 1
        for point in points[1:]:
            if rng[1] < point[0]:
                cnt += 1
                rng = point
            else:
                rng = max(rng[0], point[0]), min(rng[1], point[1])
        return cnt


res=Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]])
print(res)
