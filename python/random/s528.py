import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.psum = []
        self.tot = 0
        for x in w:
            self.tot += x
            self.psum.append(self.tot)

    def pickIndex(self) -> int:
        # [0, tot)
        targ = random.randint(0, self.tot-1)
        l = 0
        r = len(self.psum)
        while l < r:
            mid = (l + r) // 2
            curr = self.psum[mid]
            if curr == targ:
                # r = mid
                l = mid + 1 # fixme: 往右边逼
            elif curr < targ:
                l = mid + 1
            elif curr > targ:
                r = mid
        return l


solv = Solution([1, 3, 1])
for _ in range(100):
    print(solv.pickIndex())
