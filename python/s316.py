import collections


class Solution:
    def removeDuplicateLetters(self, s) -> int:
        stack = []
        counter = collections.Counter(s)
        for c in s:
            if c not in stack:
                # stack[-1] > c | 单调递增条件被破坏
                while stack and stack[-1] > c and counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            counter[c] -= 1
        return "".join(stack)
