from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for num in nums[1:]:
            if num > dp[-1]:
                dp.append(num)
            else:
                l, r = 0, len(dp)
                while l < r:
                    mid = (l + r) // 2
                    if dp[mid] == num:
                        r = mid
                    elif dp[mid] < num:
                        l = mid + 1
                    else:
                        r = mid
                dp[l] = num
        print(dp)
        return len(dp)


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
