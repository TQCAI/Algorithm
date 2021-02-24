from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def dfs(s: str, ix: int, lst: List[str]):
            if s == "" and len(lst) == 4:
                ans.append(".".join(lst))
            # 不添加到 lst
            nix = ix + 1
            if nix <= len(s):
                dfs(s, nix, lst)
            # 添加到   lst
            if ix == 0:
                return
            if len(lst) >= 4:
                return
            sub = s[:ix]
            remain = s[ix:]
            if len(sub) > 1 and s[0] == '0':
                return
            if int(sub) > 255:
                return
            dfs(remain, 0, lst + [sub])

        dfs(s, 0, [])
        return ans


ans = Solution().restoreIpAddresses("101023")
print(ans)
