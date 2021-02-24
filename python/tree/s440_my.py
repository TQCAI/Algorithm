class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_count(prefix, n):
            next = prefix + 1
            cur = prefix
            count = 0
            # 为什么是<=呢？ n=10 时， 节点数是 11
            # cur: 1 10
            while cur <= n:
                count += min(n + 1, next) - cur
                cur *= 10
                next *= 10
            return count

        p = 1
        prefix = 1
        while p < k:
            count = get_count(prefix, n)
            if p + count > k:
                prefix *= 10
                p += 1
            else:
                prefix += 1
                p += count
        return prefix
