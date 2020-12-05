from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s_nums=sorted(nums)
        num2cnt={}
        for i,num in enumerate(s_nums):
            if num not in num2cnt:
                num2cnt[num]=i
        return [num2cnt[num] for num in nums]
