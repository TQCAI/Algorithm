from typing import List


class Solution:
    def twoSum(self, nums, start, target):
        l = start
        r = len(nums) - 1
        ans = []
        while l < r:
            lo = nums[l]
            hi = nums[r]
            if lo + hi == target:
                ans.append([lo, hi])
                #         判断条件写成了 !=
                while l < r and nums[r] == hi: r -= 1 # 写成了 += 1
                while l < r and nums[l] == lo: l += 1
            elif lo + hi < target:
                while l < r and nums[l] == lo: l += 1
            else:
                while l < r and nums[r] == hi: r -= 1
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        i = 0
        while (i < n - 2): # 错误地使用了for循环
            num = nums[i]
            cur_ans = self.twoSum(nums, i + 1, 0 - num)
            if cur_ans:
                ans += [item + [num] for item in cur_ans]
            while i < n - 2 and nums[i] == num: i += 1
        return ans


ans = Solution().threeSum([-1, 0, 1, 2, -1, -4])
print(ans)
