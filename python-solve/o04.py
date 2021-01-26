#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Date    : 2021-01-26
# @Contact    : qichun.tang@bupt.edu.cn
from typing import List, Tuple


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        N = len(matrix)
        M = len(matrix[0])

        def rec(root: Tuple[int, int]):
            x, y = root
            if not (0 <= x < N or 0 <= y < M):
                return False
            root_val = matrix[x][y]
            if root_val == target:
                return True
            if root_val < target:
                return rec((x, y + 1))  # 下
            else:
                return rec((x - 1, y))  # 左

        return rec((0, M - 1))
