
[剑指 Offer 26. 树的子结构](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/)


[面试题26. 树的子结构（先序遍历 + 包含判断，清晰图解）](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/solution/mian-shi-ti-26-shu-de-zi-jie-gou-xian-xu-bian-li-p/)




```
例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
```

`recur`判定函数的记忆方法：
- 如果B为空，说明走到底了，True
- 如果A为空，说明没救了，False
- 判断元素是否相等
- 继续往下递归（and条件）

递归里面有递归，很难想到

```python
def recur(A, B):
    if B is None:
        return True
    if A is None:
        return False
    if not A.val==B.val:
        return False
    return recur(A.left, B.left) and recur(A.right, B.right) # and

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # bool
        return bool(A and B) and ( recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B) )
```



```python
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B:
                return True
            if not (A and A.val == B.val):
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        # 误将 isSubStructure 写成了 recur
        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
```


