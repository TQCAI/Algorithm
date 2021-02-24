class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        ans = 0
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = 2 + (
                        dp[i - 2] if i - 2 >= 0 else 0
                    )
                else:
                    pre = dp[i - 1]
                    pre_ix = i - 1 - pre
                    if pre_ix >= 0 and s[pre_ix] == "(":
                        dp[i] = dp[i - 1] + 2
                        # 没把条件缩进来
                        if pre_ix - 1 > 0:  # ()(())
                            dp[i] += dp[pre_ix - 1]
                ans = max(ans, dp[i])
        return ans


ans = Solution().longestValidParentheses("()()))))()()(")
print(ans)
