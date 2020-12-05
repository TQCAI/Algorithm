import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        maxExec = max(freq.values())
        maxCount = sum(1 for cnt in freq.values() if cnt == maxExec)
        return max(  # 没想到
            (maxExec - 1) * (n + 1) + maxCount,
            len(tasks)  # 没想到
        )


res = Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 0)
print(res)
