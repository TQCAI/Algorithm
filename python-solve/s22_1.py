from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s, l_cnt):
            nonlocal res
            if len(s) >= n * 2:
                if l_cnt == 0:  # 需要加个判断，去掉非法解
                    res.append(s)
                return
            # left
            dfs(s + "(", l_cnt + 1)
            # right
            if l_cnt > 0:
                dfs(s + ")", l_cnt - 1)

        def dfs_ok(s, l_cnt, r_cnt):
            nonlocal res
            if len(s) >= n * 2:
                res.append(s)
                return
            # left
            if l_cnt < n:
                dfs_ok(s + "(", l_cnt + 1, r_cnt)
            # right
            if l_cnt > r_cnt:
                dfs_ok(s + ")", l_cnt, r_cnt + 1)

            # dfs("", 0)
        dfs_ok("", 0, 0)
        return res


res = Solution().generateParenthesis(3)
print(res)
