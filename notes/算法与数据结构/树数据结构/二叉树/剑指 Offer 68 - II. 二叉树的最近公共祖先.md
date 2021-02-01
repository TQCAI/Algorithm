[剑指 Offer 68 - II. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/)

```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        if root.val in [p.val, q.val]:
            return root
        l_ret = self.lowestCommonAncestor(root.left,p,q)
        r_ret = self.lowestCommonAncestor(root.right,p,q)
        if l_ret is None and r_ret is None:
            return None
        if l_ret is not None and r_ret is not None:
            return root
        return l_ret if l_ret else r_ret
```