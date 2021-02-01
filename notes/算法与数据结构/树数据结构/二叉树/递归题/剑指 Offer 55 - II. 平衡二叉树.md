[剑指 Offer 55 - II. 平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/)

[面试题55 - II. 平衡二叉树（从底至顶、从顶至底，清晰图解）](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/solution/mian-shi-ti-55-ii-ping-heng-er-cha-shu-cong-di-zhi/)

有空看题解

```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.ans=True
        def recur(node):
            if node is None:
                return 0
            l=recur(node.left)
            r=recur(node.right)
            if abs(l-r)>=2:
                self.ans=False
            return max(l,r)+1
        recur(root)
        return self.ans
```