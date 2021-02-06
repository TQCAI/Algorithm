class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # m 行 n 列
        m = len(s)
        n = len(p)
        # 注意返回的是bool类型，不要用0来初始化
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        def match(i, j):
            if i == 0 or j == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        # 两个空状态匹配为True
        dp[0][0] = True
        # 被匹配串可以为空，模式串不能为空
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    if match(i, j - 1):
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
                else:
                    # if match(i-1,j-1): # 我是傻逼
                    if match(i, j):
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = False
        return dp[m][n]
