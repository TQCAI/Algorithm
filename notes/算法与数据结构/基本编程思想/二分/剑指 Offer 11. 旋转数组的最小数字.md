[剑指 Offer 11. 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)

写了半个小时，勉强AC，哭了

艹，看了下答案我还写对了，就是 `l = mid + 1` 是怎么来的我还没想清楚，我是试出来的

感觉官方的代码写的很诡异

[11_MinNumberInRotatedArray](https://github.com/zhedahht/CodingInterviewChinese2/blob/master/11_MinNumberInRotatedArray/MinNumberInRotatedArray.cpp)


时间复杂度： $O(N)$

```python
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l = 0
        r = len(numbers) - 1
        while l < r:
            mid = (l + r) // 2
            if numbers[l] >= numbers[r]:
                if numbers[mid] == numbers[r]:
                    l += 1
                elif numbers[mid] < numbers[r]:
                    r = mid
                else:
                    l = mid + 1
            else:
                return numbers[l]
        return numbers[r]
```


[153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)


```python
class Solution:
    def findMin(self, numbers: List[int]) -> int:
        l = 0
        r = len(numbers) - 1
        while l < r:
            mid = (l + r) // 2
            if numbers[l] >= numbers[r]:
                if numbers[mid] < numbers[r]:
                    r = mid
                else:
                    l = mid + 1
            else:
                return numbers[l]
        return numbers[r]
```

[154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)

```java
class Solution {
    public int findMin(int[] nums) {
        int low = 0;
        int high = nums.length - 1;
        while (low < high) {
            int pivot = low + (high - low) / 2;
            if (nums[pivot] < nums[high]) {
                high = pivot;
            } else if (nums[pivot] > nums[high]) {
                low = pivot + 1;
            } else {
                high -= 1;
            }
        }
        return nums[low];
    }
}
```


```python
class Solution:
    def findMin(self, numbers: List[int]) -> int:
        l = 0
        r = len(numbers) - 1
        while l < r:
            mid = (l + r) // 2
            if numbers[l] >= numbers[r]:
                if numbers[mid] == numbers[r]:
                    l += 1
                elif numbers[mid] < numbers[r]:
                    r = mid
                else:
                    l = mid + 1
            else:
                return numbers[l]
        return numbers[r]
```

