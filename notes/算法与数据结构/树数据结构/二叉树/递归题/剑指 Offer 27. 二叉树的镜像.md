[剑指 Offer 27. 二叉树的镜像](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/)

```python
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def recur(node):
            if node is None:
                return None
            node.left, node.right = recur(node.right), recur(node.left)
            return node
        return recur(root)
```