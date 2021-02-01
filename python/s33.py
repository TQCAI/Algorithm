from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 左边有序
            if nums[0] <= nums[mid]:
                # 目标值在左边范围内
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                # 目标值在右边范围内
                else:
                    l = mid + 1
            # 右边有序
            else:
                # 目标值在右边范围内
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                # 目标值在左边范围内
                else:
                    r = mid - 1
        return -1


Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
