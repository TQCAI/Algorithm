from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 贪心法与DP不同，在开始交易时就考虑手续费fee
        L = len(prices)
        buy = prices[0] + fee
        profit = 0
        for i in range(1, L):
            if prices[i] + fee < buy:
                buy = prices[i] + fee # 重新买
            elif prices[i] > buy:
                profit += prices[i] - buy # 增量卖
                buy = prices[i]
        return profit

res = Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)
print(res)
