class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for c in s:
            if c in pairs and stack and stack[-1] == pairs[c]:
                stack.pop()
            else:
                stack.append(c)
        return not stack


print(Solution().isValid("){"))