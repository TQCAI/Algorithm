class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        window = {}
        l = 0
        max_len = 0
        for r in range(len(s)):
            # 右端点元素进窗口之前，需要通过不断右移左端点保证当前窗口所有元素唯一
            window[s[r]] = window.get(s[r], 0) + 1
            while l < r and len(window) > 2:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    window.pop(s[l])
                l += 1
            max_len = max(max_len, r - l + 1)  # 可以用 len(windows)代替
        return max_len


print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))
