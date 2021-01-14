from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        p1 = p2 = c = 0
        for i in range(N - 1, -1, -1):
            c = max(p1, p2 + nums[i])
            p2 = p1
            p1 = c
        return c
