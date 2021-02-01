class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 需要转list，因为str不支持按索引修改
        nums = list(str(n))
        N = len(nums)
        i = N - 2
        # 若满足单调递减，则继续循环
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # 此时找到了第一个不满足单调递减的 i
        # 分情况讨论，如果整个排列都是单调递减的，不存在下个更大的排列
        if i >= 0:
            j = N - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            # 从右往左找到第一个略大于nums[i]的nums[j]
            # 交换两个元素
            nums[i], nums[j] = nums[j], nums[i]
            # 从i+1开始逆序。
            l, r = i + 1, N - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        else:
            return -1
        ans = int("".join(nums))
        return ans if ans < (1 << 32 - 1) else -1
