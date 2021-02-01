import collections


class Solution:
    def sortString(self, s: str) -> str:
        counter = collections.Counter(s)
        keys = list(counter.keys())
        keys.sort()
        res = ""
        N = len(keys)
        rng = list(range(N)) + list(range(N - 1, -1, -1))
        while True:
            should_break = True
            for i in rng:
                key = keys[i]
                if counter[key]:
                    counter[key] -= 1
                    should_break = False
                    res += key
            if should_break:
                break
        return res


res = Solution().sortString("aaaabbbbcccc")
print(res)
