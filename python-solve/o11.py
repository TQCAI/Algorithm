from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l = 0
        r = len(numbers) - 1
        while l<r:
            mid=(l+r)//2
            if numbers[mid]<numbers[r]:
                r=mid
            elif numbers[mid]>numbers[r]:
                l=mid+1


print(Solution().minArray([3, 3, 1, 3]))
print(Solution().minArray([10, 1, 10, 10, 10]))
