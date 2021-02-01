#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Date    : 2021-01-26
# @Contact    : qichun.tang@bupt.edu.cn

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        in_ix = tin.index(pre[0])
        node = TreeNode(pre[0])
        node.left = self.reConstructBinaryTree(pre[1:in_ix + 1], tin[:in_ix])
        node.right = self.reConstructBinaryTree(pre[in_ix + 1:], tin[in_ix + 1:])
        return node
