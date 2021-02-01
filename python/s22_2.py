from functools import lru_cache
from typing import List


class Solution:
    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        ans = []
        for c in range(n):
            for l in self.generateParenthesis(c):
                for r in self.generateParenthesis(n - 1 - c):
                    ans.append("({}){}".format(l, r))
        return ans


res = Solution().generateParenthesis(3)
print(res)
