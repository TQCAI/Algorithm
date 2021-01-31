[剑指 Offer 34. 二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)

```python
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        path=[root.val]
        def dfs(root,cur_sum):
            # if cur_sum>sum: # 有阴间负数
            #     return
            if root.left is None and root.right is None:
                if cur_sum==sum:
                    ans.append(path.copy())
                return
            if root.left:
                path.append(root.left.val)
                dfs(root.left, cur_sum+root.left.val)
                path.pop()
            if root.right:
                path.append(root.right.val)
                dfs(root.right, cur_sum+root.right.val)
                path.pop()
        
        dfs(root,root.val)
        return ans
```