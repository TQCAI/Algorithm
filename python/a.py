class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] + nums[r] < target:
                l = mid + 1
            elif nums[l] + nums[mid] > target:
                r = mid - 1
            elif nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                return [nums[l], nums[r]]
        return [0, 0]
