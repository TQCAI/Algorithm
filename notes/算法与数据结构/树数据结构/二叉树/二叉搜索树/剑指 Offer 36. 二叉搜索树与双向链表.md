[剑指 Offer 36. 二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/)

题解写的比我的简单

[面试题36. 二叉搜索树与双向链表（中序遍历，清晰图解）](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/solution/mian-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/)


```python
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: # 记得处理边界条件
            return root

        pre = None
        head = None

        def travel(node: Node):
            nonlocal pre, head
            if node is None:
                return
            travel(node.left)
            if head is None:
                # 不设dummy head
                head = node
            if pre is not None:
                pre.right = node
            node.left = pre
            pre = node
            travel(node.right)

        travel(root)
        pre.right=head # 加了后两句就好了
        head.left=pre
        return head
```

