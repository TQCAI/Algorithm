import collections
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        ans = []
        for p1 in range(N - 2):
            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue
            # p3 的定义要放在循环外面， 否则会超时
            p3 = N - 1
            target = -nums[p1]
            for p2 in range(p1 + 1, N):
                if p2 > p1 + 1 and nums[p2] == nums[p2 - 1]:
                    continue
                while p2 < p3 and nums[p2] + nums[p3] > target:
                    p3 -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if p2 == p3:
                    break
                if nums[p2] + nums[p3] == target:
                    ans.append([nums[p1], nums[p2], nums[p3]])
        return ans


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
