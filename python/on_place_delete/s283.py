from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = nz = 0
        n = len(nums)
        while z < n and nz < n:
            while z < n and nums[z] != 0:
                z += 1
            while nz < n and nums[nz] == 0:
                nz += 1
            if z >= n or nz >= n:
                break
            if z < nz:
                nums[z], nums[nz] = nums[nz], nums[z]
            else:
                nz = z + 1
        print(nums)


Solution().moveZeroes([0, 1, 0, 3, 12])
Solution().moveZeroes([1, 0, 0])
Solution().moveZeroes([1, 0, 1])
