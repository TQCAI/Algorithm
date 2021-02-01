from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, lower):
            l = 0
            r = len(nums) - 1
            ans = len(nums)
            while l <= r:  # diff
                mid = (l + r) // 2
                # 满足左边就一定会满足右边
                if (nums[mid] > target) or (lower and nums[mid] >= target):
                    r = mid - 1  # diff
                    ans = mid  # diff
                else:
                    l = mid + 1  # common
            return ans

        l_ix = binary_search(nums, target, True)
        r_ix = binary_search(nums, target, False) - 1
        if l_ix <= r_ix and r_ix < len(nums) and nums[l_ix] == target and nums[r_ix] == target:
            return l_ix, r_ix
        return -1, -1


print(Solution().searchRange([2, 3], 3))
