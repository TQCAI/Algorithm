from math import inf
from typing import List

from structure import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def rec(a, b) -> TreeNode:
            if a >= b:
                return None
            if a == b - 1:
                return TreeNode(nums[a])
            max_ = -inf
            max_ix = -1
            for i in range(a, b):
                if nums[i] > max_:
                    max_ = nums[i]
                    max_ix = i
            return TreeNode(nums[max_ix], rec(a, max_ix), rec(max_ix + 1, b))

        return rec(0, len(nums))
