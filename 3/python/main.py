class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        cur_len = 0
        max_len = 0
        N = len(s)
        lookup = set()
        for i in range(N):
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            lookup.add(s[i])
            cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len

Solution().lengthOfLongestSubstring("abcabcbb")