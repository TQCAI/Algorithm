from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(s, left, right):
            if left > n or right > n:
                return
            if left == right == n:
                ans.append(s)
            dfs(s + "(", left + 1, right)
            if left > right:
                dfs(s + ")", left, right + 1)

        dfs("", 0, 0)
        return ans


ans = Solution().generateParenthesis(3)
print(ans)
