from structure import TreeNode


class Solution(object):
    def maxPathSum(self, root: TreeNode) -> int:
        res = -inf

        def dfs(node):
            nonlocal res
            if node is None:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            res = max(res, (left + right + node.val))
            return max(left, right) + node.val

        dfs(root)
        return res
root=TreeNode(1,TreeNode(2),TreeNode(3))
ans=Solution().maxPathSum(root)
print(ans)
