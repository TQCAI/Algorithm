import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        i = 0
        need_cnt = len(t)
        res = (0, float('inf'))
        for j, c in enumerate(s):
            if need[c] > 0:
                need_cnt -= 1
            need[c] -= 1
            if need_cnt == 0:
                while True:
                    if need[s[i]] == 0:
                        break
                    need[s[i]] += 1
                    i += 1
                if j - i < res[1] - res[0]: # 默写时写错bool条件
                    res = (i, j)
                need[s[i]] += 1 # 默写时写错
                i += 1
                need_cnt += 1
        return "" if res[1] == float('inf') else s[res[0]:res[1] + 1]


res = Solution().minWindow("ADOBECODEBANC", "ABC")
print(res)
