from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = inf
        max_reward = -inf
        for price in prices:
            min_price=min(price,min_price)
            max_reward=max(price-min_price,max_reward)
        return max_reward


Solution().maxProfit([])
