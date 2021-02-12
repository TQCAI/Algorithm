from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def get_H(k: int):
            return sum([ceil(pile / k) for pile in piles])

        l = 1
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            cur_H = get_H(mid)
            if cur_H == H:
                r = mid  # 往左边逼近
            elif cur_H < H:
                r = mid
            elif cur_H > H:
                l = mid + 1

        return l


Solution().minEatingSpeed([3, 6, 7, 11], 8)
Solution().minEatingSpeed([30, 11, 23, 4, 20], 5)
Solution().minEatingSpeed([30, 11, 23, 4, 20], 6)
