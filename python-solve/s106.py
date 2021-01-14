from typing import List

from structure import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(post_s, post_e, in_s, in_e):
            if post_s > post_e or in_s > in_e:
                return None
            if post_s == post_e:
                return TreeNode(postorder[post_e])
            i = inorder.index(postorder[post_e])
            num_left = i - in_s
            node = TreeNode(postorder[post_e])
            node.left = build(post_s, post_s + num_left - 1, in_s, i - 1)
            node.right = build(post_s + num_left, post_e - 1, i + 1, in_e)
            return node

        N = len(inorder)
        return build(0, N - 1, 0, N - 1)


res = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
print(res)
