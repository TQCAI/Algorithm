import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        N = len(nums)
        res = []
        for i in range(N):
            # 满足单调递减
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()  # 默认右端出栈
            queue.append(i)
            # 删掉左端不在滑动窗口内元素
            if queue[0] <= i - k:
                queue.popleft()
            # 如果窗口已经形成，记录结果
            if i >= k - 1:
                # 结果记录的是最大值，所以需要把索引带入nums (默写出错)
                res.append(nums[queue[0]])
        return res
