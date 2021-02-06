class Solution:
    def findNthDigit(self, n: int) -> int:
        # digit: 数字位数， 如 1, 2, 3
        # start： 开始数字，如 1, 10, 100
        # count： 每个位上的计数
        digit = 1
        start = 1
        count = 9
        while n > count:
            n -= count
            count = digit * start * 9
            start = start * 10 if start else 1
            digit += 1
        # 确定n对应的是哪个数字
        # 此时的n其实是从0开始的，多了一位数，所以要减去。下同
        num = start + (n - 1) // digit
        # 确定是num的哪一位
        return int(str(num)[(n - 1) % digit])


ans = Solution().findNthDigit(11)
print(ans)
