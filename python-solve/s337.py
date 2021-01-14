from structure import TreeNode


class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = {}

        def rec(root: TreeNode):
            if root is None:
                return 0
            if id(root) in memo:
                return memo[id(root)]
            do_it = root.val + \
                    (rec(root.left.left) + rec(root.left.right) if root.left else 0) + \
                    (rec(root.right.left) + rec(root.right.right) if root.right else 0)
            not_do = rec(root.left) + rec(root.right)
            ans = max(do_it, not_do)
            memo[id(root)] = ans
            return ans

        return rec(root)
