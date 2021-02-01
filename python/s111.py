#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Date    : 2021-01-07
# @Contact    : qichun.tang@bupt.edu.cn
import collections

from structure import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque()
        cnt = 0
        while queue:
            cnt += 1
            sz = len(queue)
            while sz:
                sz -= 1
                top = queue.popleft()
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                if top.left is None and top.right is None:
                    return cnt
        return -1
