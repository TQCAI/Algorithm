from math import sqrt


class Solution:
    def is_prime(self, x) -> int:
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return 0
        return 1

    def countPrimes(self, n):
        return sum(self.is_prime(i) for i in range(2, n))


res = Solution().countPrimes(10)
print(res)
