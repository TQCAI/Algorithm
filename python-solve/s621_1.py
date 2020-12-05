import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        rest = list(freq.values())
        M = len(rest)
        nextValid = [1] * M
        time = 0
        for _ in tasks:
            time += 1
            # 下一个最早可用时间
            minNextValid = min(nextValid[i] for i in range(M) if rest[i] > 0)
            time = max(time, minNextValid)  # 写错成了min
            best = -1
            for i in range(M):
                # 在剩余任务中，时间满足
                if rest[i] > 0 and nextValid[i] <= time:
                    # 剩余次数最多
                    if best == -1 or rest[i] > rest[best]:
                        best = i
            rest[best] -= 1
            # 根据样例、需要间隔n个
            nextValid[best] = time + n + 1
        return time


res = Solution().leastInterval(["A","A","A","B","B","B"],
2
)
print(res)
