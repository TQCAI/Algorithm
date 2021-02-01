from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        L = len(cost)
        dp = [0] * (L + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        cost.append(0)
        for i in range(2, L + 1):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return dp[L]


print(Solution().minCostClimbingStairs([10, 15, 20]))
