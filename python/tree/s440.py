class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def getCnt(prefix, n):
            count = 0
            cur = prefix
            next = prefix + 1
            # 为什么是<=呢？ n=10 时， 节点数是 11
            # cur: 1 10
            while cur <= n:
                count += min(next, n + 1) - cur
                cur *= 10
                next *= 10
            return count

        p = 1
        prefix = 1
        while p < k:
            count = getCnt(prefix, n)
            # 符号确定：试想 n=19, k=11
            # 此时count=11, p+count=12 > 11
            # 向下 (目标点是当前结点的叶子)
            if p + count > k:
                prefix *= 10
                p += 1
            # 向右 (目标点是当前结点的兄弟)
            elif p + count <= k:
                prefix += 1
                p += count
        return prefix


print(Solution().findKthNumber(19, 11))
