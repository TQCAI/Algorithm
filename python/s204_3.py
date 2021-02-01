from math import sqrt

class Solution:
    def countPrimes(self, n):
        is_prime = [1] * n
        primes = []
        for x in range(2, n):
            if is_prime[x]:
                primes.append(x)
            for prime in primes:
                if x * prime >= n:
                    break
                is_prime[x * prime] = 0
                if x % prime==0:
                    break
        return len(primes)


res = Solution().countPrimes(10)
print(res)
