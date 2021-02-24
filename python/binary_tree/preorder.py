from typing import List

from structure import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        while root or stack:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return ans
