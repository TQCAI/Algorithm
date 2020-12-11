from typing import List
import copy


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        nums = []
        N = len(S)
        ans = None
        big = 2 ** 31 - 1

        def dfs(st=0):
            nonlocal ans, N, nums
            if st >= N:
                if len(nums) >= 3:
                    ok = True
                    for i in range(2, len(nums)):
                        if nums[i] != nums[i - 1] + nums[i - 2]:
                            ok = False
                            break
                    if ok:
                        ans = copy.deepcopy(nums)
                return
            if ans is not None:
                return
            for l in range(1, N - st + 1):
                s_num = S[st:st + l]
                num = int(s_num)
                if num > big:  # 放上来更优
                    break
                # 一个条件： 01 不可 0 可以
                if (not (s_num.startswith("0") and len(s_num) > 1)) and len(s_num):
                    if len(nums) < 2 or (nums[-1] + nums[-2] == num):
                        nums.append(num)
                        dfs(st + l)
                        nums.pop()
                    # 少了这个break条件就会只击败5%
                    if len(nums) >= 2 and num > nums[-2] + nums[-1]:
                        break

        dfs()
        if ans is not None:
            return ans
        return []


input = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
res = Solution().splitIntoFibonacci(input)
print(res)
