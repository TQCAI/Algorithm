#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Contact    : tqichun@gmail.com
from typing import List


class Solution:
    def binary(self, x):
        result = 0
        while x:
            result += int(x % 2 == 1)
            x //= 2
        return result

    def count1(self, x):
        res = 0
        while x:
            res += x & 1
            x >>= 1
        return res

    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (self.count1(x), x))


res = Solution().sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(res)
