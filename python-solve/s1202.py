import collections
import heapq
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UnionSet():
            def __init__(self, n):
                self.cnt = n
                self.parent = [0] * n
                for i in range(n):
                    self.parent[i] = i

            def union(self, a, b):
                pa = self.find(a)
                pb = self.find(b)
                if pa == pb:
                    return
                self.parent[pa] = pb
                self.cnt -= 1

            def find(self, x) -> int:
                if x == self.parent[x]:
                    return x
                # 找到根节点
                r = x
                while r != self.parent[r]:
                    r = self.parent[r]
                # 路径压缩
                while x != self.parent[x]:
                    t = self.parent[x]
                    self.parent[x] = r
                    x = t
                return r

        N = len(s)
        union_set = UnionSet(N)
        for pair in pairs:
            union_set.union(*pair)
        id2heap = collections.defaultdict(list)
        for i in range(N):
            heap = id2heap[union_set.find(i)]
            heapq.heappush(heap, (s[i], i))
        ans = ""
        for i in range(N):
            heap = id2heap[union_set.find(i)]
            ch, _ = heapq.heappop(heap)
            ans += ch
        return ans
