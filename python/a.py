class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        i1 = l1 - 1
        i2 = l2 - 1
        carry = 0
        base = 10
        ans = ''
        while i1 >= 0 or i2 >= 0 or carry:
            a = int(num1[i1]) if i1 >= 0 else 0
            b = int(num2[i2]) if i2 >= 0 else 0
            sum_ = a + b + carry
            print(sum_)
            ans = ans + str(sum_ % base)
            carry = sum_ // base
            i1 -= 1
            i2 -= 1

        return ans[::-1]


ans = Solution().addStrings("123", "456")
print(ans)
