from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        # 基本概率
        p = 1 / 6
        # 初始化dp数组，轴1表示色子数，轴2表示点数。
        dp = [[p] * (6 * n_dices + 1) for n_dices in range(0, n + 1)]
        # fixme ↑ 统一初始化为 p
        # for k in range(1, 7): # fixme 不需要单独初始化
        #     dp[1][k] = p
        for n_dices in range(2, n + 1):
            # 如果抛2个色子，最小点数是2，最大点数6*2=12
            for n_points in range(n_dices, 6 * n_dices + 1):
                # 当前能抛的点数是1-6， 少抛一个色子的点数就要减去(1-6)，并且要乘以当前抛出点数的概率
                dp[n_dices][n_points] = sum( # fixme ↓ 将 0 改为上个状态的起始点数 n_dices - 1
                    dp[n_dices - 1][max(n_points - 6, n_dices - 1):(n_points - 1 + 1)]
                ) * p
        return dp[n][n:]


res = Solution().dicesProbability(2)
print(res)
