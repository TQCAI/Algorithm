from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # N 行 M 列
        N = len(matrix)
        if not N:
            return []
        M = len(matrix[0])
        if not M:
            return []
        vis = [[0] * M for _ in range(N)]
        i = 0
        j = 0
        ans = []

        def process(i, j, is_i, bound, delta):
            def judge(i, j):
                x = i if is_i else j
                return (x >= bound if delta == -1 else x < bound) and vis[i][j] != 1

            while judge(i, j):
                ans.append(matrix[i][j])
                vis[i][j] = 1
                if is_i:
                    i += delta
                else:
                    j += delta
            if is_i:
                i -= delta
            else:
                j -= delta
            return i, j

        while True:
            i, j = process(i, j, is_i=False, bound=M, delta=1)
            i, j = process(i, j, is_i=True, bound=N, delta=1)
            i, j = process(i, j, is_i=False, bound=0, delta=-1)
            i, j = process(i, j, is_i=True, bound=0, delta=-1)
            print(i, j)
        return ans


ans = Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(ans)
