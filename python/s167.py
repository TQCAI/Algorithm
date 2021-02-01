from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i <= j:
            m = (i + j) // 2
            if numbers[i] + numbers[m] == target:
                return [i, j]
            if numbers[i] + numbers[m] > target:
                j = m - 1
            elif numbers[m] + numbers[j] < target:
                i = m + 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
        return [-1, -1]
