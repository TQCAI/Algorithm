#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qichun tang
# @Date    : 2020-12-17
# @Contact    : tqichun@gmail.com
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp1 = {}
        mp2 = {}
        s_list = s.split(" ")
        if len(s_list) != len(pattern):
            return False
        for ch, word in zip(pattern, s_list):
            if ch not in mp1:
                mp1[ch] = word
            else:
                if mp1[ch] != word:
                    return False
            if word not in mp2:
                mp2[word] = ch
            else:
                if mp2[word] != ch:
                    return False
        return True


print(Solution().wordPattern("abba", "dog dog dog dog"))
