[剑指 Offer 13. 机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)

```python
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        ans = 0
        vis = [[0] * n for _ in range(m)]
        queue = collections.deque()
        queue.append([0, 0])
        ans += 1
        vis[0][0] = 1
        while queue:
            tx, ty = queue.popleft()
            for dx, dy in zip([0, 0, -1, 1], [1, -1, 0, 0]):
                x, y = tx + dx, ty + dy
                if 0 <= x < m and 0 <= y < n and (not vis[x][y]) and sum([int(s) for s in f"{x}{y}"]) <= k:
                    queue.append([x, y])
                    ans += 1
                    vis[x][y] = 1
        return ans
```