from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        dp = [0 for _ in range(N + 1)]
        pres = [[] for _ in range(N + 1)]
        dp[0] = 1
        wordDict = set(wordDict)
        for i in range(0, N + 1):
            if dp[i]:
                for j in range(i + 1, N + 1):
                    if s[i:j] in wordDict:
                        dp[j] = 1
                        pres[j].append(i)
        results: List[str] = []

        def recursion(ix, result):
            if ix == 0:
                results.append(" ".join(result))
            for pre in pres[ix]:
                recursion(pre, [s[pre:ix]] + result)

        recursion(N, [])

        if len(results) == 1 and results[0] == "":
            return []
        return results


res = Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
print(res)
