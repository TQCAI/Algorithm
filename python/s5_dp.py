class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        ret = ""
        # l 为 子串长度 - 1
        for l in range(N):
            for i in range(N - l):
                j = i + l
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j] and l + 1 > len(ret):
                    ret = s[i:j + 1]
        return ret
