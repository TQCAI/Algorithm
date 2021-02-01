from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)

        def backtrace(t):
            if t == N:
                res.append(nums[:])
            for i in range(N):
                nums[i], nums[t] = nums[t], nums[i]
                backtrace(t + 1)
                nums[t], nums[i] = nums[i], nums[t]

        backtrace(0)
        return res
