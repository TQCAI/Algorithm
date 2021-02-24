from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        a = 0
        b = n - 1
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            while mid > a and nums[mid] == nums[a]:
                a += 1
            while mid < b and nums[mid] == nums[b]:
                b -= 1
            if not a <= mid <= b:
                break
            # 左边有序
            # 记得加=，虽然互不相同，但是mid可能直接取到0,
            if nums[mid] > nums[a] or mid == a:
                if nums[a] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[b]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


# ans = Solution().search([6, 7, 8, 1, 2, 3, 4, 5], 8)
ans = Solution().search([1, 0, 1, 1, 1], 0)
print(ans)
