from typing import List

from structure import TreeNode


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
