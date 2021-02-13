import random
from typing import List


class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        b_len = len(blacklist)
        self.convert = {}
        self.L = N - b_len
        self.tails = set(range(self.L, N)) - set(blacklist)
        self.tails = list(self.tails)  # 记录末尾在黑名单中的数
        index = 0
        for b in blacklist:
            # 如果b>=N-b_len ，压根不用映射
            if b < self.L:
                self.convert[b] = self.tails[index]
                index += 1

    def pick(self) -> int:
        index = random.randint(0, self.L - 1)
        return self.convert[index] if index in self.convert else index


res = Solution(4, [0, 2])
print(res.convert)
