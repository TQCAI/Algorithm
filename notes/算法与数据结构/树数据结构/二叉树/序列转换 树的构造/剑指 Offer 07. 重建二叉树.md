[剑指 Offer 07. 重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/)

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        in_ix = inorder.index(preorder[0])
        return TreeNode(
            preorder[0],
            self.buildTree(preorder[1:in_ix + 1], inorder[:in_ix]),
            self.buildTree(preorder[in_ix + 1:], inorder[in_ix + 1:]),
        )
```