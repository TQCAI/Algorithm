[剑指 Offer 55 - II. 平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/)

[面试题55 - II. 平衡二叉树（从底至顶、从顶至底，清晰图解）](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/solution/mian-shi-ti-55-ii-ping-heng-er-cha-shu-cong-di-zhi/)

```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if root is None:
                return 0
            left = recur(root.left)
            right = recur(root.right)
            if left==-1 or right==-1:
                return -1
            if abs(right-left)>=2:
                return -1
            return max(left, right) + 1
        return recur(root)!=-1
```