from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l1 = len(strs)
        if l1 == 0:
            return ""
        l2 = min(map(len, strs))
        for i in range(l2):
            for j in range(1, l1):
                if strs[j][i] != strs[j - 1][i]:
                    return strs[0][:i]
        return strs[0][:l2]


ans=Solution().longestCommonPrefix(['a', 'ab'])
print(ans)
