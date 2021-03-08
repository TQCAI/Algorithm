class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 排除 10 和 负数 的特殊情况
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rx = 0
        while x > rx:
            rx = rx * 10 + x % 10
            x //= 10
        return rx == x or rx // 10 == x


ans = Solution().isPalindrome(1221)
print(ans)
