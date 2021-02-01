from structure import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        rank = 0
        ans = -1

        def rec(node: TreeNode):
            nonlocal rank, ans
            if node is None:
                return
            rec(node.left)
            rank += 1
            if rank == k:
                ans = node.val
                return
            rec(node.right)

        rec(root)
        return ans
