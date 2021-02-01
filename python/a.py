class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def upper_bound(nums, x):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] == x:
                    l = mid + 1
                elif nums[mid] < x:
                    l = mid + 1
                elif nums[mid] > x:
                    r = mid
            return r

        return upper_bound(nums, target) - upper_bound(nums, target - 1)
