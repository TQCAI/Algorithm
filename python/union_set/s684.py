from typing import List


class UnionSet():
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        self.parent[pa] = pb


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionset = UnionSet(1001)
        res = []
        for a, b in edges:
            pa = unionset.find(a)
            pb = unionset.find(b)
            if pa == pb:
                res = [a, b]
            else:
                unionset.parent[pa] = pb
        return res


ans = Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
print(ans)
