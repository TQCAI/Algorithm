from structure import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self._isValidBST(root, None, None)

    def _isValidBST(self, root: TreeNode, min_: TreeNode, max_: TreeNode):
        if root is None:
            return True
        if min_ is not None and root.val <= min_.val:
            return False
        if max_ is not None and root.val >= max_.val:
            return False
        return self._isValidBST(root.left, min_, root) and \
               self._isValidBST(root.right, root, max_)

