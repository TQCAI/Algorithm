from structure import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = []
        queue.append(root)
        cnt = 0
        while queue:
            layers = []
            while queue:
                layers.append(queue.pop(0))
            for top in layers:
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            cnt += 1
        return cnt