class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        end_map = collections.defaultdict(int)
        k = 3
        for x in nums:
            if counter.get(x):
                if end_map.get(x - 1):
                    counter[x] -= 1 # 将x添加到序列中
                    # 序列向右顺延
                    end_map[x - 1] -= 1
                    end_map[x] += 1
                else:
                    # 开始更新
                    for i in range(k):
                        if counter.get(x + i):
                            counter[x + i] -= 1  # 将x+i添加到序列中
                        else:
                            return False
                    # 构造了一条【最下可用序列】，序列的结尾为 x+k-1
                    end_map[x + k - 1] += 1
        return True
