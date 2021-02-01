[剑指 Offer 38. 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)

[面试题38. 字符串的排列（回溯法，清晰图解）](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/solution/mian-shi-ti-38-zi-fu-chuan-de-pai-lie-hui-su-fa-by/)

我采用中规中矩的排列树做的，最后加个去重，并对两个参数的取值进行了思考

```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        path = list(s)
        ans = []
        L = len(path)

        def backtrace(t):
            # t == L 和 t == L - 1 一样
            # 因为如果 t == L 的话，在上一个状态 t=L-1时，
            # 是在做原地交换，相当于没做任何事
            # 所以 t == L - 1 即可
            if t == L - 1:  
                ans.append("".join(path))
                return
            # 初始条件必须是 t 而不是 t+1
            # t 看似是在原地交换，但是要考虑当前状态不做任何事的情况进入下个状态
            for i in range(t, L):  # i 最大为 L-1
                path[t], path[i] = path[i], path[t]
                backtrace(t + 1)
                path[t], path[i] = path[i], path[t]

        backtrace(0)
        return list(set(ans))
```

看了题解后，我做了修改

虽然时间复杂度还是 $O(N!)$ 但是实际的运行时间还是会减少的

```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        path = list(s)
        ans = []
        L = len(path)

        def backtrace(t):
            if t == L :  
                ans.append("".join(path))
                return
            visit = set()
            for i in range(t, L): 
                if path[i] in visit:
                    continue
                visit.add(path[i])
                path[t], path[i] = path[i], path[t]
                backtrace(t + 1)
                path[t], path[i] = path[i], path[t]

        backtrace(0)
        return list(set(ans))
```

