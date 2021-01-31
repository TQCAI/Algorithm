
[剑指 Offer 33. 二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)


```python
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder)<=1:
            return True
        root=postorder[-1]
        L=len(postorder)
        find_bigger=False
        bigger_ix=0
        for i in range(0, L-1):
            if postorder[i]<root:
                if find_bigger:
                    return False 
            else:
                if not find_bigger:
                    bigger_ix=i
                    find_bigger=True
        return self.verifyPostorder(postorder[:bigger_ix]) and self.verifyPostorder(postorder[bigger_ix:-1])
```

有空看下这个题解，感觉和我的思路不一样

[面试题33. 二叉搜索树的后序遍历序列（递归分治 / 单调栈，清晰图解）](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/)