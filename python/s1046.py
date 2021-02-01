import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = -heapq.heappop(stones)
            s2 = 0
            if len(stones):
                s2 = -heapq.heappop(stones)
            s = abs(s1 - s2)
            if s:
                heapq.heappush(stones, -s)
        return -stones[0] if stones else 0


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
