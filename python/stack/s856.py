class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack=[0]
        for c in S:
            if c =="(":
                stack.append(0)
            else:
                val=stack.pop()
                if val==0:
                    delta=1
                else:
                    delta=val*2
                stack[-1]+=delta
        return stack[0]

print(Solution().scoreOfParentheses("()"))
print(Solution().scoreOfParentheses("(())"))
print(Solution().scoreOfParentheses("()()"))
print(Solution().scoreOfParentheses("(()(()))"))
