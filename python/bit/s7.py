class Solution:
    def reverse(self, x: int) -> int:
        sign = x < 0
        x = abs(x)
        y = 0
        # 错在没加括号
        MAX = (1 << 31) - 1
        MUL_MAX = (1 << 30) // 5  # (2^31)/10
        while x:
            # 错在 >=
            if y > MUL_MAX:
                return 0
            y *= 10
            tail = x % 10
            # 错在 >=
            if y > MAX - tail:
                return 0
            y += tail
            x //= 10
        if sign:
            y *= -1
        return y


ans = Solution().reverse(1463847412)
print(ans)
