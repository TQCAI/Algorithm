[剑指 Offer 40. 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)

时间复杂度 $O(N \log K)$

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for num in arr:
            heapq.heappush(heap, -num)
            if len(heap) > k:
                heapq.heappop(heap)
        return [-x for x in heap]
```

[4种解法秒杀TopK（快排/堆/二叉搜索树/计数排序）❤️](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/3chong-jie-fa-miao-sha-topkkuai-pai-dui-er-cha-sou/)

