from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        vis = [[0 for _ in range(M)] for _ in range(N)]
        deltas = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1),
        ]

        def is_valid(cx, cy):
            return 0 <= cx < N and 0 <= cy < M

        def bfs(i, j):
            sum_p = 0
            queue = [(i, j)]
            vis[i][j] = 1
            while len(queue) > 0:
                tx, ty = queue.pop(0)
                for dx, dy in deltas:
                    cx = tx + dx
                    cy = ty + dy
                    if is_valid(cx, cy):
                        if grid[cx][cy] == 0:
                            sum_p += 1
                        if vis[cx][cy] == 0 and grid[cx][cy] == 1:
                            vis[cx][cy] = 1
                            queue.append((cx, cy))
                    else:
                        sum_p += 1
            return sum_p

        # 恰有一个岛屿
        for i, rows in enumerate(grid):
            for j, elem in enumerate(rows):
                if elem and vis[i][j] == 0:
                    return bfs(i, j)


res = Solution().islandPerimeter([[1, 0]])
print(res)
