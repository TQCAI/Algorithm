import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        lookup = collections.defaultdict(int)
        cnt = 0
        start = 0
        res = (0, 0)

        for end, c in enumerate(s):
            if lookup[c] == 0:
                cnt += 1
            lookup[c] += 1
            while cnt > 2:
                lookup[s[start]] -= 1
                if lookup[s[start]] == 0:
                    cnt -= 1
                start += 1
            if end - start > res[1] - res[0]:
                res = (start, end)
        return res[1] - res[0] + 1


print(Solution().lengthOfLongestSubstringTwoDistinct("eceba"))
print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))
