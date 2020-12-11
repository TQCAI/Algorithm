class Solution:
    def __init__(self):
        L = 101
        self.dp = [[0] * L for _ in range(L)]
        self.dp[0][1] = 1
        self.M = 1
        self.N = 1

    def uniquePaths(self, m: int, n: int) -> int:
        for i in range(self.M, m + 1):
            for j in range(self.N, n + 1):
                self.dp[i][j] = self.dp[i - 1][j] + self.dp[i][j - 1]
        self.M = max(self.M, m + 1)
        self.N = max(self.N, n + 1)
        return self.dp[m][n]


s = Solution()
res = s.uniquePaths(3, 7)
print(res)
res = s.uniquePaths(2, 7)
print(res)
