from math import sqrt


class Solution:
    def countPrimes(self, n):
        is_prime = [1] * n
        ans = 0
        for x in range(2, n):
            if is_prime[x]:
                ans += 1
                if x ** 2 < n:
                    j = x ** 2
                    while j < n:
                        is_prime[j] = 0
                        j += x
        return ans


res = Solution().countPrimes(10)
print(res)
