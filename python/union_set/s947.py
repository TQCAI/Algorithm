from typing import List


class UnionSet():
    def __init__(self):
        self.parent = {}
        self.count = 0

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.count += 1
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        self.count -= 1
        self.parent[pa] = pb


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uniset = UnionSet()
        for x, y in stones:
            uniset.union(10001 - x, y)
        return len(stones) - uniset.count
