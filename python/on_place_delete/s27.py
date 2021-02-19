from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = slow = 0
        while fast < len(nums) and slow < len(nums):
            while fast < len(nums) and nums[fast] == val:
                fast += 1
            if fast < len(nums):
                nums[slow] = nums[fast]
            else:
                break
            slow += 1
            fast += 1
        # print(nums[:slow])
        return slow


Solution().removeElement([3, 2, 2, 3], 3)
