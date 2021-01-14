from typing import List


class Solution:
    def twoSum(self, nums: List[int], start, target) -> List[List[int]]:
        if start >= len(nums):
            return []
        lo = start
        hi = len(nums) - 1
        res = []
        while lo < hi:
            left, right = nums[lo], nums[hi]
            if left + right > target:
                hi -= 1
            elif left + right < target:
                lo += 1
            else:
                res.append([nums[lo], nums[hi]])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums) - 2:
            arrs = self.twoSum(nums, i + 1, -nums[i])
            for arr in arrs:
                arr.append(nums[i])
                res.append(arr)
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
