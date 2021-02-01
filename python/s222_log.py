from structure import TreeNode


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        r = l = root
        hr = hl = 0
        while r is not None:
            hr += 1
            r = r.right
        while l is not None:
            hl += 1
            l = l.left
        # 空指针也会在这里返回
        if hl == hr:
            return 2 ** (hl) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

