class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # 只想到通过 s p 最前面加字符的方法， 没想到设置match函数更方便
        def match(i, j):
            if i == 0 or j == 0:
                return False
            if p[j - 1] == ".":
                return True
            return s[i - 1] == p[j - 1]

        for i in range(m + 1):
            # s 可以是空串， p 必须有值。如 "" 匹配 "b*"
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    if match(i, j - 1):
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
                else:
                    if match(i, j):
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = False
        return dp[m][n]


# print(Solution().isMatch("mississippi", "mis*is*p*."))
print(Solution().isMatch("aab", "c*a*b"))
