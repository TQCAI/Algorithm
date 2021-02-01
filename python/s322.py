from math import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}

        def helper(amount):
            if (amount in memo):
                return memo[amount]
            res = inf
            for coin in coins:
                if (amount >= coin):
                    res = min(res, helper(amount - coin) + 1)
            memo[amount] = res
            return res

        return helper(amount) if (helper(amount) != inf) else -1
