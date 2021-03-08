from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left = top = 0
        right, bottom = n - 1, m - 1
        ans = []
        while True:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1
            if top > bottom and left > right: break

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1
            if top > bottom and left > right: break

            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom and left > right: break

            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            if top > bottom and left > right: break
        return ans


print(Solution().spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
