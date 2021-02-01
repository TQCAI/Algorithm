import collections
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        sym2idx = {}
        for equation, value in zip(equations, values):
            for symbol in equation:
                if symbol not in sym2idx:
                    sym2idx[symbol] = len(sym2idx)
            graph[sym2idx[equation[0]]].append([sym2idx[equation[1]], value])
            graph[sym2idx[equation[1]]].append([sym2idx[equation[0]], 1 / value])
        results = []
        for query in queries:
            a, b = query
            if a not in sym2idx or b not in sym2idx:
                result = -1
            else:
                result = -1
                queue = collections.deque()
                vis = collections.defaultdict(bool)
                vis[sym2idx[a]] = True
                queue.append([sym2idx[a], 1])
                while queue:
                    top, top_w = queue.popleft()
                    if top == sym2idx[b]:
                        result = top_w
                    for idx, w in graph[top]:
                        if not vis[idx]:
                            queue.append([idx, w * top_w])
                            vis[idx] = True
            results.append(result)
        return results


print(Solution().calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                              [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
