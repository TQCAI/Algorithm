class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        left = a.copy()
        right = a.copy()
        N = len(a)
        res = [0] * N
        for i in range(1, N):
            left[i] = left[i - 1] * left[i]
        for i in range(N - 2, -1, -1):
            right[i] = right[i] * right[i + 1]
        for i in range(1, N - 1):
            res[i] = left[i - 1] * right[i + 1]
        res[0] = right[1]
        res[N - 1] = left[N - 2]
        return res
