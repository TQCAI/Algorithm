from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        L = len(nums)
        sum_ = sum(nums)
        if sum_ % 2:
            return False
        target = sum_ // 2
        # L 行 target + 1 列
        dp = [[0] * (target + 1) for _ in range(L)]
        # 容量为0的时候，绝逼恰好能装满
        dp[0][0] = True
        # 初始化第一个物品
        if target >= nums[0]:
            dp[0][nums[0]] = True
        # 开始DP
        for i in range(1, L):
            for j in range(target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
            # 只装i个物品就装满了
            if dp[i][target]:
                return True
        return False


res = Solution().canPartition([9, 5])
print(res)
