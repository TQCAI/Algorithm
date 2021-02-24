class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(xi - x0) < 1e-7:
                break
            x0 = xi
        return int(x0)


print(Solution().mySqrt(8))
