import collections
from typing import List

from structure import TreeNode


class Solution:
    NULL = "#"

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        memo = collections.defaultdict(int)
        res = []

        def traverse(node: TreeNode):
            if node is None:
                return self.NULL
            seq = ",".join([traverse(node.left), traverse(node.right), str(node.val)])
            if memo[seq] == 1:
                res.append(node)
            memo[seq] += 1
            return seq

        traverse(root)
        return res