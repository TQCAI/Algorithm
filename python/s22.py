from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(s: str = '', k: int = 0):
            if k >= n:
                ans.append(s)
                return
            dfs('(' + s + ')', k + 1)
            dfs('()' + s, k + 1)
            dfs(s + '()', k + 1)

        dfs()
        return list(set(ans))


ans = Solution().generateParenthesis(3)
print(ans)
