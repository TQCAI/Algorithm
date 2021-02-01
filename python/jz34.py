from typing import List

from structure import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        path = [root.val]

        def dfs(root, cur_sum):
            if cur_sum > sum:
                return
            if root.left is None and root.right is None:
                if cur_sum == sum:
                    ans.append(path.copy())
                return
            if root.left:
                path.append(root.left.val)
                dfs(root.left, cur_sum + root.left.val)
                path.pop()
            if root.right:
                path.append(root.right.val)
                dfs(root.right, cur_sum + root.right.val)
                path.pop()

        dfs(root, root.val)
        return ans

print(Solution().pathSum(TreeNode(-2,None,TreeNode(-3)),-5))