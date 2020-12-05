import collections


class Solution:
    def sortString(self, s: str) -> str:
        num = [0] * 26
        for c in s:
            num[ord(c) - 97] += 1
        ret, M = "", 26
        while len(ret) < len(s):
            for i in list(range(M)) + list(range(M - 1, -1, -1)):
                if num[i]:
                    ret += chr(i + 97)
                    num[i] -= 1
        return ret


res = Solution().sortString("aaaabbbbcccc")
print(res)
