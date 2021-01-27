from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        N = len(nums)
        l = 0
        r = N - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 左边有序
            # “左边有序”的判断一定要<=，其他的判断可以无脑两个<=
            # if nums[0] < nums[mid]:
            if nums[0] <= nums[mid]:
                # 目标值在左边
                # if nums[0] <= target <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 右边有序
            else:
                # 目标值在右边
                # if nums[mid] <= target <= nums[N - 1]:
                if nums[mid] < target <= nums[N - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


res = Solution().search([3, 1], 1)
print(res)
