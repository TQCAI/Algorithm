from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        for i in range(1, n - 1):
            max_left[i] = max(max_left[i - 1], height[i - 1])
        for i in reversed(range(1, n - 1)):  # range(n - 2, 0, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])
        for i in range(1, n - 1):
            min_height = min(max_left[i], max_right[i])
            sum += max(0, min_height - height[i])
        return sum


ans = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(ans)
