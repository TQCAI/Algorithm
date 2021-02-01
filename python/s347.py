import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        heap = []
        for num, cnt in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, num))
            else:
                if heap[0][0] < cnt:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (cnt, num))
        ans = []
        while len(heap):
            ans.insert(0, heapq.heappop(heap)[1])
        return ans


ans = Solution().topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)
print(ans)
