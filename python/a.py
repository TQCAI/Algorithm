class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        # 错在没+1
        for i in range(1, l1 + 1):
            dp[i][0] = i
        for i in range(1, l2 + 1):
            dp[0][i] = i
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                # 错在没+1
                left = dp[i][j - 1] + 1
                down = dp[i - 1][j] + 1
                ld = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    ld += 1
                dp[i][j] = min(left, down, ld)
        return dp[l1][l2]
