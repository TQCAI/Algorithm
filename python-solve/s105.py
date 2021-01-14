from typing import List

from structure import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pre_s, pre_e, in_s, in_e):
            if pre_s > pre_e or in_s > in_e:
                return None
            if pre_s == pre_e:
                return TreeNode(preorder[pre_s])
            i = inorder.index(preorder[pre_s])
            num_left = i - in_s
            node = TreeNode(preorder[pre_s])
            node.left = build(pre_s + 1, pre_s + num_left, in_s, i - 1)
            node.right = build(pre_s + num_left + 1, pre_e, i + 1, in_e)
            return node

        N = len(inorder)
        return build(0, N - 1, 0, N - 1)


res = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
print(res)
