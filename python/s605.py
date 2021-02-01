from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)

        def available(i):
            if flowerbed[i] == 0 and \
                    (i == 0 or flowerbed[i - 1] == 0) and \
                    (i == N - 1 or flowerbed[i + 1] == 0):
                return True
            return False

        cnt = 0
        for i in range(N):
            if available(i):
                cnt += 1
                flowerbed[i] = 1
        return n <= cnt


Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2)
