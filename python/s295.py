import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 较小数字，大根堆
        self.lo = []
        # 较大数字，小根堆
        self.hi = []


    def addNum(self, num: int) -> None:
        # 保持平衡，lo -> hi 倒腾一下
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        # 按照规定，lo对hi多一个数字（奇数时）
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        return (self.hi[0] + (-self.lo[0])) / 2 if len(self.hi) == len(self.lo) else -self.lo[0]
