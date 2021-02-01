class Solution():
    def monotoneIncreasingDigits(self, N):
        max = -1
        idx = -1
        nums = [int(c) for c in str(N)]
        for i, num in enumerate(nums[:-1]):
            if max < num:
                max = num
                idx = i
            if num > nums[i + 1]:
                nums[idx] -= 1
                for j in range(idx + 1, len(nums)):
                    nums[j] = 9
                break
        return int("".join(map(str, nums)))


print(Solution().monotoneIncreasingDigits(1234))
