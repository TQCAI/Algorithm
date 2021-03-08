import collections
from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        # 建图
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        res = []
        # 记录每个节点当前时间戳和最早时间戳
        dfn = [-1] * n
        low = [-1] * n

        # tarjan算法
        def tarjan(node, parent, depth):
            dfn[node] = depth
            low[node] = depth
            for nex in graph[node]:
                # 下个节点为父节点，跳过
                if nex == parent: continue
                if dfn[nex] == -1:
                    tarjan(nex, node, depth + 1)
                    # 如果当前节点仍然比子节点小，说明找到桥
                    if dfn[node] < low[nex]:
                        res.append([node, nex])
                # 更新当前节点的最小时间戳
                low[node] = min(low[node], low[nex])

        tarjan(0, -1, 0)
        return res


ans = Solution().criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])
print(ans)
