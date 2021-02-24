from typing import List


class Heap():
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        ix = len(self.heap) - 1
        while ix > 0:
            pix = (ix - 1) // 2
            if self.heap[pix] <= self.heap[ix]:
                break
            self.heap[ix], self.heap[pix] = self.heap[pix], self.heap[ix]
            ix = pix

    def pop(self):
        n = len(self.heap)
        self.heap[0], self.heap[n - 1] = self.heap[n - 1], self.heap[0]
        val = self.heap.pop()
        ix = 0
        n = len(self.heap)
        while True:
            lix = ix * 2 + 1
            rix = ix * 2 + 2
            if lix >= n:
                break
            if rix >= n:
                bix = lix
            else:
                bix = lix if self.heap[lix] < self.heap[rix] else rix
            if self.heap[ix] < self.heap[bix]:
                break
            self.heap[ix], self.heap[bix] = self.heap[bix], self.heap[ix]
            ix = bix
        return val

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

    def __repr__(self):
        return repr(self.heap)


def heap_sort(nums):
    heap = Heap()
    for num in nums:
        heap.push(num)
    res = []
    while len(heap):
        res.append(heap.pop())
    return res


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return heap_sort(nums)


# import random
# nums = list(range(10))
# random.shuffle(nums)
nums = [5, 2, 3, 1]

print(Solution().sortArray(nums))
