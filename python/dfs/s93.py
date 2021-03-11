from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def dfs(s, ix, path):
            if s == "" and len(path) == 4:
                ans.append(".".join(path))
                return
            # 不选
            if ix <= len(s) - 1:
                dfs(s, ix + 1, path)
            # 选
            if len(path) >= 4 or ix == 0:
                return
            chose, rest = s[:ix], s[ix:]
            if int(chose) > 255 or (chose.startswith('0') and chose != '0'):
                return
            cur_path = path + [chose]
            if len(cur_path) == 4 and rest != "":
                return
            dfs(rest, 0, cur_path)

        dfs(s, 1, [])
        return ans


ans = Solution().restoreIpAddresses("101023")
print(ans)
