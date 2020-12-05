from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        N = len(A)
        if N < 3:
            return 0
        A.sort(reverse=True)
        for i in range(N - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return sum(A[i:i + 3])
        return 0


print(Solution().largestPerimeter(
    [2, 1, 2]
))
