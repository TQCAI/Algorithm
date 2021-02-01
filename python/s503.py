from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        L = len(nums)
        ans = [0] * L
        for i in range(L * 2 - 1, -1, -1):
            num = nums[i % L]
            while stack and stack[-1] <= num:
                stack.pop()
            ans[i % L] = stack[-1] if stack else -1
            stack.append(num)
        return ans


ans = Solution().nextGreaterElements([2, 1, 2, 4, 3])
print(ans)
