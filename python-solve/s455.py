#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Date    : 2020-12-26
# @Contact    : qichun.tang@bupt.edu.cn
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        s_N = len(s)
        s_start = 0
        cnt = 0
        for child_demand in g:
            while s_start < s_N:
                biscuit = s[s_start]
                s_start += 1
                if biscuit >= child_demand:
                    cnt += 1
                    break
            if s_start >= s_N:
                break
        return cnt
