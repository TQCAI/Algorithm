class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def countNodes(self, root: TreeNode) -> int:
        cnt = 0
        def preorder(node):
            nonlocal cnt
            if node:
                cnt += 1
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return cnt