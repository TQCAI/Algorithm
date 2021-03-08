import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        pq = []
        vis = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i in (0, m - 1) or j in (0, n - 1):
                    heapq.heappush(pq, (heightMap[i][j], i, j))
                    vis[i][j] = 1
        dirs = [-1, 0, 1, 0, -1]
        ans = 0
        while pq:
            wh, x, y = heapq.heappop(pq)
            for k in range(4):
                nx, ny = x + dirs[k], y + dirs[k + 1]
                if 0 <= nx < m and 0 <= ny < n and vis[nx][ny] == 0:
                    ch = heightMap[nx][ny]
                    ans += max(0, wh - ch)
                    vis[nx][ny] = 1
                    heapq.heappush(pq, (max(wh, ch), nx, ny))
        return ans


print(Solution().trapRainWater([
    [1, 4, 3, 1, 3, 2],
    [3, 2, 1, 3, 2, 4],
    [2, 3, 3, 2, 3, 1]
]))
