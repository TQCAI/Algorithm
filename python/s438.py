import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        need.update(collections.Counter(p))
        res = []
        valid = 0
        l, r = 0, 0
        while r < len(s):
            c = s[r]
            r += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            if r - l == len(p):
                if valid == len(need):
                    res.append(l)
                c = s[l]
                l += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return res
