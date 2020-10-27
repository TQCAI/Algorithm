from typing import List, Tuple


class Solution:
    def get_compare(self, s: str) -> Tuple[List[int], List[int]]:
        if not s:
            return ([], [])
        pre = s[0]
        cnt = 1
        results = ([], [])
        for c in s[1:]:
            if c != pre:
                results[0].append(pre)
                results[1].append(cnt)
                pre = c
                cnt = 1
            else:
                cnt += 1
        results[0].append(s[-1])
        results[1].append(cnt)
        return results

    def isLongPressedName(self, name: str, typed: str) -> bool:
        if bool(name) ^ bool(typed):
            return False
        if not name:
            return True
        res1 = self.get_compare(name)
        res2 = self.get_compare(typed)
        if res1[0] == res2[0]:
            for i in range(len(res1[1])):
                if res1[1][i] > res2[1][i]:
                    return False
        else:
            return False
        return True



results = Solution().isLongPressedName(
    "xnhtq",
    "xhhttqq"
)
print(results)
