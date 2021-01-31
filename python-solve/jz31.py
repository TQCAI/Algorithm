from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pu_i = 0
        for num in popped:
            if stack and stack[-1] == num:
                stack.pop()
            else:
                while pu_i < len(pushed):
                    cur_push = pushed[pu_i]
                    stack.append(cur_push)
                    pu_i += 1
                    if cur_push == num:
                        break
                if stack[-1] != num:
                    return False
                stack.pop()
        return True

print(Solution().validateStackSequences([1,2,3,4,5],
[4,5,3,2,1]
))
