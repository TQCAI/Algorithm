from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            # 考虑长度为 1 和 0 的情况
            return N
        pre_delta = nums[1] - nums[0]
        ans = 1 if pre_delta == 0 else 2
        for i in range(2, N):
            delta = nums[i] - nums[i - 1]
            if (delta > 0 and pre_delta <= 0) or (delta < 0 and pre_delta >= 0):
                ans += 1
                pre_delta = delta
        return ans



res = Solution().wiggleMaxLength([1, 2, 3])
# res = Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])
print(res)
