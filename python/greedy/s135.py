from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        right = 1
        ans = left[n - 1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right += 1
            else: # 错在这
                right = 1
            ans += max(right, left[i])
        return ans


Solution().candy([1, 3, 2, 2, 1])
