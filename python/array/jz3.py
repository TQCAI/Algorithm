from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # 有一个顾虑，就是如果不存在数字i会出现死循环，
            # 但不用担心，如 [1, 1, 1] ，会直接返回掉
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                # ↓ 这么干就凉了
                # nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
                tmp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = tmp
        return -1


Solution().findRepeatNumber([2, 3, 1, 0, 2, 5, 3])
