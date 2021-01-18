from structure import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root in (p, q):  # 错写成 root.val ，一定要看清参数列表
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None and right is None:
            return None
        if left is not None and right is not None:
            return root
        return left if left else right
