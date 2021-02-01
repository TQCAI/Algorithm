from structure import TreeNode


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        if root.val == key:
            # 一举解决了情况1和情况2
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # 情况3
            min_node = self.find_min(root.right) # root.right 写错
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        elif root.val > key: # 左右顺序写错
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root

    def find_min(self, root: TreeNode) -> TreeNode:
        while root.left:
            root = root.left
        return root
