from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        res = 0
        for i in range(1, N):
            res += max(0, prices[i] - prices[i - 1])
        return res


res = Solution().maxProfit([7, 1, 5, 3, 6, 4])
print(res)
