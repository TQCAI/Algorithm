from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [0 for i in range(N + 1)]
        dp[0] = 1
        wordDict = set(wordDict)
        s_ = "c" + s
        for i in range(0, N + 1):
            if dp[i]:
                for j in range(i + 1, N + 1):
                    if s_[i + 1:j+1] in wordDict:
                        dp[j] = 1
        return bool(dp[N])


res=Solution().wordBreak("applepenapple", ["apple", "pen"])
print(res)
