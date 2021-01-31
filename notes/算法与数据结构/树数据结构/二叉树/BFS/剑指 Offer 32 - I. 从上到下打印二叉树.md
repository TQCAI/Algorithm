[剑指 Offer 32 - I. 从上到下打印二叉树](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res=[]
        queue = collections.deque()
        queue.append(root)
        while queue:
            sz=len(queue)
            while sz:
                sz-=1
                top=queue.popleft()
                res.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
        return res
```

[剑指 Offer 32 - II. 从上到下打印二叉树 II](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res=[]
        queue = collections.deque()
        queue.append(root)
        while queue:
            sz=len(queue)
            lev=[]
            while sz:
                sz-=1
                top=queue.popleft()
                lev.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            res.append(lev)
        return res
```

[剑指 Offer 32 - III. 从上到下打印二叉树 III](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res=[]
        queue = collections.deque()
        queue.append(root)
        while queue:
            sz=len(queue)
            lev=[]
            while sz:
                sz-=1
                top=queue.popleft()
                lev.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            res.append(lev if len(res)%2==0 else lev[::-1])
        return res
```