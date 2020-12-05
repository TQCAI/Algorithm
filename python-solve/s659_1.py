from typing import List
import collections
import heapq


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mp = collections.defaultdict(list)
        for x in nums:
            queue = mp.get(x - 1)
            if queue:
                prevLength = heapq.heappop(queue) # 尽量插入到长度最小的序列上
                heapq.heappush(mp[x], prevLength + 1)
            else:
                heapq.heappush(mp[x], 1)

        return not any(queue and queue[0] < 3 for queue in mp.values())


Solution().isPossible([1, 2, 3, 3, 4, 4, 5, 5])
