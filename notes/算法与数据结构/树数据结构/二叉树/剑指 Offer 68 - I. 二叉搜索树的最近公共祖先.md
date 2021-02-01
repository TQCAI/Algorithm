[剑指 Offer 68 - I. 二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/)

[面试题68 - I. 二叉搜索树的最近公共祖先（迭代 / 递归，清晰图解）](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/mian-shi-ti-68-i-er-cha-sou-suo-shu-de-zui-jin-g-7/)

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        qv = q.val
        pv = p.val
        while root:
            rv = root.val
            if rv < qv and rv < pv:
                root = root.right
            elif rv > qv and rv > pv:
                root = root.left
            else:
                break
        return root
```