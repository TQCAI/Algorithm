import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L1 = len(s1)
        L2 = len(s2)
        counter = collections.Counter(s1)
        if L1 > L2:
            return False
        for i in range(L2 - L1 + 1):
            sub = s2[i:i + L1]
            if collections.Counter(sub) == counter:
                return True
        return False
