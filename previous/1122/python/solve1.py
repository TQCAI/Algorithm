#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Contact    : tqichun@gmail.com
from typing import List
import collections


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = collections.Counter(arr1)
        res = []
        for e in arr2:
            if e in counter:
                res += [e] * counter[e]
                counter.pop(e)
        sorted_keys = sorted(list(counter.keys()))
        for k in sorted_keys:
            cnt = counter[k]
            res += [k] * cnt
        return res
