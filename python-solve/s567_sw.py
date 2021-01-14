import collections


class Solution(object):
    def checkInclusion(self, s1, s2):
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        l, r = 0, 0
        valid = 0  # 满足need的key数量
        need.update(collections.Counter(s1))
        while r < len(s2):
            c = s2[r]
            r += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            if r - l == len(s1):
                if valid == len(need):
                    return True
                c = s2[l]
                l += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1

        return False
