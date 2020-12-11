from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right, ret = [[0] * n for _ in range(3)]
        left[0] = 1
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        for i in range(n):
            ret[i] = left[i] * right[i]
        return ret


ret = Solution().productExceptSelf([1, 2, 3, 4])
print(ret)
