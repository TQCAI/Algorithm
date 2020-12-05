from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        K = 100
        counts = [0 for _ in range(K + 1)]
        for num in nums:
            counts[num] += 1
        for i in range(1, K + 1):
            counts[i] += counts[i - 1]
        return [counts[num - 1] if num else 0 for num in nums]
