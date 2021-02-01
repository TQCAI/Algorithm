from typing import List
import functools
from math import inf


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        v = -inf
        nums.sort()
        for i in range(1, len(nums)):
            v = max(abs(nums[i] - nums[i - 1]), v)
        return v