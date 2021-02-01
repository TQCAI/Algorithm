from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i <= len(A) and j <= len(B):
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]
            if a1 <= b2 and a2 >= b1:
                res.append([max(a1, a2), min(b1, b2)])
            if b2 > a2:
                i += 1
            else:
                j += 1
        return res
