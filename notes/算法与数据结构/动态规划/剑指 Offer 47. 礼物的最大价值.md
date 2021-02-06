[剑指 Offer 47. 礼物的最大价值](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/)

[面试题47. 礼物的最大价值（动态规划，清晰图解）](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/solution/mian-shi-ti-47-li-wu-de-zui-da-jie-zhi-dong-tai-gu/)

```python
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        dp=grid.copy()
        # M 行 N 列
        M = len(grid)
        N = len(grid[0])
        # 利用Python负索引的性质，在最后追加一圈0
        dp.append([0]*N)
        for row in dp:
            row.append(0)
        ans = 0
        for i in range(M):
            for j in range(N):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                ans=max(ans,dp[i][j])
        return ans
```

多开一行一列的空间能够让代码更简洁

```java
class Solution {
    public int maxValue(int[][] grid) {
        int row = grid.length;
        int column = grid[0].length;
        //dp[i][j]表示从grid[0][0]到grid[i - 1][j - 1]时的最大价值
        int[][] dp = new int[row + 1][column + 1];
        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= column; j++) {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1];
            }
        }
        return dp[row][column];
    }
}
```