from structure import TreeNode


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        sum_ = 0

        def rec(node: TreeNode):
            nonlocal sum_
            if node is None:
                return None
            rec(node.right)
            sum_ += node.val
            node.val = sum_
            rec(node.left)

        rec(root)
        return root
