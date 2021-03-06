from math import inf


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # ring: godding | j | n
        # key: gd       | i | m
        # 定义 dp[i][j] 表示从前往后拼写出 key 的第 i 个字符， ring 的第 j 个字符 的最小步数
        # 维护一个位置数组 pos[c] ，表示 字符c 在 ring 中出现的位置集合
        #

        fn = lambda x: ord(x) - 97
        n = len(ring)
        m = len(key)
        pos = [[] for _ in range(26)]
        for i in range(n):
            pos[fn(ring[i])].append(i)
        dp = [[inf for _ in range(n)] for _ in range(m)]
        # 对于 key 0， 直接旋转
        for i in pos[fn(key[0])]:
            dp[0][i] = min(i, n - i) + 1  # + 1 是为了按button
        for i in range(1, m):  # 遍历key
            for j in pos[fn(key[i])]:  # key[i] 在 ring 中所有出现过的位置 j
                for k in pos[fn(key[i - 1])]:  # key[i-1] 在 ring 中所有出现过的位置 k
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - 1][k] + min(  # 从上一次的状态（多个）转到当前状态（多个）的最小值
                            abs(j - k),
                            n - abs(j - k)
                        ) + 1  # 记得 + 1
                    )
        return min(*dp[m - 1])


print(Solution().findRotateSteps(
    "abcde",
    "ade"
))
