from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_lst = []
        min_ = float('inf')
        max_lst = []
        max_ = -float('inf')
        res = -float('inf')
        for price in prices:
            min_ = min(min_, price)
            min_lst.append(min_)
        for price in reversed(prices):
            max_ = max(max_, price)
            max_lst.append(max_)
        for min_d, max_d in zip(min_lst, reversed(max_lst)):
            res = max(res, max_d - min_d)
        return res


Solution().maxProfit([])
