import collections

from structure import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # BFS
        queue = collections.deque()
        queue.append(root)
        while queue:
            # 遍历一层
            sz = len(queue)
            has_children = False
            seq = []
            while sz:
                sz -= 1
                top = queue.popleft()
                if top is None:
                    queue.append(None)
                    queue.append(None)
                    seq.append('#')
                else:
                    queue.append(top.left)
                    queue.append(top.right)
                    has_children = True
                    seq.append(top.val)
            if not has_children:
                break
            l = 0
            r = len(seq) - 1
            while l < r:
                if seq[l] != seq[r]:
                    return False
                l, r = l + 1, r - 1
        return True


res = Solution().isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))))
print(res)
