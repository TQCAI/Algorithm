from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        base = 1 / 6
        dp = [[0] * (6 * _ + 1) for _ in range(n + 1)]
        for k in range(1, 7):
            dp[1][k] = base
        for i in range(2, n + 1):
            for j in range(i, 6 * i + 1):
                # i-1表示上一个状态的色子数
                # 从点数和为j-1到点数和为j-6
                dp[i][j] = sum(dp[i - 1][max(0, j - 6):j]) * base
        return dp[n][n:]
