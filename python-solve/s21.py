class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        for i, c in enumerate(s):
            pre_ix = i - dp[i - 1] - 1
            if c == ")" and pre_ix >= 0 and s[pre_ix] == "(":
                dp[i] = dp[i - 1] + 2
                if pre_ix - 1 >= 0:
                    dp[i] += dp[pre_ix - 1]
        return max(dp)


Solution().longestValidParentheses("()(())")
