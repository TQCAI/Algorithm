[剑指 Offer 03. 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)

[原地置换，时间空间100%](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/yuan-di-zhi-huan-shi-jian-kong-jian-100-by-derrick/)


```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i: # while 条件 是 符合排序后的条件
                if nums[i] == nums[nums[i]]: # 0 1 2 1 ， 发现了重复数字了
                    return nums[i]
                # 2 0 1
                # 1 0 2  // iter 1: 让 nums[nums[i]] 符合条件
                # 0 1 2  // iter 2 
                tmp = nums[i]
                nums[i] = nums[tmp]
                nums[tmp] = tmp
```

还有个二分法的情况，暂时看不懂

[03_02_DuplicationInArrayNoEdit](https://github.com/zhedahht/CodingInterviewChinese2/blob/master/03_02_DuplicationInArrayNoEdit/FindDuplicationNoEdit.cpp)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210130170434837.png)


