class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)

        def expand_aroud_center(l, r):
            while l >= 0 and r < N and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        start, end = 0, 0
        for i in range(N):
            l1, r1 = expand_aroud_center(i, i)
            l2, r2 = expand_aroud_center(i, i + 1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start:end + 1]

Solution().longestPalindrome("babad")
