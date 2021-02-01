import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        window = collections.defaultdict(int)
        valid = 0
        l, r = 0, 0
        a, b = -1, len(s)
        while r < len(s):
            c = s[r]
            r += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while l < r and valid == len(need):
                if  r - l < b - a:
                    a, b = l, r
                c = s[l]
                l += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return "" if a == -1 else s[a:b]


Solution().minWindow("ADOBECODEBANC", "ABC")