from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        ans = 0
        #         □
        # □       □
        # □ □   □ □
        # 2 1 0 1 3
        #       ↑ ↑ 触发出栈情况
        # h:    1 1
        # l:    1 3
        # 出站后的pre变量代表了前一个高度
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                pre = stack.pop()
                # 如果stack为空，表示 [2, 3, 4] 这种情况，围不起来
                if not stack:
                    break
                t = stack[-1]
                h = min(height[t], height[i]) - height[pre]  # 当前高度 - 上一个高度
                l = i - t - 1
                ans += h * l
            stack.append(i)
        return ans


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
