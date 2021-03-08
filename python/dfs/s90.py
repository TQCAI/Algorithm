from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # 1. 求集合就是组合问题
        # 2. nums中有重复数字：排列去重，排序(nums.sort)  剪枝(nums[i-1]==nums[i] and i>begin)
        # 3. nums中一个元素只能用一次，res不重复：组合去重，begin=i+1

        import copy
        def dfs(path, begin):
            res.append(copy.copy(path))
            for i in range(begin, size):
                if i > begin and nums[i - 1] == nums[i]:
                    continue
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()

        nums.sort()
        size = len(nums)
        path = []
        begin = 0
        res = []
        dfs(path, begin)
        return res


Solution().subsetsWithDup([1,2,2])