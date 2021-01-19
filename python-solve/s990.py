from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
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
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

        union_set = UnionSet(500)
        symbol2idx = {}

        def get_symbol_idx(symbol):
            if symbol not in symbol2idx:
                symbol2idx[symbol] = len(symbol2idx)
            return symbol2idx[symbol]

        eq = []
        neq = []
        for equation in equations:
            s1 = get_symbol_idx(equation[0])
            s2 = get_symbol_idx(equation[-1])
            link = equation[1:3]
            if link == "==":
                eq.append([s1, s2])
            else:
                neq.append([s1, s2])

        for s1, s2 in eq:
            union_set.union(s1, s2)
        for s1, s2 in neq:
            if union_set.find(s1) == union_set.find(s2):
                return False
        return True
