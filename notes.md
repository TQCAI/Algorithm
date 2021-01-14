
@[toc]
# 语法 
## Java语法 
[java类似python collections.Counter的用法](https://stackoverflow.com/questions/32348453/python-counter-alternative-for-java)

[集合互转](https://blog.csdn.net/u014532901/article/details/78820124)

[`int[], Integer[], List<Integer>, List<String> 互相转换`](https://blog.csdn.net/jiangge123456/article/details/95794928)

## CPP语法

[C++语法汇总](https://blog.csdn.net/TQCAI666/article/details/110731835)
 
# 链表
## 001. Java链表结点定义

```java
package structure;

public class ListNode {
    public int val;
    public ListNode next;

    public ListNode() {
    }

    public ListNode(int val) {
        this.val = val;
    }

    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    public static ListNode fromArray(int[] list) {
        ListNode head = null;
        ListNode tail = null;
        for (int item : list) {
            ListNode node = new ListNode(item);
            if (head == null) {
                head = node;
                tail = node;
            } else {
                tail.next = node;
                tail = node;
            }
        }
        return head;
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder();
        ListNode p = this;
        while (p != null) {
            res.append(p.val).append(" -> ");
            p = p.next;
        }
        res.append("O");
        return res.toString();
    }
}

```

## 002. Python链表结点定义

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def fromList(lst):
        head = None
        tail = None
        for item in lst:
            node = ListNode(item)
            if head is None:
                head = node
                tail = head
            else:
                tail.next = node
                tail = node
        return head

    def __str__(self):
        p = self
        res = ""
        while p is not None:
            res += f"{p.val} -> "
            p = p.next
        res += "O"
        return res

    __repr__ = __str__
```

## 19. 删除链表的倒数第N个节点
[19. 删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)

瞎写的

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        k = 0
        p2 = None
        while p is not None:
            p = p.next
            k += 1
            if (k - 1) == n:
                p2 = head
            if (k - 1) > n:
                p2 = p2.next
        if p2 is None and k == n:
            head = head.next
        elif p2.next is not None:
            p2.next = p2.next.next
        return head
```

官方题解

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next
```

还是官方的好， 我写的和屎一样。希望能默写一下官方题解

## 206. 反转链表
[206. 反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)

**迭代法**

时间复杂度：$\mathcal O(n)$
空间复杂度：$\mathcal O(1)$

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        p = head
        while p is not None:
            tmp = p.next
            p.next = pre
            pre = p
            if tmp is None:
                break
            p = tmp
        return p
```

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        p = head
        while p is not None:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        return pre
```

**递归法**

时间复杂度：$\mathcal O(n)$
空间复杂度：$\mathcal O(n)$


```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node
```

说实话有点没看懂

## 143. 重排链表
[143. 重排链表](https://leetcode-cn.com/problems/reorder-list/)

乱写的解法

```python
import math

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        p = head
        while p is not None:
            nodes.append(p)
            pre = p
            p = p.next
            pre.next = None
        N = len(nodes)
        mid = math.floor(len(nodes) / 2)
        list2 = list(reversed(nodes[mid:]))
        list1 = nodes[:mid]
        if len(list2) > len(list1):
            list1.append(list2.pop())
        lst = [list1, list2]
        for i in range(N):
            if i == 0:
                head = list1[0]
                p = head
            else:
                p.next = lst[i % 2][i // 2]
                p = p.next

```

按照题解默写的线性表解法

```python
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None:
            return None
        p = head
        vec = []
        while p is not None:
            vec.append(p)
            p = p.next
        i = 0
        j = len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1
        vec[i].next = None  # 容易想错
```


## 234. 回文链表
[234. 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list/)
快慢指针 + 翻转链表
```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pre = None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            tmp = slow.next
            slow.next = pre
            pre = slow
            fast = fast.next.next
            slow = tmp
```

## 21. 合并两个有序链表

[21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

瞎写的不带头结点的方法

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pp = None
        res = None
        p1 = l1
        p2 = l2
        while p1 is not None or p2 is not None:
            if p1 is None and p2 is not None:
                p = p2
                p2 = p2.next
            elif p1 is not None and p2 is None:
                p = p1
                p1 = p1.next
            else:
                if p1.val < p2.val:
                    p = p1
                    p1 = p1.next
                else:
                    p = p2
                    p2 = p2.next
            if pp is not None:
                pp.next = p
                pp = pp.next
            else:
                pp = res = p
        return res
```

看了题解后写的带头结点的方法

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pp = dummy = ListNode(-1)
        p1 = l1
        p2 = l2
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                p = p1
                p1 = p1.next
            else:
                p = p2
                p2 = p2.next
            pp.next = p
            pp = pp.next
        pp.next = p1 if p1 is not None else p2
        return dummy.next
```


## 2. 两数相加
[2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/solution/)
```python

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        ret = None
        p = None
        carry = 0
        while p1 is not None or p2 is not None:
            v1 = p1.val if p1 is not None else 0
            v2 = p2.val if p2 is not None else 0
            num = v1 + v2 + carry
            node = ListNode(num % 10)
            carry = num // 10
            if ret is None:
                ret = node
                p = ret
            else:
                p.next = node
                p = p.next
            p1 = p1.next if p1 is not None else None
            p2 = p2.next if p2 is not None else None
        if carry:
            p.next = ListNode(carry)
        return ret
```

## 328. 奇偶链表
[328. 奇偶链表](https://leetcode-cn.com/problems/odd-even-linked-list/)
```python
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None: # 用例 []
            return None
        odds = None
        evens = None
        index = 1
        p = head
        evens_head = None
        while p is not None:
            if index % 2:
                if odds is not None:
                    odds.next = p
                odds = p
            else:
                if evens is not None:
                    evens.next = p
                else:
                    evens_head = p
                evens = p
            p = p.next
            index += 1
        if evens is not None:  # 用例 [1]
            evens.next = None  # 注意了
        odds.next = evens_head
        return head
```

```python
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        oddHead, evenHead = head, head.next
        odd, even = oddHead, evenHead
        while even and even.next:
            odd.next = even.next
            odd = odd.next         # 别忘了自己要移动
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
```

## 141. 环形链表
[141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)


```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not slow or not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
```

## 147. 链表插入排序

[官方题解](https://leetcode-cn.com/problems/insertion-sort-list/solution/dui-lian-biao-jin-xing-cha-ru-pai-xu-by-leetcode-s/)

[147. 对链表进行插入排序](https://leetcode-cn.com/problems/insertion-sort-list/)

```python
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        lastSorted = head
        curr = head.next
        while curr:
            # 排序区最后的元素小于等于当前元素，把当前元素放排序区后面就行
            if lastSorted.val <= curr.val:
                lastSorted = lastSorted.next
            # 否则
            else:
                prev = dummyHead
                while prev.next.val <= curr.val:
                    prev = prev.next
                # prev.next.val > curr.val
                # prev.val <= curr.val
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastSorted.next
        return dummyHead.next
```



## 148. 链表归并排序

[148. 排序链表](https://leetcode-cn.com/problems/sort-list/)

- 伪代码

merge函数参考 [merge-two-sorted-lists](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

```python
subLength = 1 
while subLength < len(listNode):
	构造 prev, curr
	while curr 非空:
		构造head1, head2, 两个链表长度为subLengh, 结尾为空
		将curr指向下一个节点
		合并两个有序链表
		构造新的prev
	subLength *= 2
```


```python
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        if not head:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummyHead = ListNode(0, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                # 构造 head1
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                # 构造 head2
                head2 = curr.next
                curr.next = None  # head1 结尾为空
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break
                # 将curr指向下一个节点，并让head2 结尾为空
                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None
                curr = succ
                # 合并两个有序链表
                merged = merge(head1, head2)
                # 套到上一个节点上
                prev.next = merged
                # 构造新的prev
                while prev.next:
                    prev = prev.next
            subLength *= 2

        return dummyHead.next
```

## 23. 合并K个升序链表

[23. 合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/)

- 分治合并

```java
class Solution {
    public ListNode mergeTwoLists(ListNode a, ListNode b) {
        if (a == null || b == null) {
            return a != null ? a : b;
        }
        ListNode head = new ListNode(0);
        ListNode tail = head, aPtr = a, bPtr = b;
        while (aPtr != null && bPtr != null) {
            if (aPtr.val < bPtr.val) {
                tail.next = aPtr;
                aPtr = aPtr.next;
            } else {
                tail.next = bPtr;
                bPtr = bPtr.next;
            }
            tail = tail.next;
        }
        tail.next = (aPtr != null ? aPtr : bPtr);
        return head.next;
    }

    public ListNode merge(ListNode[] lists, int l, int r) {
        if (l == r) {
            return lists[l];
        }
        if (l > r) {
            return null;
        }
        int mid = (l + r) >> 1;
        return mergeTwoLists(
                merge(lists, l, mid),
                merge(lists, mid + 1, r)
        );
    }

    public ListNode mergeKLists(ListNode[] lists) {
        return merge(lists, 0, lists.length - 1);
    }
}
```

- 堆排序

```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<Status> queue = new PriorityQueue<>();
        for (ListNode node : lists) {
            if (node != null) {
                queue.offer(new Status(node.val, node));
            }
        }
        ListNode head = new ListNode(0);
        ListNode tail = head;
        while (!queue.isEmpty()) {
            Status f = queue.poll();
            tail.next = f.ptr;
            tail = tail.next;
            if (f.ptr.next != null) {
                queue.offer(new Status(f.ptr.next.val, f.ptr.next));
            }
        }
        return head.next;
    }

    class Status implements Comparable<Status> {
        int val;
        ListNode ptr;

        Status(int val, ListNode ptr) {
            this.val = val;
            this.ptr = ptr;
        }

        public int compareTo(Status status2) {
            return this.val - status2.val;
        }
    }
}
```

## 86. 分隔链表

[86. 分隔链表](https://leetcode-cn.com/problems/partition-list/)

```python
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        head1 = ListNode(0)
        p1 = head1
        head2 = ListNode(0)
        p2 = head2
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        if head1.next is None:
            return head2.next
        if head2.next is None:
            return head1.next
        p1.next = head2.next
        p2.next = None
        return head1.next
```

# 基本编程思想

## 二分


### 001. labuladong框架

>搜索一个元素时，搜索区间两端闭
>while条件带等号，否则需要打补丁
>if相等就返回，其他事情甭操心
>mid必须加减一，因为区间两端闭
>while结束就凉了，凄凄惨惨返-1

>搜索左右区间时，搜索区间要阐明
>左闭右开最常见，其余逻辑便自明
>while要用小于号，这样才能不漏掉
>if相等别返回，利用mid锁边界

```python
nums = [1, 1, 3, 6, 6, 6, 7, 8, 8, 9]


def binary_search(nums, target):
    '''找一个数'''
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        # 如果是Java Cpp
        # mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    return -1


print("binary_search", binary_search(nums, 6))


def lower_bound(nums, target):
    '''找左边界'''
    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            r = mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid
    # 对未命中情况进行后处理
    if l == len(nums):
        return -1
    return l if nums[l] == target else -1


print("lower_bound", lower_bound(nums, 6))
print("lower_bound", lower_bound(nums, 2))


def upper_bound(nums, target):
    '''找右边界'''
    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            l = mid + 1
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid
    if l == 0:
        return -1
    return l - 1 if nums[l - 1] == target else -1


print("upper_bound", upper_bound(nums, 100))
print("upper_bound", upper_bound(nums, -1))
print("upper_bound", upper_bound(nums, 2))
print("upper_bound", upper_bound(nums, 6))
```


### 002. 实现lower_bound与upper_bound
- 默写labuladong算法小抄

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(nums, target):
            l = 0
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    r = mid
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid
            if l >= len(nums):
                return -1
            return l if nums[l] == target else -1
        def upper_bound(nums, target):
            l = 0
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid
            if l == 0:
                return -1
            return l - 1 if nums[l - 1] == target else -1
        return [lower_bound(nums, target), upper_bound(nums, target)]

```


[LeetCode官方题解](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/zai-pai-xu-shu-zu-zhong-cha-zhao-yuan-su-de-di-3-4/)将LB与UB整合到了一行代码中(cpp)


> 并且二分查找的具体方式也有所不同


```cpp
int binarySearch(vector<int>& nums, int target, bool lower) {
    int left = 0, right = (int)nums.size() - 1, ans = (int)nums.size();
    while (left <= right) {
        int mid = (left + right) / 2;
        if (nums[mid] > target || (lower && nums[mid] >= target)) {
            right = mid - 1;
            ans = mid;
        } else {
            left = mid + 1;
        }
    }
    return ans;
}
```

翻译成python代码

```python
def binary_search(nums, target, lower):
    l = 0
    r = len(nums) - 1
    ans = len(nums)
    while l <= r:  # diff
        mid = (l + r) // 2
        # 满足左边就一定会满足右边
        if (nums[mid] > target) or (lower and nums[mid] >= target):
            r = mid - 1  # diff
            ans = mid  # diff
        else:
            l = mid + 1  # common
    return ans
```

> TODO: 更深入地学习labuladong算法小抄中关于二分的部分


练习题： [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)


### 300. 最长递增子序列

[300. 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)

贪心 + 二分

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        N = len(nums)
        dp = []
        for i, num in enumerate(nums):
            if len(dp) == 0 or dp[-1] < num:
                dp.append(num)
            else:
                # lower_bound
                l = 0
                r = len(dp)
                while l < r:
                    mid = (l + r) // 2
                    if dp[mid] == num:
                        r = mid
                    elif dp[mid] < num:
                        l = mid + 1
                    elif dp[mid] > num:
                        r = mid
                dp[l] = num
        return len(dp)
```

### 4. 寻找两个正序数组的中位数
[4. 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)

[题解：详细通俗的思路分析， 多解法](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/)
上述题解的题解3需要再看一下，感觉写的比官方的简洁

下面的解法参考官方题解`两个有序数组的第k元素`的方法，还有些不熟悉的地方。

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            index1 = index2 = 0
            while True:
                # 特殊情况(写错了)
                # if index1 + k > n - 1:
                #     return nums1[n - 1]
                # elif index2 + k > m - 1:
                #     return nums2[m - 1]
                # elif k == 1:
                #     return min(nums1[index1 + k], nums2[index2 + k])
                # ---------------------------
                # nums1 普遍偏小的情况
                if index1 == n:
                    return nums2[index2 + k - 1]
                # nums2 普遍偏小的情况
                if index2 == m:
                    return nums1[index1 + k - 1]
                # 死循环退出条件
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                # 正常情况
                half = k // 2
                new_index1 = min(index1 + half - 1, n - 1)
                new_index2 = min(index2 + half - 1, m - 1)
                if nums1[new_index1] < nums2[new_index2]:
                    k -= new_index1 - index1 + 1
                    index1 = new_index1 + 1  # 忘了 + 1
                else:
                    k -= new_index2 - index2 + 1
                    index2 = new_index2 + 1  # 忘了 + 1

        n = len(nums1)
        m = len(nums2)
        total_len = (n + m)
        if total_len % 2:
            return getKthElement((total_len + 1) // 2)
        else:
            return (getKthElement(total_len // 2) + getKthElement(total_len // 2 + 1)) / 2

```

### 33. 搜索旋转排序数组
[33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        N = len(nums)
        l = 0
        r = N - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 左边有序
            # “左边有序”的判断一定要<=，其他的判断可以无脑两个<=
            # if nums[0] < nums[mid]:
            if nums[0] <= nums[mid]:
                # 目标值在左边
                # if nums[0] <= target <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # 右边有序
            else:
                # 目标值在右边
                # if nums[mid] <= target <= nums[N - 1]:
                if nums[mid] < target <= nums[N - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
```

### 167. 两数之和 II - 输入有序数组
[167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

- 二分

时间 $O(N\log N)$  空间 $O(N)$
```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        for (int i = 0; i < numbers.length; ++i) {
            int low = i + 1, high = numbers.length - 1;
            while (low <= high) {
                int mid = (high - low) / 2 + low;
                if (numbers[mid] == target - numbers[i]) {
                    return new int[]{i + 1, mid + 1};
                } else if (numbers[mid] > target - numbers[i]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
        }
        return new int[]{-1, -1};
    }
}
```

- 双指针

时间 $O(N)$  空间 $O(1)$

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int low = 0, high = numbers.length - 1;
        while (low < high) {
            int sum = numbers[low] + numbers[high];
            if (sum == target) {
                return new int[]{low + 1, high + 1};
            } else if (sum < target) {
                ++low;
            } else {
                --high;
            }
        }
        return new int[]{-1, -1};
    }
}
```

- 双指针 + 二分

时间 ：最好 $O(\log N)$   ，最坏 $O(N)$   

```java
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0, j = numbers.length - 1;
        while (i < j) {
            int m = (i + j) >>> 1;
            if (numbers[i] + numbers[m] > target) {
                j = m - 1;
            } else if (numbers[m] + numbers[j] < target) {
                i = m + 1;
            } else if (numbers[i] + numbers[j] > target) {
                j--;
            } else if (numbers[i] + numbers[j] < target) {
                i++;
            } else {
                return new int[]{i + 1, j + 1};
            }
        }
        return new int[]{0, 0};
    }
}
```

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i <= j:
            m = (i + j) // 2
            if numbers[i] + numbers[m] > target:
                j = m - 1
            elif numbers[m] + numbers[j] < target:
                i = m + 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i + 1, j + 1]
        return [-1, -1]
```

## 分治
### 240. 搜索二维矩阵 II
[240. 搜索二维矩阵 II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/)
```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        N = len(matrix)
        if not N:
            return False
        M = len(matrix[0])
        i = N - 1
        j = 0
        while i >= 0 and j < M:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return False
```

## 	贪心
### 621. 任务调度器

- 模拟法

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        rest = list(freq.values())
        M = len(rest)
        nextValid = [1] * M
        time = 0
        for _ in tasks:
            time += 1
            # 下一个最早可用时间
            minNextValid = min(nextValid[i] for i in range(M) if rest[i] > 0)
            time = max(time, minNextValid)  # 写错成了min
            best = -1
            for i in range(M):
                # 在剩余任务中，时间满足
                if rest[i] > 0 and nextValid[i] <= time:
                    # 剩余次数最多
                    if best == -1 or rest[i] > rest[best]:
                        best = i
            rest[best] -= 1
            # 根据样例、需要间隔n个
            nextValid[best] = time + n + 1
        return time
```

- 构造法
```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        maxExec = max(freq.values())
        maxCount = sum(1 for cnt in freq.values() if cnt == maxExec)
        return max(  # 没想到
            (maxExec - 1) * (n + 1) + maxCount,
            len(tasks)  # 没想到
        )
```

### 861. 翻转矩阵后的得分

[861. 翻转矩阵后的得分](https://leetcode-cn.com/problems/score-after-flipping-matrix/)

```cpp
class Solution {
public:
    int matrixScore(vector<vector<int>> &A) {
        int m = A.size(), n = A[0].size();
        //m 行 n 列
        int ret = m * (1 << (n - 1)); // 忘了 m * ()
        // 先“翻转”行再“翻转”列。翻转行必然使第一列全为1
        for (int j = 1; j < n; ++j) { //遍历第j列
            int nOnes = 0;
            for (int i = 0; i < m; ++i) { //第i行
                if (A[i][0] == 1) {  //如果某一行第一列是0，该行会翻转
                    nOnes += A[i][j]; // 手抖写成  A[i][0]
                } else {
                    nOnes += (1 - A[i][j]);
                }
            }
            int k = max(nOnes, m - nOnes);
            ret += k * (1 << (n - 1 - j));
        }
        return ret;
    }
};
```
### 860. 柠檬水找零

先把大面额的钱找出去

```python
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = dict(zip([5, 10, 20], [0] * 3))
        for bill in bills:
            if bill == 5:
                counter[5] += 1
            elif bill == 10:
                if counter[5] < 1:
                    return False
                counter[5] -= 1
                counter[10] += 1
            else: # 20
                if counter[10] >=1 and counter[5] >= 1:
                    counter[5] -= 1
                    counter[10] -= 1
                elif counter[5] >= 3:
                    counter[5] -= 3
                else:
                    return False
        return True
```


### 649. Dota2 参议院

[649. Dota2 参议院](https://leetcode-cn.com/problems/dota2-senate/)

自己瞎写， 超时

```python
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        ix = 0
        senate = list(senate)
        while True:
            if len(senate) == 1:
                break
            for i in itertools.chain(
                    range(ix + 1, len(senate)),
                    range(ix),
            ):
                if senate[i] != senate[ix]:
                    del senate[i]
                    break
            ix += 1
            if ix >= len(senate):
                ix = 0
        return "Dire" if senate[0] == "D" else "Radiant"
```

官方题解

```python
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_list = collections.deque()
        d_list = collections.deque()

        for i, ch in enumerate(senate):
            if ch == "R":
                r_list.append(i)
            else:
                d_list.append(i)

        while r_list and d_list:
            if r_list[0] < d_list[0]:
                r_list.append(r_list[0] + n)
            else:
                d_list.append(d_list[0] + n)
            r_list.popleft()
            d_list.popleft()

        return "Radiant" if r_list else "Dire"
```

> TODO: 
> 自己写一遍

### 376. 摆动序列
[376. 摆动序列](https://leetcode-cn.com/problems/wiggle-subsequence/)



```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            # 考虑长度为 1 和 0 的情况
            return N
        pre_delta = nums[1] - nums[0]
        ans = 1 if pre_delta == 0 else 2
        for i in range(2, N):
            delta = nums[i] - nums[i - 1]
            if (delta > 0 and pre_delta <= 0) or (delta < 0 and pre_delta >= 0):
                ans += 1
                pre_delta = delta
        return ans
```

> TODO: 
> 自己写一遍
> 看DP题解




### 135. 分发糖果
[135. 分发糖果](https://leetcode-cn.com/problems/candy/)

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        L = len(ratings)
        left = [1] * L
        right = [1] * L
        for i in range(1, L):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        cnt = left[L - 1]
        for i in reversed(range(0, L - 1)):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            cnt += max(left[i], right[i])
        return cnt
```

### 455. 分发饼干
排序+贪心
```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        s_N = len(s)
        s_start = 0
        cnt = 0
        for child_demand in g:
            while s_start < s_N:
                biscuit = s[s_start]
                s_start += 1
                if biscuit >= child_demand:
                    cnt += 1
                    break
            if s_start >= s_N:
                break
        return cnt
```

### 605. 种花问题

[605. 种花问题](https://leetcode-cn.com/problems/can-place-flowers/)

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)

        def available(i):
            if flowerbed[i] == 0 and \
                    (i == 0 or flowerbed[i - 1] == 0) and \
                    (i == N - 1 or flowerbed[i + 1] == 0):
                return True
            return False

        cnt = 0
        for i in range(N):
            if available(i):
                cnt += 1
                flowerbed[i] = 1
        return n <= cnt
```

官方题解看不懂，这个题解思路和我一样，但是会提前return，比我做得好。

[【1】种花问题：简单的贪心](https://leetcode-cn.com/problems/can-place-flowers/solution/1-chong-hua-wen-ti-jian-dan-de-tan-xin-b-h8xb/)

```cpp
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        for(int i=0; i<flowerbed.length; i++) {
            if(flowerbed[i] == 0 && (i == 0 || flowerbed[i-1] == 0) && (i == flowerbed.length-1 || flowerbed[i+1] == 0)) {
                n--;
                if(n <= 0) return true;
                flowerbed[i] = 1;
            }
        }

        return n <= 0;
    }
}
```

# 搜索法
## 回溯法
### 51. N 皇后
[51. N 皇后](https://leetcode-cn.com/problems/n-queens/)
baseline
```python
from typing import List
class Solution:

    def dfs(self, i):
        if i >= self.n:
            self.res.append(["".join(row) for row in self.board])
            return
        for j in range(self.n):
            if self.isValid(i, j):
                self.board[i][j] = "Q"
                self.dfs(i + 1)
                self.board[i][j] = "."

    def isValid(self, x, y):
        for i in range(x):
            if self.board[i][y] == "Q":
                return False
        for j in range(y):
            if self.board[x][j] == "Q":
                return False
        i = x - 1
        j = y - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        i = x - 1
        j = y + 1
        while i >= 0 and j < self.n:
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.board = [['.' for i in range(n)] for j in range(n)]
        self.res = []
        self.dfs(0)
        return self.res
```


打表
```java
class Solution {
	public int totalNQueens(int n) {
        int[] rs = new int[]{0,1,0,0,2,10,4,40,92,352,724,2680};
        return rs[n];
    }
}
```

对角线数组优化（python）

```python
class Solution:

    def dfs(self, i):
        if i >= self.n:
            self.res.append(["".join(row) for row in self.board])
            return
        n = self.n
        for j in range(n):
            dgi = i - j + n
            udgi = i + j
            if self.col[j] != 1 and self.dg[dgi] != 1 and self.udg[udgi] != 1:
                self.board[i][j] = "Q"
                self.col[j] = self.dg[dgi] = self.udg[udgi] = 1
                self.dfs(i + 1)
                self.board[i][j] = "."
                self.col[j] = self.dg[dgi] = self.udg[udgi] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.res = []
        self.col = [0] * n
        self.dg = [0] * (n * 2)
        self.udg = [0] * (n * 2)
        self.dfs(0)
        return self.res
```


对角线数组优化（java）

```java

class Solution {
    int n = 0;
    List<List<String>> res;
    int[] queens;
    int[] col;
    int[] dg;
    int[] udg;

    public void dfs(int i) {
        if (i == n) {
            res.add(getBoard(queens));
        }
        for (int j = 0; j < n; j++) {
            int dgi = i - j + n;
            int udgi = i + j;
            if (col[j] != 1 && dg[dgi] != 1 && udg[udgi] != 1) {
                queens[i] = j;
                col[j] = dg[dgi] = udg[udgi] = 1;
                dfs(i + 1);
                col[j] = dg[dgi] = udg[udgi] = 0;
            }
        }
    }

    public List<String> getBoard(int[] queens) {
        List<String> board = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            char[] row = new char[n];
            Arrays.fill(row, '.');
            row[queens[i]] = 'Q';
            board.add(new String(row));
        }
        return board;
    }

    public List<List<String>> solveNQueens(int n) {
        this.n = n;
        res = new ArrayList<>();
        queens = new int[n];
        col = new int[n];
        dg = new int[n * 2];
        udg = new int[n * 2];
        dfs(0);
        return res;
    }
}
```




###  842. 将数组拆分成斐波那契序列

[842. 将数组拆分成斐波那契序列](https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/)

自己花了一个小时写出来的屎一样的代码
```python
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        nums = []
        N = len(S)
        ans = None
        big = 2 ** 31 - 1

        def dfs(st=0):
            nonlocal ans, N, nums
            if st >= N:
                if len(nums) >= 3:
                    ok = True
                    for i in range(2, len(nums)):
                        if nums[i] != nums[i - 1] + nums[i - 2]:
                            ok = False
                            break
                    if ok:
                        ans = copy.deepcopy(nums)
                return
            if ans is not None:
                return
            for l in range(1, N - st + 1):
                s_num = S[st:st + l]
                num = int(s_num)
                if num > big:  # 放上来更优
                    break
                # 一个条件： 01 不可 0 可以
                if (not (s_num.startswith("0") and len(s_num) > 1)) and len(s_num):
                    if len(nums) < 2 or (nums[-1] + nums[-2] == num):
                        nums.append(num)
                        dfs(st + l)
                        nums.pop()
                    # 少了这个break条件就会只击败5%
                    if len(nums) >= 2 and num > nums[-2] + nums[-1]:
                        break

        dfs()
        if ans is not None:
            return ans
        return []
```

题解代码：

```python
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = list()

        def backtrack(index: int):
            if index == len(S):
                return len(ans) >= 3

            curr = 0
            for i in range(index, len(S)):
                if i > index and S[index] == "0":
                    break
                curr = curr * 10 + ord(S[i]) - ord("0")
                if curr > 2**31 - 1:
                    break

                if len(ans) < 2 or curr == ans[-2] + ans[-1]:
                    ans.append(curr)
                    if backtrack(i + 1):
                        return True
                    ans.pop()
                # 将 > 2 改为 >= 2, 提交无问题
                elif len(ans) >= 2 and curr > ans[-2] + ans[-1]:
                    break

            return False

        backtrack(0)
        return ans
```
### 17. 电话号码的字母组合
[17. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
```
- 方法1. 自己实现的循环法
```python
        results = [""]

        for digit in digits:
            cur_results = []
            for result in results:
                for alpha in phoneMap[digit]:
                    cur_results.append(result + alpha)
            results = cur_results

        return results
```
- 方法2. 回溯法

```python
        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = list()
        combinations = list()
        backtrack(0)
        return combinations
```
- 方法3. 调用python自带的`itertools.product`方法

```python
        groups = (phoneMap[digit] for digit in digits)
        return ["".join(combination) for combination in itertools.product(*groups)]
```

## DFS

### 129. 求根到叶子节点数字之和

[129. 求根到叶子节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/)

```python
class Solution:
    sum_list = []

    def dfs(self, node, sum):
        if node is not None:
            cur_sum = sum + str(node.val)
            self.dfs(node.left, cur_sum)
            self.dfs(node.right, cur_sum)
            if node.left is None and node.right is None:
                self.sum_list.append(cur_sum)

    def sumNumbers(self, root: TreeNode) -> int:
        self.sum_list = []
        self.dfs(root, "")
        return sum(map(int, self.sum_list))
```
   
###  22. 括号生成

[22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)

dfs是我自己写的方法，dfs_ok是我参考了题解写的方法，考虑了左括号的限值条件，去掉了递归终点处的冗余判断。

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s, l_cnt):
            nonlocal res
            if len(s) >= n * 2:
                if l_cnt == 0:  # 需要加个判断，去掉非法解
                    res.append(s)
                return
            # left
            dfs(s + "(", l_cnt + 1)
            # right
            if l_cnt > 0:
                dfs(s + ")", l_cnt - 1)

        def dfs_ok(s, l_cnt, r_cnt):
            nonlocal res
            if len(s) >= n * 2:
                res.append(s)
                return
            # left
            if l_cnt < n:
                dfs_ok(s + "(", l_cnt + 1, r_cnt)
            # right
            if l_cnt > r_cnt:
                dfs_ok(s + ")", l_cnt, r_cnt + 1)

        # dfs("", 0)
        dfs_ok("", 0, 0)
        return res
```


结合缓存的方法是最快的
```python
class Solution:
    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        ans = []
        for c in range(n):
            for l in self.generateParenthesis(c):
                for r in self.generateParenthesis(n - 1 - c):
                    ans.append("({}){}".format(l, r))
        return ans
```

C++的题解用到了`shared_ptr`，可以看看。

## BFS
### 463. 岛屿的周长

算周长应该按邻接水域来算（4连通相邻元素有多少为`0`），而不是我写的这样，考虑邻接的陆地然后再动态调整（增加了一些不必要的变量，`mark`,  ）

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        vis = [[0 for _ in range(M)] for _ in range(N)]
        mark = [[0 for _ in range(M)] for _ in range(N)]
        deltas = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1),
        ]

        def is_valid(cx, cy):
            return 0 <= cx < N and 0 <= cy < M

        def get_perimeter(x, y):
            res = 4
            for dx, dy in deltas:
                cx = x + dx
                cy = y + dy
                if is_valid(cx, cy) and mark[cx][cy] == 1:
                    res -= 2
            return res
            # 恰有一个岛屿

        sum_p = 0
        for i, rows in enumerate(grid):
            for j, elem in enumerate(rows):
                if elem and vis[i][j] == 0:
                    queue = [(i, j)]
                    vis[i][j] = 1
                    while len(queue) > 0:
                        tx, ty = queue.pop(0)
                        sum_p += get_perimeter(tx, ty)
                        mark[tx][ty] = 1
                        for dx, dy in deltas:
                            cx = tx + dx
                            cy = ty + dy
                            if is_valid(cx, cy) and vis[cx][cy] == 0 and grid[cx][cy] == 1:
                                vis[cx][cy] = 1
                                queue.append((cx, cy))
                    return sum_p
```

按照官方题解的方法改造为用邻接水域来统计周长

注意非法元素（`is_valid = False`）也算周长

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        vis = [[0 for _ in range(M)] for _ in range(N)]
        deltas = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1),
        ]

        def is_valid(cx, cy):
            return 0 <= cx < N and 0 <= cy < M

        def bfs(i, j):
            sum_p = 0
            queue = [(i, j)]
            vis[i][j] = 1
            while len(queue) > 0:
                tx, ty = queue.pop(0)
                for dx, dy in deltas:
                    cx = tx + dx
                    cy = ty + dy
                    if is_valid(cx, cy):
                        if grid[cx][cy] == 0:
                            sum_p += 1
                        if vis[cx][cy] == 0 and grid[cx][cy] == 1:
                            vis[cx][cy] = 1
                            queue.append((cx, cy))
                    else:
                        sum_p += 1
            return sum_p

        # 恰有一个岛屿
        for i, rows in enumerate(grid):
            for j, elem in enumerate(rows):
                if elem and vis[i][j] == 0:
                    return bfs(i, j)
```

[卷积法](https://leetcode-cn.com/problems/island-perimeter/solution/python-juan-ji-by-comiee/)





### 111. 二叉树的最小深度

[111. 二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)

我的题解

```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        cnt = 0
        while queue:
            sz = len(queue)
            find_none = False
            for _ in range(sz):
                top = queue.pop(0)
                null_cnt = 0
                if top.left:
                    queue.append(top.left)
                else:
                    null_cnt += 1
                if top.right:
                    queue.append(top.right)
                else:
                    null_cnt += 1
                if null_cnt==2:
                    find_none = True
            cnt += 1
            if find_none:
                return cnt
        return cnt
```

官方题解

```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
        
        return 0
```

## 双向BFS

### 752. 打开转盘锁

[752. 打开转盘锁](https://leetcode-cn.com/problems/open-the-lock/)

- 普通BFS

普通BFS在**入队**的时候需要**判断**与**标记**

```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = []
        vis = set()
        origin = "0000"
        queue.append(origin)
        vis.add(origin)
        invalid_set = set(deadends)
        if origin in invalid_set:
            return -1

        def modify(state, i, delta):
            c = state[i]
            c = str((int(c) + delta) % 10)
            return state[:i] + c + state[i + 1:]

        cnt = 0
        while queue:
            sz = len(queue)
            while sz:
                state = queue.pop(0)
                if state == target:
                    return cnt
                for delta in (-1, 1):
                    for i in range(4):
                        sub_state = modify(state, i, delta)
                        if sub_state not in vis and sub_state not in invalid_set:
                            vis.add(sub_state)
                            queue.append(sub_state)
                sz -= 1
            cnt += 1
        return -1

```

双向BFS在入队时不需要任何操作，在**出队**后需要**判断**与**标记**

- 双向BFS在入队

```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        origin = "0000"
        invalid_set = set(deadends)
        if origin in invalid_set:
            return -1

        def modify(state, i, delta):
            c = state[i]
            c = str((int(c) + delta) % 10)
            return state[:i] + c + state[i + 1:]

        cnt = 0
        q1 = {origin}
        q2 = {target}
        # vis = {origin, target}
        vis = set()
        while q1 and q2:
            tmp = set()
            for state in q1:
                if state in invalid_set:
                    continue
                if state in q2:
                    return cnt
                vis.add(state)
                for i in range(4):
                    for delta in [-1, 1]:
                        child = modify(state, i, delta)
                        # if child not in vis and child not in invalid_set:
                        tmp.add(child)
                        # vis.add(child)
            cnt += 1
            q1 = q2
            q2 = tmp
        return -1
```

### 127. 单词接龙
[127. 单词接龙](https://leetcode-cn.com/problems/word-ladder/)

- 方法一：广度优先搜索 + 优化建图

```python
class Solution:
    def __init__(self):
        self.init()

    def init(self):
        self.word2id_ = {}
        self.edges = collections.defaultdict(set)

    def word2id(self, word):
        if word not in self.word2id_:
            self.word2id_[word] = len(self.word2id_)
        return self.word2id_[word]

    def add_edge(self, word):
        for i in range(len(word)):
            lst = list(word)
            lst[i] = "*"
            target = "".join(lst)
            self.edges[word].add(target)
            self.edges[target].add(word)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.init()
        self.add_edge(beginWord)
        for word in wordList:
            self.add_edge(word)
        if endWord not in self.edges:
            return 0
        queue = list()
        vis = collections.defaultdict(bool)
        dis = collections.defaultdict(int)
        queue.append(beginWord)
        vis[beginWord] = True
        while len(queue) > 0:
            top = queue.pop(0)
            if top == endWord:
                return dis[top] // 2 + 1
            for neighbor in self.edges[top]:
                if not vis[neighbor]:
                    vis[neighbor] = True
                    queue.append(neighbor)
                    dis[neighbor] = dis[top] + 1
        return 0
```

### 126. 单词接龙 II

[126. 单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/)

### 1284. 转化为全零矩阵的最少反转次数
[1284. 转化为全零矩阵的最少反转次数](https://leetcode-cn.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)


# 散列数据结构
## 哈希
### 234. 回文链表
[234. 回文链表](https://leetcode-cn.com/problems/palindrome-linked-list/)

```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # hash = hash * seed + val
        # seed: prime number
        # val: node value
        # hash1 = a0 * seed^(n-1) + a1 * seed^(n-2)
        hash1=hash2=0
        h=1
        seed=3
        p=head
        while p is not None:
            hash1=hash1*seed+p.val
            hash2=hash2+h*p.val
            h*=seed
            p=p.next
        return hash1==hash2
```




## 哈希表
### 1207. 独一无二的出现次数

[1207. 独一无二的出现次数](https://leetcode-cn.com/problems/unique-number-of-occurrences/)

涉及哈希表（HashMap、dict、map）与集合
```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        values = collections.Counter(arr).values()
        return len(set(values)) == len(values)
```

### 381. O(1) 时间插入、删除和获取随机元素 - 允许重复
[381. O(1) 时间插入、删除和获取随机元素 - 允许重复](https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed/)
```python
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vector = []
        self.N = 0
        self.elem2idxs = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        contain = len(self.elem2idxs[val])
        self.elem2idxs[val].add(self.N)
        if len(self.vector) <= self.N:
            self.vector.append(val)
        else:
            self.vector[self.N] = val
        self.N += 1
        return not bool(contain)

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """

        if len(self.elem2idxs[val]):
            idx = self.elem2idxs[val].pop()
            if idx != self.N - 1:
                other = self.vector[self.N - 1]
                self.vector[idx] = other
                self.elem2idxs[other].remove(self.N - 1)
                self.elem2idxs[other].add(idx)
            self.N -= 1
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.vector[:self.N])
```





# 线性数据结构
## 数组

### 48. 旋转图像

[48. 旋转图像](https://leetcode-cn.com/problems/rotate-image/)

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 官方题解的做法是先上下翻转，再按对角线翻转
        # 为了和题解有所不同，我选择先对角线翻转，再左右翻转
        # --主对角线翻转--
        L = len(matrix)
        for i in range(1, L):
            for j in range(i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        # --左右翻转--
        l, r = 0, L - 1
        while l < r:
            for j in range(L):
                tmp = matrix[j][l]
                matrix[j][l] = matrix[j][r]
                matrix[j][r] = tmp
            l += 1
            r -= 1
```
### 830. 较大分组的位置



[830. 较大分组的位置](https://leetcode-cn.com/problems/positions-of-large-groups/)

```python
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        pre=""
        a=b=0
        res=[]
        for i, e in enumerate(s):
            b=i
            if e != pre:
                if b-a>=3:
                    res.append([a,b-1])
                a=i
            pre=e 
        if b-a+1>=3:
            res.append([a,b])
        return res
```

### 189. 旋转数组

[189. 旋转数组](https://leetcode-cn.com/problems/rotate-array/)

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

```
### 228. 汇总区间
[228. 汇总区间](https://leetcode-cn.com/problems/summary-ranges/)

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res=[]
        s=0
        e=0
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1]==1:
                e=i
            else:
                res.append(str(nums[s]) if s==e else f"{nums[s]}->{nums[e]}")
                s=e=i
        res.append(str(nums[s]) if s==e else f"{nums[s]}->{nums[e]}")
        return res
```

## 堆

### 973. 最接近原点的 K 个点

```python
import heapq


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distances = [x * x + y * y for x, y in points]
        heap = []
        for i, dis in enumerate(distances):
            heapq.heappush(heap, (dis, i))
        return [points[heapq.heappop(heap)[1]] for _ in range(K)]
```
[题解值得再学习一下](https://leetcode-cn.com/problems/k-closest-points-to-origin/solution/zui-jie-jin-yuan-dian-de-k-ge-dian-by-leetcode-sol/)


### 767. 重构字符串

[767. 重构字符串](https://leetcode-cn.com/problems/reorganize-string/)

```python
class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return S
        L = len(S)
        counter = collections.Counter(S)
        max_cnt = max(counter.values())
        if max_cnt > (L + 1) // 2:
            return ""
        heap = [(-v, k) for k, v in counter.items()]
        heapq.heapify(heap)
        ret = []
        # while len(ret) < L: # 错误示范
        while len(heap) > 1:  # 保证有两个元素出堆
            _, letter1 = heapq.heappop(heap)
            _, letter2 = heapq.heappop(heap)
            ret += [letter1, letter2]
            counter[letter1] -= 1
            counter[letter2] -= 1
            if counter[letter1] > 0:
                heapq.heappush(heap, (-counter[letter1], letter1))
            if counter[letter2] > 0:
                heapq.heappush(heap, (-counter[letter2], letter2))
        # 考虑只有1个元素的情况
        if heap:
            ret.append(heap[0][1])
        return "".join(ret)
```


### 659. 分割数组为连续子序列
[659. 分割数组为连续子序列](https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/)

要求判断最小的连续序列是否>=3

1. 哈希 + 最小堆

$\mathcal{O}(nlogn)$

建立**最后数**$\rightarrow$**长度列表**映射，并尽可能增加**短序列**的长度
```python
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # 根据【最后一个数】+【长度】可以确定一个序列
        # last2queue：【最后一个数】→【长度】列表
        # 希望尽可能增加最短序列的长度，故“【长度】列表”用最小堆表示
        last2queue = collections.defaultdict(list)
        for x in nums:
            queue = last2queue[x - 1]  # 写错成 x 
            if queue:
                prev_len = heapq.heappop(queue)
                heapq.heappush(last2queue[x], prev_len + 1)
            else:
                heapq.heappush(last2queue[x], 1) # 写错成 queue
        # 忘了写not
        return not any(queue and queue[0] < 3 for queue in last2queue.values())

```
2. 哈希 + 贪心

$\mathcal{O}(n)$

换一个角度思考问题，不再建立**最后数**$\rightarrow$**长度**==列表==，而是**最后数**$\rightarrow$**大于3的序列个数**，在建立这个映射的时候，满足题设`最小的连续序列是否 >= 3`


```python
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
```

有空可以研究一下这个时间$\mathcal{O}(N)$空间$\mathcal{O}(1)$的解法

[【最优贪心解法】O(N) 时间 + O(1) 空间](https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/solution/tan-xin-o1-kong-jian-fu-za-du-de-zui-you-jie-fa-by/)

### 347. 前 K 个高频元素

[347. 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/)

一行代码解千愁

```python
return [num for num, _ in sorted(list(collections.Counter(nums).items()), key=lambda x:-x[1])[:k]]
```

我傻啊，`Counter`明明自带取最多的方法`most_common`

```python
 return [e[0] for e in collections.Counter(nums).most_common(k)]
```
计数后建堆，再出堆$K$次，时间复杂度依然是$\mathcal{O}(NlogN)$，因为建堆的时间复杂度就是这个。

所以建堆方法是这样的（时间复杂度$\mathcal{O}(NlogK)$，因为堆的大小始终$<K$）：

在这里，我们可以利用堆的思想：建立一个`小顶堆`，然后遍历「出现次数数组」：

- 如果堆的元素个数小于 $K$，就可以直接插入堆中。
-  如果堆的元素个数等于 $K$，则检查堆顶与当前出现次数的大小。如果堆顶更大，说明至少有 $K$个数字的出现次数比当前值大，故舍弃当前值；否则，就弹出堆顶，并将当前值插入堆中。

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        heap = []
        for num, cnt in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, num))
            else:
                if heap[0][0] < cnt:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (cnt, num))
        ans = []
        while len(heap):
        	# ans.insert(0, heapq.heappop(heap)[1]) # 大可不必，题目忽略顺序
            ans.append(heapq.heappop(heap)[1])
        return ans
```

### 1046. 最后一块石头的重量
[1046. 最后一块石头的重量](https://leetcode-cn.com/problems/last-stone-weight/)


我写的辣鸡代码：

```python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = -heapq.heappop(stones)
            s2 = 0
            if len(stones):
                s2 = -heapq.heappop(stones)
            s = abs(s1 - s2)
            if s:
                heapq.heappush(stones, -s)
        return -stones[0] if stones else 0
```

简洁代码：

```python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-stone for stone in stones]
        heapq.heapify(h)

        while len(h) > 1:
            a, b = heapq.heappop(h), heapq.heappop(h)
            if a != b:
                heapq.heappush(h, a - b)
        return -h[0] if h else 0
```

## 栈
### 20. 有效的括号
[20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

```python
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for c in s:
            if c in pairs and stack and stack[-1] == pairs[c]:
                stack.pop()
            else:
                stack.append(c)
        return not stack
```

### 32. 最长有效括号

[32. 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/)

保持栈底元素为当前已经遍历过的元素中「最后一个没有被匹配的右括号的下标」

栈里其他元素维护左括号的下标

```java
public class Solution {
    public int longestValidParentheses(String s) {
        int maxans = 0;
        Deque<Integer> stack = new LinkedList<Integer>();
        stack.push(-1);
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.empty()) {
                    stack.push(i);
                } else {
                    maxans = Math.max(maxans, i - stack.peek());
                }
            }
        }
        return maxans;
    }
}
```

## 单调队列
### 239. 滑动窗口最大值
[239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)

- 题解

[labuladong 单调队列解题详解](https://leetcode-cn.com/problems/sliding-window-maximum/solution/dan-diao-dui-lie-by-labuladong/)

[【Python】 简洁的单调队列解法（详解+注释）](https://leetcode-cn.com/problems/sliding-window-maximum/solution/python-jian-ji-de-dan-diao-dui-lie-jie-f-q56i/)

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        N = len(nums)
        res = []
        for i in range(N):
            # 满足单调递减
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()  # 默认右端出栈
            queue.append(i)
            # 删掉左端不在滑动窗口内元素
            if queue[0] <= i - k:
                queue.popleft()
            # 如果窗口已经形成，记录结果
            if i >= k - 1:
                # 结果记录的是最大值，所以需要把索引带入nums (默写出错)
                res.append(nums[queue[0]])
        return res
```


## 单调栈

### 001. 东哥笔记

[一招吃遍力扣四道题，妈妈再也不用担心我被套路啦～](https://leetcode-cn.com/problems/remove-k-digits/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-5/)
[单调栈 Monotonic Stack 的使用 ](https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247484525&idx=1&sn=3d2e63694607fec72455a52d9b15d4e5&chksm=9bd7fa65aca073734df90b45054448e09c14e6e35ad7b778bff62f9bd6c2b4f6e1ca7bc4f844&scene=21#wechat_redirect)
### 402. 移掉K位数字

[402. 移掉K位数字](https://leetcode-cn.com/problems/remove-k-digits/)

首先要理解题意， 求$N-K$个最小的数

思维转变， 把丢弃视为保留

删除`第一个不单调递增`（开始下降， `num[x] < num[x-1]`）

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
            numStack.append(digit)
        # 特殊情况： 单调递增的num
        # [:-k]  等同于删除末尾的k个数字
        finalStack = numStack[:-k] if k else numStack
        # 特殊情况：前导0
        #  or "0" 这步相当妙，默写的时候没默出来
        return "".join(finalStack).lstrip("0") or "0"
```




### 316. 去除重复字母
[316. 去除重复字母](https://leetcode-cn.com/problems/remove-duplicate-letters/)

[1081. 不同字符的最小子序列](https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters/)

如果去掉`counter`的代码， 会造成`使得每个字母只出现一次`的条件失效，即有的字母出现0次
`counter`的作用是在删字母的时候，判断是否会导致有的字母不出现

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020112617240327.png)


```python
class Solution:
    def removeDuplicateLetters(self, s) -> int:
        stack = []
        counter = collections.Counter(s)
        for c in s:
            if c not in stack:
                # stack[-1] > c | 单调递增条件被破坏
                while stack and stack[-1] > c and counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            counter[c] -= 1
        return "".join(stack)
```

>TODO: 理解还不深刻， 继续理解

在上一题中，限值条件是`k`（所以出现在上一题的`while`判断条件中），这一题的限值条件是`使得每个字母只出现一次`，故判断条件是`counter[stack[-1]]`。


`counter` 表示当**前指针及之后**所含元素的计数。如果从栈中弹出了元素，并且这个元素后续没有机会再添加进来了，这一定是非法的。



### 321. 拼接最大数

[321. 拼接最大数](https://leetcode-cn.com/problems/create-maximum-number/)


```python
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick_max(lst, k):
            stack = []
            drop = len(lst) - k  # 没想到
            for e in lst:
                # 没想到
                while drop and stack and stack[-1] < e:
                    stack.pop()
                    drop -= 1  # 没想到
                stack.append(e)
            return stack[:k]  # 没想到截断 (2次)

        def merge(la, lb):
            res = []
            while la or lb:
                # bigger 保证不为空列表
                bigger = la if la > lb else lb
                res.append(bigger.pop(0))  # 简写
                # bigger.pop(0) # 简写
            return res

        ret = []
        for sp in range(k + 1):
	        # 判断条件的 <= 写错为 < 
            if sp <= len(nums1) and k - sp <= len(nums2):
                tmp = merge(
                    pick_max(nums1, sp),
                    pick_max(nums2, k - sp),
                )
                ret = max(ret, tmp)
        return ret
```


### 84. 柱状图中最大的矩形

[84. 柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        N = len(heights)
        left = [0] * N
        right = [N] * N
        stack = []
        for i in range(N):
            while stack and heights[stack[-1]] > heights[i]:
                right[stack.pop()] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        return max(heights[i] * (right[i] - left[i] - 1) for i in range(N))
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201226223439767.png)
### 85. 最大矩形
[85. 最大矩形](https://leetcode-cn.com/problems/maximal-rectangle/)

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        left = [0] * N
        right = [N] * N
        stack = []
        for i in range(N):
            while stack and heights[stack[-1]] > heights[i]:
                right[stack.pop()] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        return max(heights[i] * (right[i] - left[i] - 1) for i in range(N))

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        if not N:
            return 0
        M = len(matrix[0])
        if not M:
            return 0
        heights = [0] * M
        ans = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, self.largestRectangleArea(heights))
        return ans
```

### 496. 下一个更大元素 I

[496. 下一个更大元素 I](https://leetcode-cn.com/problems/next-greater-element-i/)

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = nums2
        mp = {}
        # ---------------------
        stack = []
        L = len(nums)
        ans = [0] * L
        for i in range(L - 1, -1, -1):
            num = nums[i]
            while stack and stack[-1] <= num:
                stack.pop()
            ans[i] = stack[-1] if stack else -1
            stack.append(num)
            # 缓存
            mp[num] = ans[i]
        # -----------------------
        return [mp[x] for x in nums1]
```


### 739. 每日温度
[739. 每日温度](https://leetcode-cn.com/problems/daily-temperatures/)

```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        nums = T
        # -------------------------
        stack = []
        L = len(nums)
        ans = [0] * L
        for i in range(L - 1, -1, -1):
            num = nums[i]
            while stack and nums[stack[-1]] <= num:
                stack.pop()
            ans[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return ans
```

### 503. 下一个更大元素 II

[503. 下一个更大元素 II](https://leetcode-cn.com/problems/next-greater-element-ii/)

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        L = len(nums)
        ans = [0] * L
        for i in range(L * 2 - 1, -1, -1):
            num = nums[i % L]
            while stack and stack[-1] <= num:
                stack.pop()
            ans[i % L] = stack[-1] if stack else -1
            stack.append(num)
        return ans
```

# 排列组合

## 46. 全排列

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        visit = [False] * N
        ans = []
        path = []

        def backtrace(n):
            if n == N:
                ans.append(path[:])
                return
            for i in range(N):
                if not visit[i]:
                    path.append(nums[i])
                    visit[i] = True
                    backtrace(n + 1)
                    visit[i] = False
                    path.pop()

        backtrace(0)
        return ans
```

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)

        def backtrace(t):
            if t == N:
                res.append(nums[:])
            for i in range(t, N):
                nums[i], nums[t] = nums[t], nums[i]
                backtrace(t + 1)
                nums[t], nums[i] = nums[i], nums[t]

        backtrace(0)
        return res
```

# 下一个数字/排列问题

## 738. 单调递增的数字

[738. 单调递增的数字](https://leetcode-cn.com/problems/monotone-increasing-digits/)

```python
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
```

## 31. 下一个排列

[31. 下一个排列](https://leetcode-cn.com/problems/next-permutation/)

[下一个排列算法详解：思路+推导+步骤，看不懂算我输！](https://leetcode-cn.com/problems/next-greater-element-iii/)

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i = N - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            # note 1. 两个判断条件写一行， 减少代码量
            # note 2. 判断条件是前者>=后者
            i -= 1
        # 通过判断避免单调递减的情况
        if i >= 0:
            j = N - 1
            while j >= 0 and nums[i] >= nums[j]:  # 注意判断条件
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        l, r = i + 1, N - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
```

## 556. 下一个更大元素 III
[556. 下一个更大元素 III](https://leetcode-cn.com/problems/next-greater-element-iii/)

- 套` 31. 下一个排列`代码的解法

```python
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

```

---

>TODO: 单调栈解法

---

[C++ 排列解法](https://leetcode-cn.com/problems/next-greater-element-iii/solution/c-pai-lie-jie-fa-by-vclip/)
把输入数字转化为字符串，找出这个字符串的下一个排列即可。注意可能超出`int32`的数值范围，这时stoi函数会抛出异常，捕获然后返回`-1`即可。

```cpp
class Solution {
public:
    int nextGreaterElement(int n) {
        try {
            string s = to_string(n);
            return next_permutation(s.begin(), s.end()) ? stoi(s) : -1;
        } catch (exception const&) {
            return -1;
        }
    }
};
```



# 区间覆盖/合并

## 001. 东哥笔记

[一文秒杀所有区间相关问题 ](https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247487316&idx=1&sn=95cfbbd24f1cb5d8c07c71c2ba15246a&chksm=9bd7f15caca0784ab7bce7f36a6eb9118de2a573515a99948168ed93b25069a3b7bf85cf50a5&mpshare=1&scene=1&srcid=0105AJe4ZiPxyK1Sfnrr0sX5&sharer_sharetime=1609816194104&sharer_shareid=2416ed716504a127c7b5e1cea7556258&key=d0a771e0ab3b3c3d1493b718906a5a9e77e8b730b111f12127065d2dc68b540d33fc7307099e6b2364a1426148ad71173faef6370fcfdcb24603885720d888a84bed90c21a28645818dddb1eaf01c2519a0658ee928fa0ab80c34ac60f1373f3d4e2ece0f00792b10314b61684da72224c8ab4fc803418aae14422a50ac72200&ascene=1&uin=MTAxODExNDk3OQ%3D%3D&devicetype=Windows+XP&version=62060841&lang=zh_CN&exportkey=A%2BTUann7bw%2FpdTCzNi6BKIk%3D&pass_ticket=IW9RAWep7qMHZz0vr5BIvdvswW3Z88Y83kgcZyg%2BLGw6OLDug74Z7Wh7eZLXkzrU&wx_header=0)

## 1288. 删除被覆盖区间
[1288. 删除被覆盖区间](https://leetcode-cn.com/problems/remove-covered-intervals/)


典型的区间覆盖问题

```python

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        left = intervals[0][0]
        right = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            itv = intervals[i]
            # 1. 找到覆盖区间
            if left <= itv[0] and right >= itv[1]:
                res += 1
            # 2. 找到相交区间，合并
            if right >= itv[0] and right <= itv[1]:
                right = itv[1]
            # 3. 完全不想交，更新起始点
            if right < itv[0]:
                left = itv[0]
                right = itv[1]
        return len(intervals) - res
```

## 56. 合并区间
[56. 合并区间](https://leetcode-cn.com/problems/merge-intervals/)

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for itv in intervals:
            if res and itv[0] < res[-1][1]:
                res[-1][1] = max(res[-1][1], itv[1])
            else:
                res.append(itv)
        return res
```




## 57. 插入区间
[57. 插入区间](https://leetcode-cn.com/problems/insert-interval/)

分为`3`个阶段：

1. 列表右 $<$ 插入左
2. 列表左 $\le$ 插入右
3. 干就完了

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = newInterval
        i = 0
        N = len(intervals)
        res = []
        while i < N and intervals[i][1] < l:
            res.append(intervals[i])
            i += 1
        while i < N and intervals[i][0] <= r:
            l = min(intervals[i][0], l)
            r = max(intervals[i][1], r)
            i += 1
        res.append([l, r])
        res += intervals[i:]
        return res
```

---


## 986. 区间列表的交集

[986. 区间列表的交集](https://leetcode-cn.com/problems/interval-list-intersections/)

四种情况:

<img src="https://img-blog.csdnimg.cn/img_convert/303a2465ffa847370bf6887bd0bbd3b1.png" width=300></img>



```python
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]
            if a1 <= b2 and a2 >= b1:
                res.append([max(a1, b1), min(a2, b2)])
            if b2 > a2:
                i += 1
            else:
                j += 1
        return res
```


---
合并区间类的题目套路一样, 都是贪心思想, 先排序, 然后遍历检查是否满足合并区间的条件

## 452. 用最少数量的箭引爆气球

[452. 用最少数量的箭引爆气球](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/)

---

[按照右端点排序，然后如果左端点超过，++](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/solution/yong-zui-shao-shu-liang-de-jian-yin-bao-qi-qiu-1-2/)

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        # 最靠左的右边点
        pos = points[0][1]
        cnt = 1
        for point in points:
            # 这个点左边比【最靠左的右边点】还大
            if point[0] > pos:
                pos = point[1]
                cnt += 1
        return cnt
```

---

[更可解释的方法](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/solution/he-bing-qu-jian-lei-de-ti-mu-du-shi-yi-ge-tao-lu-a/)

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[0])
        rng = points[0]
        cnt = 1
        for point in points[1:]:
            if rng[1] < point[0]:
                cnt += 1
                rng = point
            else:
                rng = max(rng[0], point[0]), min(rng[1], point[1])
        return cnt
```

## 435. 无重叠区间

[435. 无重叠区间](https://leetcode-cn.com/problems/non-overlapping-intervals/)

**动态规划**，时间复杂度$O(N^2)$

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        f = [1]  # 以 i 结尾的区间序列的最大值
        N = len(intervals)
        for i in range(1, N):
            f.append(
                max(
                    (f[j] for j in range(i)
                     if intervals[j][1] <= intervals[i][0]),
                    default=0)
                + 1)
        return N - max(f)
```

注意到方法一本质上是一个「最长上升子序列」问题，因此我们可以将时间复杂度优化至 $O(n \log n)$，具体可以参考[「300. 最长递增子序列的官方题解」](https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/)

---



**排序+贪心**，时间复杂度$O(N\log N)$

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        right = intervals[0][1]
        N = len(intervals)
        cnt = 1
        for i in range(1, N):
            if intervals[i][0] >= right:
                cnt += 1
                right = intervals[i][1]
        return N - cnt
```

求解[452. 用最少数量的箭引爆气球](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/)也是异曲同工之妙

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        intervals = points
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        right = intervals[0][1]
        N = len(intervals)
        cnt = 1
        for i in range(1, N):
            if intervals[i][0] > right:
                cnt += 1
                right = intervals[i][1]
        return cnt
```





# nSum问题

## 1. 两数之和

[1. 两数之和](https://leetcode-cn.com/problems/two-sum/)

第一遍写的方法

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2ix = {}
        for i, num in enumerate(nums):
            num2ix[num] = i
        for i, num in enumerate(nums):
            other = target - num
            if other in num2ix and  i != num2ix[other]:
                return [i, num2ix[other]]
        raise ValueError
```



看题解后写的方法

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2ix = {}
        for i, num in enumerate(nums):
            other = target - num
            if other in num2ix:
                return [i, num2ix[other]]
            num2ix[num] = i
        raise ValueError
```

泛化版本，为后面的nSum函数做准备





## 170. 两数之和 III - 数据结构设计

[170. 两数之和 III - 数据结构设计](https://blog.csdn.net/qq_22017379/article/details/103921516)


## 167. 两数之和 II - 输入有序数组

[167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)

看二分

## 15. 三数之和
[15. 三数之和](https://leetcode-cn.com/problems/3sum/)


```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        ans = []
        for p1 in range(N - 2):
            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue
            # p3 的定义要放在循环外面， 否则会超时
            p3 = N - 1  
            target = -nums[p1]
            for p2 in range(p1 + 1, N):
                if p2 > p1 + 1 and nums[p2] == nums[p2 - 1]:
                    continue
                while p2 < p3 and nums[p2] + nums[p3] > target:
                    p3 -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if p2 == p3:
                    break
                if nums[p2] + nums[p3] == target:
                    ans.append([nums[p1], nums[p2], nums[p3]])
        return ans
```
为什么p3要放在外面呢？放里面当然可以，就是会超时，放外面为什么能保证运行正确呢？

p3左移，整体会变小，p2右移，整体会变大。`nums[p2] + nums[p3] > target`不满足时，整体已经<=target

或者换而言之， p2 p3的遍历本质上就是一个双指针的循环，即在有序数组中遍历两个相加为0的数。


- 用东哥方法写的

```python
class Solution:
    def twoSum(self, nums: List[int], start, target) -> List[List[int]]:
        if start >= len(nums):
            return []
        lo = start
        hi = len(nums) - 1
        res = []
        while lo < hi:
            left, right = nums[lo], nums[hi]
            if left + right > target:
                hi -= 1
            elif left + right < target:
                lo += 1
            else:
                res.append([nums[lo], nums[hi]])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums) - 2:
            arrs = self.twoSum(nums, i + 1, -nums[i])
            for arr in arrs:
                arr.append(nums[i])
                res.append(arr)
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res

```


## 18. 四数之和

[18. 四数之和](https://leetcode-cn.com/problems/4sum/)

复现`nSum`函数

可是说是相当复杂

```python
def nSum(nums: list, n: int, start: int, target: int):
    sz = len(nums)
    res = []
    if n < 2 or sz < n:
        return res
    if n == 2:
        lo = start
        hi = sz - 1
        while lo < hi:
            sum = nums[lo] + nums[hi]
            left, right = nums[lo], nums[hi]
            if sum < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif sum > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
    else:
        i = start
        while i < sz:
            arr_list = nSum(nums, n - 1, i + 1, target - nums[i])
            for arr in arr_list:
                arr.append(nums[i])
                res.append(arr)
            while i < sz - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
    return res
```




## 454. 四数相加 II
[454. 四数相加 II](https://leetcode-cn.com/problems/4sum-ii/)
```python
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        counter = collections.Counter(u + v for u in A for v in B)
        res = 0
        for u in C:
            for v in D:
                tmp = -(u + v)
                if tmp in counter:
                    res += counter[tmp]
        return res
```

# 股票买卖问题

## 01. 东哥笔记

```python
base case：
dp[-1][k][0] = dp[i][0][0] = 0
dp[-1][k][1] = dp[i][0][1] = -infinity
状态转移⽅程：
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
```

## 121. 买卖股票的最佳时机
[121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)


```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = inf
        max_reward = -inf
        for price in prices:
            min_price=min(price,min_price)
            max_reward=max(price-min_price,max_reward)
        return max_reward
```

- labuladong (k=1)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        dp = [[0] * 2 for _ in range(N)]
        for i in range(N):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])  # k=0 时，dp=0
        return dp[N-1][0]
```

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        dp_i_0 = 0
        dp_i_1 = -inf
        for i in range(N):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0
```



## 122. 买卖股票的最佳时机 II
[122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        res = 0
        for i in range(1, N):
            res += max(0, prices[i] - prices[i - 1])
        return res
```
- labuladong (k=$\infin$)

认为`k`和`k-1`是一样的
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        dp_i_0 = 0
        dp_i_1 = -inf
        for i in range(N):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0
```

## 309. 最佳买卖股票时机含冷冻期
[309. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        dp_i_0 = 0
        dp_pi_0 = 0
        dp_i_1 = -inf
        # 条件： 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
        for i in range(N):
            # 卖 1 -> 0
            #dp_pi_0 = dp_i_0 # 错误写法
            tmp = dp_i_0 
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            # 买 0 -> 1
            dp_i_1 = max(dp_i_1, dp_pi_0 - prices[i])
            dp_pi_0 = tmp
        return dp_i_0
```

如果状压怕写错，可以写DP数组版本的：

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        dp = [[0] * 2 for _ in range(N)]
        for i in range(N):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i]) 
        return dp[N-1][0]

        dp = [[0] * 2 for _ in range(N)]
        for i in range(N):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i]) 
        return dp[N-1][0]
```
DP数组， 增加一个初始状态，少写`i==0`的判断条件

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        dp = [[0] * 2 for _ in range(N+1)]
        dp[0][1]=-inf
        for i in range(1,N+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i-1]) 
        return dp[N][0]
```

## 714. 买卖股票的最佳时机含手续费
[714. 买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

实测`- fee`的操作放在买和卖 都可以

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        N = len(prices)
        dp_i_0 = 0
        dp_i_1 = -inf
        for i in range(N):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee)
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0
```

## 123. 买卖股票的最佳时机 III

[123. 买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        K = 2
        dp = [[[0] * 2 for _ in range(K+1)] for _ in range(N+1)]
        # dp[0][..][1]=-inf
        for k in range(K+1):
            dp[0][k][1]=-inf
        # dp[..][0][1]=-inf
        for i in range(N+1):
            dp[i][0][1]=-inf
        for i in range(1, N+1):
            for k in range(2, 0, -1):
                # 卖
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i-1])
                # 买
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i-1]) 
        return dp[N][2][0]
```

## 188. 买卖股票的最佳时机 IV
[188. 买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)

时间复杂度：$O(NK)$

```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        N = len(prices)
        # 直接将上一题的解法参数化拿过来就行了
        K = k
        dp = [[[0] * 2 for _ in range(K+1)] for _ in range(N+1)]
        # dp[0][..][1]=-inf
        for k in range(K+1):
            dp[0][k][1]=-inf
        # dp[..][0][1]=-inf
        for i in range(N+1):
            dp[i][0][1]=-inf
        for i in range(1, N+1):
            for k in range(K, 0, -1):
                # 卖
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i-1])
                # 买
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i-1]) 
        return dp[N][K][0]
```
>TODO: 状态压缩， 将空间复杂度从$O(NK)$降到$O(K)$
>TODO: 看懂这个骚操作

```java
class Solution {
    public int maxProfit(int k, int[] prices) {
        /**
        当k大于等于数组长度一半时, 问题退化为贪心问题此时采用 买卖股票的最佳时机 II
        的贪心方法解决可以大幅提升时间性能, 对于其他的k, 可以采用 买卖股票的最佳时机 III
        的方法来解决, 在III中定义了两次买入和卖出时最大收益的变量, 在这里就是k租这样的
        变量, 即问题IV是对问题III的推广, t[i][0]和t[i][1]分别表示第i比交易买入和卖出时
        各自的最大收益
        **/
        if(k < 1) return 0;
        if(k >= prices.length/2) return greedy(prices);
        int[][] t = new int[k][2];
        for(int i = 0; i < k; ++i)
            t[i][0] = Integer.MIN_VALUE;
        for(int p : prices) {
            t[0][0] = Math.max(t[0][0], -p);
            t[0][1] = Math.max(t[0][1], t[0][0] + p);
            for(int i = 1; i < k; ++i) {
                t[i][0] = Math.max(t[i][0], t[i-1][1] - p);
                t[i][1] = Math.max(t[i][1], t[i][0] + p);
            }
        }
        return t[k-1][1];
    }
    
    private int greedy(int[] prices) {
        int max = 0;
        for(int i = 1; i < prices.length; ++i) {
            if(prices[i] > prices[i-1])
                max += prices[i] - prices[i-1];
        }
        return max;
    }
}
```


# 正向逆向结合
## 32. 最长有效括号
[32. 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/)

```java
class Solution {
    public int longestValidParentheses(String s) {
        int left = 0, right = 0, maxlength = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxlength = Math.max(maxlength, 2 * right);
            } else if (right > left) {
                left = right = 0;
            }
        }
        left = right = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '(') {
                left++;
            } else {
                right++;
            }
            if (left == right) {
                maxlength = Math.max(maxlength, 2 * left);
            } else if (left > right) {
                left = right = 0;
            }
        }
        return maxlength;
    }
}
```

## 152. 乘积最大子数组
[152. 乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/)

[python5行：不同于回溯、DP的tricks解法](https://leetcode-cn.com/problems/maximum-product-subarray/solution/python5xing-bu-tong-yu-hui-su-dpde-tricksjie-fa-by/)

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= (nums[i - 1] or 1)
            r_nums[i] *= (r_nums[i - 1] or 1)
        return max(max(nums), max(r_nums))
```


## 238. 除自身以外数组的乘积

[238. 除自身以外数组的乘积](https://leetcode-cn.com/problems/product-of-array-except-self/)

[除自身以外数组的乘积 - 题解](https://leetcode-cn.com/problems/product-of-array-except-self/solution/chu-zi-shen-yi-wai-shu-zu-de-cheng-ji-by-leetcode-/)

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right, ret = [[0] * n for _ in range(3)]
        left[0] = 1
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        for i in range(n):
            ret[i] = left[i] * right[i]
        return ret
```



# 树数据结构

## 并查集
### 001. 并查集定义

```python
class UnionSet():
    def __init__(self, n):
        self.cnt = n
        self.parent = [0] * n
        for i in range(n):
            self.parent[i] = i

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        self.parent[pa] = pb
        self.cnt -= 1

    def find(self, x) -> int:
        if x == self.parent[x]:
            return x
        # 找到根节点
        r = x
        while r != self.parent[r]:
            r = self.parent[r]
        # 路径压缩
        while x != self.parent[x]:
            t = self.parent[x]
            self.parent[x] = r
            x = t
        return r
```



另一种路径压缩的写法，代码更少，速度更快

```python
    def find(self, x) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
```

还有一种递归的写法，比上一个写法要慢点，但是容易理解：

```python
 def find(self, x) -> int:
     if self.parent[x] != x:
         self.parent[x] = self.find(self.parent[x])
     return self.parent[x]
```


- 并查集题库

「力扣」第 547 题：省份数量（中等）；
「力扣」第 684 题：冗余连接（中等）；
「力扣」第 1319 题：连通网络的操作次数（中等）；
「力扣」第 1631 题：最小体力消耗路径（中等）；
「力扣」第 959 题：由斜杠划分区域（中等）；
「力扣」第 1202 题：交换字符串中的元素（中等）；
「力扣」第 947 题：移除最多的同行或同列石头（中等）；
「力扣」第 721 题：账户合并（中等）；
「力扣」第 803 题：打砖块（困难）；
「力扣」第 1579 题：保证图可完全遍历（困难）;
「力扣」第 778 题：水位上升的泳池中游泳（困难）。


### 547. 省份数量

[547. 省份数量](https://leetcode-cn.com/problems/number-of-provinces/)

```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        class UnionSet():
            ...
        
        N = len(isConnected)
        union_set = UnionSet(N)
        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j]:
                    union_set.union(i, j)
        return union_set.cnt

```

### 1202. 交换字符串中的元素

[1202. 交换字符串中的元素](https://leetcode-cn.com/problems/smallest-string-with-swaps/)


```python
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UnionSet():
		 	...

        N = len(s)
        union_set = UnionSet(N)
        for pair in pairs:
            union_set.union(*pair)
        id2heap = collections.defaultdict(list)
        for i in range(N):
            heap = id2heap[union_set.find(i)]
            heapq.heappush(heap, (s[i], i))
        ans = ""
        for i in range(N):
            heap = id2heap[union_set.find(i)]
            ch, _ = heapq.heappop(heap)
            ans += ch
        return ans
```

### 399. 除法求值
[399. 除法求值](https://leetcode-cn.com/problems/evaluate-division/)

- 并查集解法

```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        class UnionSet():
            def __init__(self, n):
                self.cnt = n
                self.parent = [0] * n
                self.weight = [1] * n
                for i in range(n):
                    self.parent[i] = i

            def union(self, a, b, w):
                pa = self.find(a)
                pb = self.find(b)
                if pa == pb:
                    return
                self.parent[pa] = pb
                self.weight[pa] = w * self.weight[b] / self.weight[a]
                self.cnt -= 1

            def find(self, x) -> int:
                if x != self.parent[x]:
                    px = self.parent[x]
                    self.parent[x] = self.find(self.parent[x])
                    self.weight[x] *= self.weight[px]
                return self.parent[x]

            def query(self, a, b):
                if self.find(a) == self.find(b):
                    return self.weight[a] / self.weight[b]
                return -1

        N = len(equations)
        sym2idx = {}
        union_set = UnionSet(2 * N)
        for equation, value in zip(equations, values):
            for symbol in equation:
                if symbol not in sym2idx:
                    sym2idx[symbol] = len(sym2idx)
            union_set.union(sym2idx[equation[0]], sym2idx[equation[1]], value)
        results = []
        for query in queries:
            if query[0] not in sym2idx or query[1] not in sym2idx:
                result = -1
            else:
                result = union_set.query(sym2idx[query[0]], sym2idx[query[1]])
            results.append(result)
        return results
```

- BFS解法

```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        sym2idx = {}
        for equation, value in zip(equations, values):
            for symbol in equation:
                if symbol not in sym2idx:
                    sym2idx[symbol] = len(sym2idx)
            graph[sym2idx[equation[0]]].append([sym2idx[equation[1]], value])
            graph[sym2idx[equation[1]]].append([sym2idx[equation[0]], 1 / value])
        results = []
        for query in queries:
            a, b = query
            if a not in sym2idx or b not in sym2idx:
                result = -1
            else:
                result = -1
                queue = collections.deque()
                vis = collections.defaultdict(bool)
                vis[sym2idx[a]] = True
                queue.append([sym2idx[a], 1])
                while queue:
                    top, top_w = queue.popleft()
                    if top == sym2idx[b]:
                        result = top_w
                    for idx, w in graph[top]:
                        if not vis[idx]:
                            queue.append([idx, w * top_w])
                            vis[idx] = True
            results.append(result)
        return results
```

# 双指针
## 11. 盛最多水的容器

[11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        ret = 0
        while left < right:
            lh = height[left]
            rh = height[right]
            ret = max(
                (right - left) * min(lh, rh), 
                ret
            )
            if lh < rh:
                left += 1
            else:
                right -= 1
        return ret
```

[O(n) 双指针解法：理解正确性、图解原理](https://leetcode-cn.com/problems/container-with-most-water/solution/on-shuang-zhi-zhen-jie-fa-li-jie-zheng-que-xing-tu/)


    167. 两数之和 II - 输入有序数组
    240. 搜索二维矩阵 II




## 977. 有序数组的平方
[977. 有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array/)
baseline

```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([x**2 for x in A])
```

双指针

```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        N = len(A)
        start = 0
        end = N - 1
        res = [0] * N
        for i in range(N - 1, -1, -1):
            sp = A[start] ** 2
            ep = A[end] ** 2
            if sp > ep:
                res[i] = sp
                start += 1
            else:
                res[i] = ep
                end -= 1
        return res
```

- 方法二：双向广度优先搜索

## 283. 移动零
[283. 移动零](https://leetcode-cn.com/problems/move-zeroes/)

>TODO: 自己重新刷一遍

伪代码
```python
left=right=0
for i in range:
    if nums[right]==0:
        right 右移
    else:
        交换 left right
        left right 同时右移 
```
`left`, `right`同时维护`0`区间的左右指针


考虑到更简洁的条件判断， 故应该为下面的形式：
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
```

## 88. 合并两个有序数组

[88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)


```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]
```

# 滑动窗口

## 001. 东哥笔记

滑动窗口题目:

[3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

[30. 串联所有单词的子串](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/)

[76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)

[159. 至多包含两个不同字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/)

[209. 长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum/)

[239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)

[567. 字符串的排列](https://leetcode-cn.com/problems/permutation-in-string/)

[632. 最小区间](https://leetcode-cn.com/problems/smallest-range/)

[727. 最小窗口子序列](https://leetcode-cn.com/problems/minimum-window-subsequence/)



## 3. 无重复字符的最长子串

[3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

根据一个我能看懂题解的默写：

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
	    if not s:return 0 # 默写后看了原题解加上
        left = 0
        cur_len = 0
        max_len = 0
        N = len(s)
        lookup = set()
        for i in range(N):
            while s[i] in lookup:
                lookup.remove(s[left]) # 容易写错的一个地方，滑动窗口滑动的本质
                left += 1
                cur_len -= 1
            lookup.add(s[i])
            cur_len += 1 # 相比于原题解放到了后面，无影响
            max_len = max(max_len, cur_len) # 相比原题解更容易读
        return max_len
```

## 76. 最小覆盖子串

[76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)

- labuladong

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        window = collections.defaultdict(int)
        valid = 0
        l, r = 0, 0
        a, b = -1, len(s)
        while r < len(s):
            c = s[r]
            r += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while l < r and valid == len(need):
                if  r - l < b - a:
                    a, b = l, r
                c = s[l]
                l += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return "" if a == -1 else s[a:b]
```


## 159. 至多包含两个不同字符的最长子串
[159. 至多包含两个不同字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/)

[340. 至多包含 K 个不同字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters/)

>给定一个字符串 s ，找出 至多 包含两个不同字符的最长子串 t 。

>示例 1:
输入: "eceba"
输出: 3
解释: t 是 "ece"，长度为3。

> 示例 2:
输入: "ccaabbb"
输出: 5
解释: t 是 "aabbb"，长度为5。

题解

```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if lookup[s[end]] == 0:
                counter += 1
            lookup[s[end]] += 1
            end +=1
            while counter > 2:
                if lookup[s[start]] == 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len
```

默写

```python
import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        lookup = collections.defaultdict(int)
        cnt = 0
        start = 0
        res = (0, 0)

        for end, c in enumerate(s):
            if lookup[c] == 0:
                cnt += 1
            lookup[c] += 1
            while cnt > 2:
                lookup[s[start]] -= 1
                if lookup[s[start]] == 0:
                    cnt -= 1
                start += 1
            if end - start > res[1] - res[0]:
                res = (start, end)
        return res[1] - res[0] + 1


print(Solution().lengthOfLongestSubstringTwoDistinct("eceba"))
print(Solution().lengthOfLongestSubstringTwoDistinct("ccaabbb"))

```

没钱充会员


##  567. 字符串的排列
[567. 字符串的排列](https://leetcode-cn.com/problems/permutation-in-string/)

- 暴力 

时间复杂度$O(NK)$

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L1 = len(s1)
        L2 = len(s2)
        counter = collections.Counter(s1)
        if L1 > L2:
            return False
        for i in range(L2 - L1 + 1):
            sub = s2[i:i + L1]
            if collections.Counter(sub) == counter:
                return True
        return False
```

- 滑动窗口

时间复杂度$O(N)$

```python
class Solution(object):
    def checkInclusion(self, s1, s2):
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        l, r = 0, 0
        valid = 0  # 满足need的key数量
        need.update(collections.Counter(s1))
        while r < len(s2):
            c = s2[r]
            r += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            if r - l == len(s1):
                if valid == len(need):
                    return True
                c = s2[l]
                l += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return False
```

## 438. 找到字符串中所有字母异位词

[438. 找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)

默写了一遍滑动窗口

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        need.update(collections.Counter(p))
        res = []
        valid = 0
        l, r = 0, 0
        while r < len(s):
            c = s[r]
            r += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            if r - l == len(p):
                if valid == len(need):
                    res.append(l)
                c = s[l]
                l += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return res
```


# 动态规划
## 5. 最长回文子串

[5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)

如图所示， **中心扩散法**更快

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201202170251998.png)



- 动态规划

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        ret = ""
        # l 为 子串长度 - 1
        for l in range(N):
            for i in range(N - l):
                j = i + l
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j] and l + 1 > len(ret):
                    ret = s[i:j + 1]
        return ret
```

- 中心扩散法

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)

        def expand_aroud_center(l, r):
            while l >= 0 and r < N and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        start, end = 0, 0
        for i in range(N):
            l1, r1 = expand_aroud_center(i, i)
            l2, r2 = expand_aroud_center(i, i + 1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start:end + 1]
```

## 10. 正则表达式匹配

[10. 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/)

$f[i][j]=\left\{\begin{array}{ll}\text { if }\left(p[j] \neq^{‘*’}\right)=\left\{\begin{array}{ll}f[i-1][j-1], & \operatorname{matches}(s[i], p[j]) \\ \text { false, } & \text { otherwise }\end{array}\right. \\ \text { otherwise }=\left\{\begin{array}{l}f[i-1][j] \text { or } f[i][j-2], \quad \text { matches }(s[i], p[j-1]) \\ f[i][j-2], & \text { otherwise }\end{array}\right.\end{array}\right.$

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201210132754170.png)

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # 只想到通过 s p 最前面加字符的方法， 没想到设置match函数更方便
        def match(i, j):
            if i == 0 or j == 0:
                return False
            if p[j - 1] == ".":
                return True
            return s[i - 1] == p[j - 1]

        for i in range(m + 1):
            # s 可以是空串， p 必须有值。如 "" 匹配 "b*"
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    if match(i, j - 1):
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
                else:
                    if match(i, j):
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = False
        return dp[m][n]
```

## 32. 最长有效括号

[32. 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/)

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        for i, c in enumerate(s):
            pre_ix = i - dp[i - 1] - 1
            if c == ")" and pre_ix >= 0 and s[pre_ix] == "(":
                dp[i] = dp[i - 1] + 2
                if pre_ix - 1 >= 0:
                    dp[i] += dp[pre_ix - 1]
        return max(dp)
```

> TODO: 学习另外两个题解




## 70. 爬楼梯
[70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 1:
            return 1
        dp = [1] * n
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
```
## 53. 最大子序和
[53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, N):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            res = max(res, dp[i])
        return res
```
## 300. 最长上升子序列
[300. 最长上升子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)

$\mathcal O(n^2)$方法

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if not N:
            return 0
        dp = [1] * N
        res = 1
        for i in range(1, N):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    res = max(res, dp[i])
        return res
```
$\mathcal O(nlogn)$方法

## 139. 单词拆分

[139. 单词拆分](https://leetcode-cn.com/problems/word-break/)

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [0 for i in range(N + 1)]
        dp[0] = 1
        wordDict = set(wordDict)
        for i in range(0, N + 1):
            if dp[i]:
                for j in range(i + 1, N + 1):
                    if s[i:j] in wordDict:
                        dp[j] = 1
        return bool(dp[N])
```
## 140. 单词拆分 II
[140. 单词拆分 II](https://leetcode-cn.com/problems/word-break-ii/)
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        dp = [0 for _ in range(N + 1)]
        pres = [[] for _ in range(N + 1)]
        dp[0] = 1
        wordDict = set(wordDict)
        for i in range(0, N + 1):
            if dp[i]:
                for j in range(i + 1, N + 1):
                    if s[i:j] in wordDict:
                        dp[j] = 1
                        pres[j].append(i)
        results: List[str] = []

        def recursion(ix, result):
            if ix == 0:
                results.append(" ".join(result))
            for pre in pres[ix]:
                recursion(pre, [s[pre:ix]] + result)

        recursion(N, [])

        if len(results) == 1 and results[0] == "":
            return []
        return results
```

```python
list(zip(range(len(dp)),s+"_", dp, pres))
Out[2]: 
[(0, 'c', 1, []),
 (1, 'a', 0, []),
 (2, 't', 0, []),
 (3, 's', 1, [0]),
 (4, 'a', 1, [0]),
 (5, 'n', 0, []),
 (6, 'd', 0, []),
 (7, 'd', 1, [3, 4]),
 (8, 'o', 0, []),
 (9, 'g', 0, []),
 (10, '_', 1, [7])]
```

## 72. 编辑距离

[72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(1, M + 1):
            dp[0][i] = i
        for i in range(1, N + 1):
            dp[i][0] = i
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                left = dp[i - 1][j] + 1
                down = dp[i][j - 1] + 1
                left_down = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                dp[i][j] = min(left, down, left_down)
        return dp[N][M]
```

## 514. 自由之路
[514. 自由之路](https://leetcode-cn.com/problems/freedom-trail/)

```python
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # ring: godding | j | n
        # key: gd       | i | m
        # 定义 dp[i][j] 表示从前往后拼写出 key 的第 i 个字符， ring 的第 j 个字符 的最小步数
        # 维护一个位置数组 pos[c] ，表示 字符c 在 ring 中出现的位置集合
        #

        fn = lambda x: ord(x) - 97
        n = len(ring)
        m = len(key)
        pos = [[] for _ in range(26)]
        for i in range(n):
            pos[fn(ring[i])].append(i)
        dp = [[inf for _ in range(n)] for _ in range(m)]
        # 对于 key 0， 直接旋转
        for i in pos[fn(key[0])]:
            dp[0][i] = min(i, n - i) + 1  # + 1 是为了按button
        for i in range(1, m):  # 遍历key
            for j in pos[fn(key[i])]:  # key[i] 在 ring 中所有出现过的位置 j
                for k in pos[fn(key[i - 1])]:  # key[i-1] 在 ring 中所有出现过的位置 k
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - 1][k] + min(  # 从上一次的状态（多个）转到当前状态（多个）的最小值
                            abs(j - k),
                            n - abs(j - k) 
                        ) + 1  # 记得 + 1
                    )
        return min(*dp[m - 1])
```

## 62. 不同路径
[62. 不同路径](https://leetcode-cn.com/problems/unique-paths/)

```cpp
class Solution {
public:
    int dp[200][200] = {0};

    int uniquePaths(int m, int n) {
        dp[0][1] = 1;
        for (int i = 1; i < m + 1; ++i) {
            for (int j = 1; j < n + 1; ++j) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m][n];
    }
};

```

## 746. 使用最小花费爬楼梯
[746. 使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs/)

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        L = len(cost)
        dp = [0] * (L + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        cost.append(0)
        for i in range(2, L + 1):
            dp[i] = min(dp[i - 1], dp[i - 2])+cost[i]
        return dp[L]
```

虽然能通过，但是感觉写得有问题，官方题解：

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]
```

## 714. 买卖股票的最佳时机含手续费

[714. 买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

无状态压缩的$O(N)$空间复杂度

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        L = len(prices)
        dp = [[0] * 2 for _ in range(L)]
        dp[0][1] = -prices[0]  # 初始状态写错。1 表示拥有，买
        for i in range(1, L):
            # 卖
            dp[i][0] = max(
                dp[i - 1][0],
                dp[i - 1][1] + prices[i] - fee
            )
            # 买
            dp[i][1] = max(
                dp[i - 1][1],
                dp[i - 1][0] - prices[i]
            )
        return dp[L - 1][0]
```
状态压缩的$O(1)$空间复杂度
```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        L = len(prices)
        # 仔细观察，当前状态只依赖于上一个状态，
        # 类似于随机过程的马尔科夫性。所以可以进行状态压缩
        sell, buy = 0, -prices[0]  # 初始状态写错。1 表示拥有，买
        for i in range(1, L):
            sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
        return sell
```

贪心法

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 贪心法与DP不同，在开始交易时就考虑手续费fee
        L = len(prices)
        buy = prices[0] + fee
        profit = 0
        for i in range(1, L):
            if prices[i] + fee < buy:
                buy = prices[i] + fee # 重新买
            elif prices[i] > buy:
                profit += prices[i] - buy # 增量卖
                buy = prices[i]
        return profit
```

## 322. 零钱兑换
[322. 零钱兑换](https://leetcode-cn.com/problems/coin-change/)

[记忆化回溯 + 动态规划，逐行解释 （Python 3）](https://leetcode-cn.com/problems/coin-change/solution/ji-yi-hua-hui-su-dong-tai-gui-hua-zhu-xing-jie-shi/)

- 记忆化搜索
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}
        def helper(amount):
            if amount in memo:
                return memo[amount]
            res = inf
            for coin in coins:
                if amount >= coin:
                    res = min(res, helper(amount - coin) + 1)
            memo[amount] = res # 忘了加记忆化的一步
            return res
        res = helper(amount)
        if res == inf:
            return -1
        return res
```

- DP数组
- 贪心+DFS

## 509. 斐波那契数

[509. 斐波那契数](https://leetcode-cn.com/problems/fibonacci-number/)

暴力递归的时间复杂度是$O(2^N)$

- DP

时间复杂度 $O(N)$

```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n in (1, 2):
            return 1
        prev = 1
        curr = 1
        for i in range(3, n + 1):
            sum_ = prev + curr
            prev = curr
            curr = sum_
        return curr
```


- 矩阵快速幂

时间复杂度 $O(\log N)$

空间复杂度 $O(1)$

首先我们可以构建这样一个递推关系：

$$\left[\begin{array}{cc}1 & 1 \\ 1 & 0\end{array}\right]\left[\begin{array}{c}F(n) \\ F(n-1)\end{array}\right]=\left[\begin{array}{c}F(n)+F(n-1) \\ F(n)\end{array}\right]=\left[\begin{array}{c}F(n+1) \\ F(n)\end{array}\right]$$

因此：

$$\left[\begin{array}{c}F(n+1) \\ F(n)\end{array}\right]=\left[\begin{array}{ll}1 & 1 \\ 1 & 0\end{array}\right]^{n}\left[\begin{array}{l}F(1) \\ F(0)\end{array}\right]$$

用快速幂算法来加速这里 $M^n$ 的求取

```python
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        q = [[1, 1], [1, 0]]
        res = self.matrix_pow(q, n - 1)
        return res[0][0]
    
    def matrix_pow(self, a: List[List[int]], n: int) -> List[List[int]]:
        ret = [[1, 0], [0, 1]]
        while n > 0:
            if n & 1:
                ret = self.matrix_multiply(ret, a)
            n >>= 1
            a = self.matrix_multiply(a, a)
        return ret

    def matrix_multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c
```


## 198. 打家劫舍

[198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/)

- 数组

数组版因为要访问`i - 2`和`i - 1`两个状态，负索引在程序语言上难度很大，正向反向又没区别，所以弄成逆向循环

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * (N + 2)
        for i in range(N - 1, -1, -1):
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
        return dp[0]
```

- 状压

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        p1 = p2 = c = 0
        for i in range(N):
            c = max(p1, p2 + nums[i])
            p2 = p1
            p1 = c
        return c
```

## 213. 打家劫舍 II

[213. 打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/)

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        return nums[0] if N==1 else max(self._rob(nums, 0, N-1), self._rob(nums, 1, N))

    def _rob(self, nums: List[int], s, e) -> int:
        p1 = p2 = c = 0
        for i in range(s, e):
            c = max(p1, p2 + nums[i])
            p2 = p1
            p1 = c
        return c
```

## 337. 打家劫舍 III

[337. 打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii/)

时间空间复杂度为 $O(N)$

```python
class Solution:
    def rob(self, root: TreeNode) -> int:
        memo = {}

        def rec(root: TreeNode):
            if root is None:
                return 0
            if id(root) in memo:
                return memo[id(root)]
            do_it = root.val + \
                    (rec(root.left.left) + rec(root.left.right) if root.left else 0) + \
                    (rec(root.right.left) + rec(root.right.right) if root.right else 0)
            not_do = rec(root.left) + rec(root.right)
            ans = max(do_it, not_do)
            memo[id(root)] = ans
            return ans

        return rec(root)
```

# 排序
## 排序算法模板
### 归并排序
```python
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result
```

### 基数排序

野生实现

```python
def radix_sort(nums):
    """基数排序"""
    i = 0  # 记录当前正在排拿一位，最低位为1
    max_num = max(nums)  # 最大值
    N = len(str(max_num))  # 记录最大值的位数
    while i < N:
        buckets = [[] for _ in range(10)]  # 初始化桶数组
        for num in nums:
            buckets[int(num / (10 ** i)) % 10].append(num)  # 找到位置放入桶数组
        print(buckets)
        nums.clear()
        for bucket in buckets:  # 放回原序列
            for num in bucket:
                nums.append(num)
        i += 1


if __name__ == '__main__':
    a = [334, 5, 67, 345, 7, 345345, 99, 4, 23, 78, 45, 1, 3453, 23424]
    radix_sort(a)
    print(a)

```

LeetCode官方实现

[https://leetcode-cn.com/problems/maximum-gap/solution/zui-da-jian-ju-by-leetcode-solution/](https://leetcode-cn.com/problems/maximum-gap/solution/zui-da-jian-ju-by-leetcode-solution/)

```java
import java.util.Arrays;

public class RadixSort {

    static int[] radixSort(int[] nums) {
        long exp = 1;
        int n = nums.length;
        int[] buf = new int[n];
        int maxVal = Arrays.stream(nums).max().getAsInt();
        while (maxVal >= exp) {
            int[] cnt = new int[10];
            for (int i = 0; i < n; i++) {
                int digit = (nums[i] / (int) exp) % 10;
                cnt[digit]++;
            }
            for (int i = 1; i < 10; i++) {  // cumulation
                cnt[i] += cnt[i - 1];
            }
            // 因为cnt维护索引是随迭代递减的，所以为了维护相对顺序，i也需要递减遍历
            for (int i = n - 1; i >= 0; i--) {
                int digit = (nums[i] / (int) exp) % 10;
                buf[cnt[digit] - 1] = nums[i];//计数-1=索引
                cnt[digit]--;
            }
            // src srcPos  dest  destPos  length
            System.arraycopy(buf, 0, nums, 0, n);
            exp *= 10;
        }
        return nums;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(RadixSort.radixSort(new int[]{
                334, 5, 67, 345, 7, 345345, 99, 4, 23, 78, 45, 1, 3453, 23424})));
    }
}

```




## 排序题
### 1365. 有多少小于当前数字的数字

[1365. 有多少小于当前数字的数字](https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/)
```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        K = 100
        counts = [0 for _ in range(K + 1)]
        for num in nums:
            counts[num] += 1
        for i in range(1, K + 1):
            counts[i] += counts[i - 1]
        return [counts[num - 1] if num else 0 for num in nums]
```




### 1356. 根据数字二进制下 1 的数目排序
[1356. 根据数字二进制下 1 的数目排序](https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/)


```python
class Solution:
    def count1(self, x):
        res = 0
        while x:
            res += x & 1
            x >>= 1
        return res

    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (self.count1(x), x))
```

- 可以利用递推进行线性处理`bits`

```cpp
class Solution {
public:
    vector<int> sortByBits(vector<int> &arr) {
        vector<int> bits(10001, 0);
        for (int i = 1; i < bits.size(); ++i) {
            bits[i] = bits[i >> 1] + (i & 1);
        }
        // [&bits] 表示闭包中按引用捕获 bits
        sort(arr.begin(), arr.end(), [&bits](int x, int y) -> bool {  //lambda表达式中， -> 可以去掉的
            if (bits[x] < bits[y]) {
                return true;  // 实际上是在重载 < 号
            } else if (bits[x] > bits[y]) {
                return false;
            } else {
                return x < y;  // default
            }
        });
        return arr;
    }
};
```


### 1122. 数组的相对排序
[1122. 数组的相对排序](https://leetcode-cn.com/problems/relative-sort-array/)
>输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]

```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = collections.Counter(arr1)
        res = []
        for e in arr2:
            if e in counter:
                res += [e] * counter[e]
                counter.pop(e)
        sorted_keys = sorted(list(counter.keys()))
        for k in sorted_keys:
            cnt = counter[k]
            res += [k] * cnt
        return res
```

3行python

```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2 += sorted(set(arr1) - set(arr2))
        arr1.sort(key=arr2.index)
        return arr1
```


### 1370. 上升下降字符串

[1370. 上升下降字符串](https://leetcode-cn.com/problems/increasing-decreasing-string/)


瞎写的方法

```python
class Solution:
    def sortString(self, s: str) -> str:
        counter = collections.Counter(s)
        keys = list(counter.keys())
        keys.sort()
        res = ""
        N = len(keys)
        rng = list(range(N)) + list(range(N - 1, -1, -1))
        while True:
            should_break = True
            for i in rng:
                key = keys[i]
                if counter[key]:
                    counter[key] -= 1
                    should_break = False
                    res += key
            if should_break:
                break
        return res
```


更简洁的写法，桶计数


```python
class Solution:
    def sortString(self, s: str) -> str:
        num = [0] * 26
        for c in s:
            num[ord(c) - 97] += 1
        ret, M = "", 26
        while len(ret) < len(s):
            for i in list(range(M)) + list(range(M - 1, -1, -1)):
                if num[i]:
                    ret += chr(i + 97)
                    num[i] -= 1
        return ret
```


### 406. 根据身高重建队列

[406. 根据身高重建队列](https://leetcode-cn.com/problems/queue-reconstruction-by-height/)

[官方题解](https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/gen-ju-shen-gao-zhong-jian-dui-lie-by-leetcode-sol/)

选择**从高到低排序**

每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先按身高从高到低排序， 再按前面的人数从小到大排序
        people.sort(key=lambda x: (-x[0], x[1])) 
        n = len(people)
        ans = list()
        for person in people:
        	# 看似脱裤子放屁， 其实是防止数组越界错
        	# 用前面的人数作为下标，进行插入
            ans[person[1]:person[1]] = [person]
        return ans
```


## 桶排序

###  164. 最大间距
[164. 最大间距](https://leetcode-cn.com/problems/maximum-gap/)

### 1370. 上升下降字符串
[1370. 上升下降字符串](https://leetcode-cn.com/problems/increasing-decreasing-string/)



```python
class Solution:
    def sortString(self, s: str) -> str:
        num = [0] * 26
        for c in s:
            num[ord(c) - 97] += 1
        ret, M = "", 26
        while len(ret) < len(s):
            for i in list(range(M)) + list(range(M - 1, -1, -1)):
                if num[i]:
                    ret += chr(i + 97)
                    num[i] -= 1
        return ret
```

## 归并排序

### 327. 区间和的个数

我是按照官方的java题解翻译过来的

普通的归并排序

```python
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result
```



```python
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        s = 0
        N = len(nums)
        sum = [0] * (N + 1)
        for i, num in enumerate(nums):
            s += num
            sum[i + 1] = s
        res= self.countRangeSumRecursive(sum, lower, upper, 0, N)
        return res

    def countRangeSumRecursive(self, sum, lower, upper, left, right):
        if left == right:
            return 0
        mid = (left + right) // 2
        n1 = self.countRangeSumRecursive(sum, lower, upper, left, mid)
        n2 = self.countRangeSumRecursive(sum, lower, upper, mid + 1, right)
        ret = n1 + n2
        i = left
        l = mid + 1
        r = mid + 1
        while i <= mid:
            while l <= right and sum[l] - sum[i] < lower:
                l += 1
            while r <= right and sum[r] - sum[i] <= upper:
                r += 1
            ret += (r - l)
            i += 1
        p1 = left
        p2 = mid + 1
        sorted = []
        while p1 <= mid and p2 <= right:
            if sum[p1] < sum[p2]:
                sorted.append(sum[p1])
                p1 += 1
            else:
                sorted.append(sum[p2])
                p2 += 1
        while p1 <= mid:
            sorted.append(sum[p1])
            p1 += 1
        while p2 <= right:
            sorted.append(sum[p2])
            p2 += 1
        for i, e in enumerate(sorted):
            sum[left + i] = e
        return ret
```



### 493. 翻转对
[493. 翻转对](https://leetcode-cn.com/problems/reverse-pairs/)

```java
class Solution {
    public int reversePairs(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        return reversePairsRecursive(nums, 0, nums.length - 1);
    }

    public int reversePairsRecursive(int[] nums, int left, int right) {
        if (left == right) {
            return 0;
        } else {
            int mid = (left + right) / 2;
            int n1 = reversePairsRecursive(nums, left, mid);
            int n2 = reversePairsRecursive(nums, mid + 1, right);
            int ret = n1 + n2;

            // 首先统计下标对的数量
            int i = left;
            int j = mid + 1;
            while (i <= mid) {
                while (j <= right && (long) nums[i] > 2 * (long) nums[j]) {
                    j++;
                }
                ret += j - mid - 1;
                i++;
            }

            // 随后合并两个排序数组
            int[] sorted = new int[right - left + 1];
            int p1 = left, p2 = mid + 1;
            int p = 0;
            while (p1 <= mid && p2 <= right) {
                if (nums[p1] < nums[p2]) {
                    sorted[p++] = nums[p1++];
                } else {
                    sorted[p++] = nums[p2++];
                }
            }
            while (p1 <= mid) sorted[p++] = nums[p1++];
            while (p2 <= right) sorted[p++] = nums[p2++];
            for (int k = 0; k < sorted.length; k++) {
                nums[left + k] = sorted[k];
            }
            return ret;
        }
    }
}
```

归并排序部分官方写法是：
```python
while (p1 <= mid || p2 <= right) {
    if (p1 > mid) {
        sorted[p++] = nums[p2++];
    } else if (p2 > right) {
        sorted[p++] = nums[p1++];
    } else {
        if (nums[p1] < nums[p2]) {
            sorted[p++] = nums[p1++];
        } else {
            sorted[p++] = nums[p2++];
        }
    }
}
```



# 数学

## 位运算

### 136. 只出现一次的数字
[136. 只出现一次的数字](https://leetcode-cn.com/problems/single-number/)
```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
```

### 389. 找不同

[389. 找不同](https://leetcode-cn.com/problems/find-the-difference/)

- 求和法

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = 0
        t_sum = 0
        for c in s:
            s_sum += ord(c)
        for c in t:
            t_sum += ord(c)
        return chr(t_sum - s_sum)
```

- 位运算

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ret = 0
        for c in s + t:
            ret ^= ord(c)
        return chr(ret)
```

## 几何

### 976. 三角形的最大周长

[976. 三角形的最大周长](https://leetcode-cn.com/problems/largest-perimeter-triangle/)


不失一般性，我们假设三角形的边长满足$a<b<c$，那么这三条边组成面积不为零的三角形的充分必要条件为 $a+b>c$。


```python
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        N = len(A)
        if N < 3:
            return 0
        A.sort(reverse=True)
        for i in range(N - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return sum(A[i:i + 3])
        return 0
```

## 素数

### 素数筛

[204. 计数质数](https://leetcode-cn.com/problems/count-primes/)


- 枚举法

时间复杂度：$\mathcal{O}(n\sqrt{n})$

```python
class Solution:
    def is_prime(self, x) -> int:
    	# python的range是左闭右开，所以要 + 1
        for i in range(2, int(sqrt(x)) + 1): 
            if x % i == 0:
                return 0
        return 1

    def countPrimes(self, n):
        return sum(self.is_prime(i) for i in range(2, n))
```

- 埃氏筛

时间复杂度： $\mathcal{O}(NloglogN)$

```python
class Solution:
    def countPrimes(self, n):
        is_prime = [1] * n
        ans = 0
        for x in range(2, n):
            if is_prime[x]:
                ans += 1
                if x ** 2 < n:
                    j = x ** 2
                    while j < n:
                        is_prime[j] = 0
                        j += x
        return ans
```

- 线性筛

时间复杂度： $\mathcal{O}(N)$

思路：保证每一个合数，仅被自身的第一个质因数筛除

示例：当`i=6`,可以筛除`6*2=12`，当`6%2==0`时，退出；如果继续，`6*3=18`会被筛除，而`18`会被`9*2`筛除，因为`18`的最小质因数为`2`

```python
class Solution:
    def countPrimes(self, n):
        is_prime = [1] * n
        primes = []
        for x in range(2, n):
            if is_prime[x]:
                primes.append(x)
            for prime in primes:
                if x * prime >= n:
                    break
                is_prime[x * prime] = 0
                if x % prime==0:
                    break
        return len(primes)
```


线性筛还有其他拓展用途，有能力的读者可以搜索关键字「积性函数」继续探究如何利用线性筛来求解积性函数相关的题目。


## 进制问题

### 1018. 可被 5 整除的二进制前缀

[1018. 可被 5 整除的二进制前缀](https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/)


随手一写

```python
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        acc = 0
        ans = []
        for num in A:
            acc = acc * 2 + num
            ans.append(acc % 5 == 0)
        return ans
```




# 脑筋急转弯

## 134. 加油站

[134. 加油站](https://leetcode-cn.com/problems/gas-station/)

[能看懂的题解](https://leetcode-cn.com/problems/gas-station/solution/shi-yong-tu-de-si-xiang-fen-xi-gai-wen-ti-by-cyayc/)

```python
class Solution:
    # https://leetcode-cn.com/problems/gas-station/solution/shi-yong-tu-de-si-xiang-fen-xi-gai-wen-ti-by-cyayc/
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        reward = 0
        min_i = 0
        min_reward = inf
        for i in range(N):
            reward += gas[i] - cost[i]
            if reward < min_reward:
                min_reward = reward
                min_i = i
        return (min_i + 1) % N if reward >= 0 else -1
```



# 二叉树

## 001. 东哥笔记

性质：（简单记录一下，有时间综合记录）

后序遍历序列也可以这样计算，先右后左地计算preorder，然后inverse就是后序。

## 99. 恢复二叉搜索树

[99. 恢复二叉搜索树](https://leetcode-cn.com/problems/recover-binary-search-tree/)



## 124. 二叉树中的最大路径和

[124. 二叉树中的最大路径和](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)

```python
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans = -inf
        def recursion(node)->int:
            nonlocal ans
            if node is None:
                return 0
            left = max(0, recursion(node.left))
            right = max(0, recursion(node.right))
            ans = max(ans, left + right + node.val)
            return node.val + max(left, right)
        recursion(root)
        return ans
```



## 116. 填充每个节点的下一个右侧节点指针
- 递归

题目要求常数空间。

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        def recursion(node1, node2):
            if node1 is None or node2 is None:
                return
            node1.next = node2
            recursion(node1.left, node1.right)
            recursion(node2.left, node2.right)
            recursion(node1.right, node2.left)
        recursion(root.left, root.right)
        return root
```

- 层序遍历

跑起来快多了。。

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        queue = collections.deque()
        queue.append(root)
        while queue:
            sz = len(queue)
            pre = None
            for _ in range(sz):
                top = queue.popleft()
                if pre:
                    pre.next = top
                pre = top
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
        return root
```

## 114. 二叉树展开为链表

```python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        def rec(node: TreeNode):
            if not node:
                return None
            rec(node.left)
            rec(node.right)
            left, right = node.left, node.right
            node.left = None
            node.right = left
            p = node
            while p.right:
                p = p.right
            p.right = right

        rec(root)
```

## 递归题

### 101. 对称二叉树

[101. 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree/)

> TODO: 学习迭代法

```python
class Solution:
    def isSymmetric(self, root):
        # 56ms 击败10%
        # return self.check(root, root)
        if root is None:
            return True
        # 52ms 击败20%
        return self.check(root.left, root.right)

    def check(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)

```

### 104. 二叉树的最大深度
[104. 二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)

> TODO: DFS

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = []
        queue.append(root)
        cnt = 0
        while queue:
            layers = []
            while queue:
                layers.append(queue.pop(0))
            for top in layers:
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            cnt += 1
        return cnt
```


### 226. 翻转二叉树

[226. 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/)

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root
```

## 二叉树的各种题型

### 001. 东哥笔记

[https://www.cnblogs.com/TQCAI/p/8546737.html](https://www.cnblogs.com/TQCAI/p/8546737.html)

### 根据中序 + 后序,前序 → 建树,建序




- 前序 + 中序 $\rightarrow$ 建树

```cpp
int pre[LEN] = {8, 5, 2, 6, 10, 9, 11};
int in[LEN] = {2, 5, 6, 8, 9, 10, 11};

BTNode *build_tree(int ps, int pe, int is, int ie) {
    if (ps > pe) return NULL;
    if (ps == pe) return new BTNode(in[is]);
    int i = is;
    while (i <= ie && in[i] != pre[ps]) i++;
    // post -> pre ,  pe -> ps
    BTNode *node = new BTNode(in[i]);
    int n_left = i - is;    //左侧元素数量
    node->left = build_tree(ps + 1, ps + n_left, is, is + n_left - 1);
    node->right = build_tree(ps + n_left + 1, pe, i + 1, ie);
    // 相比post的左侧两个参数，全部 + 1 , 中序部分不变
    return node;
}

BTNode *root_bd = build_tree(0, n - 1, 0, n - 1);
```

- 后序 + 中序 $\rightarrow$ 建树

```cpp
int post[LEN] = {2, 6, 5, 9, 11, 10, 8};
int in[LEN] = {2, 5, 6, 8, 9, 10, 11};

BTNode *build_tree(int ps, int pe, int is, int ie) {
    if (ps > pe) return NULL;
    if (ps == pe) return new BTNode(in[is]);
    int i = is;
    while (i <= ie && in[i] != post[pe]) i++;
    BTNode *node = new BTNode(in[i]);
    int n_left = i - is;    //左侧元素数量
    node->left = build_tree(ps, ps + n_left - 1, is, is + n_left - 1);
    node->right = build_tree(ps + n_left, pe - 1, i + 1, ie);
    return node;
}

BTNode *root_bd = build_tree(0, n - 1, 0, n - 1);
```

- 前序 + 中序 $\rightarrow$ 建后序

```cpp
int pre[LEN] = {8, 5, 2, 6, 10, 9, 11};
int in[LEN] = {2, 5, 6, 8, 9, 10, 11};
int post[LEN];
int t = 0;

void setPost(int ps,int pe,int is,int ie){
    if(ps>pe)return;//null
    if(ps==pe){
        post[t++]=pre[ps];
    }else{
        //find the elem is the pair of preOrder (ps)
        int i=is;
        while(in[i]!=pre[ps] && i<ie) i++;//redirect
        //left
        setPost(ps+1, ps+i-is, is, i-1);
        //right
        setPost(ps+i-is+1, pe, i+1, ie);
        //root
        post[t++]=pre[ps];
    }
}

setPost(0, n - 1, 0, n - 1);
```

- 后序 + 中序 $\rightarrow$ 建前序

```cpp
int pre[LEN];
int in[LEN] = {2, 5, 6, 8, 9, 10, 11};
int post[LEN] = {2, 6, 5, 9, 11, 10, 8};
int t=0;

void setPre(int ps,int pe,int is,int ie){
    if(ps>pe)return;//null
    if(ps==pe){
        pre[t++]=post[ps];
    }else{
        //find the elem is the pair of preOrder (ps)
        int i=is;
        while(in[i]!=post[pe] && i<ie) i++;//redirect
        //root
        pre[t++]=post[pe];
        //left
        setPre(ps, ps+i-is-1, is, i-1);
        //right
        setPre(ps+i-is, pe-1, i+1, ie);
    }
}

setPre(0, n - 1, 0, n - 1);
```

[105. 从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pre_s, pre_e, in_s, in_e):
            if pre_s > pre_e or in_s > in_e:
                return None
            if pre_s == pre_e:
                return TreeNode(preorder[pre_s])
            i = inorder.index(preorder[pre_s])
            num_left = i - in_s
            node = TreeNode(preorder[pre_s])
            node.left = build(pre_s + 1, pre_s + num_left, in_s, i - 1)
            node.right = build(pre_s + num_left + 1, pre_e, i + 1, in_e)
            return node

        N = len(inorder)
        return build(0, N - 1, 0, N - 1)
```


[106. 从中序与后序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(post_s, post_e, in_s, in_e):
            if post_s > post_e or in_s > in_e:
                return None
            if post_s == post_e:
                return TreeNode(postorder[post_e])
            i = inorder.index(postorder[post_e])
            num_left = i - in_s
            node = TreeNode(postorder[post_e])
            node.left = build(post_s, post_s + num_left - 1, in_s, i - 1)
            node.right = build(post_s + num_left, post_e - 1, i + 1, in_e)
            return node

        N = len(inorder)
        return build(0, N - 1, 0, N - 1)

```


### 根据前序 + 后序 →  建立后序,判断有多少树

[分析报告](https://files-cdn.cnblogs.com/files/TQCAI/pat1119%E5%88%86%E6%9E%90.pdf)

- 后序 + 中序 $\rightarrow$ 建后序

```cpp
int pre[LEN] = {8, 5, 2, 6, 10, 9, 11};
int in[LEN];
int post[LEN] = {2, 6, 5, 9, 11, 10, 8};
int t = 0;
int flag = 1;

void setIn(int preS, int preE, int postS, int postE) {
    if (preS == preE) {
        in[t++] = pre[preS];
        return;
    }
    //finding the elem which is the root of left sub_tree
    int i = postS;
    while (i <= postE && post[i] != pre[preS + 1]) i++;
    //calculate the numbers of left sub_tree
    int leftNum = i - postS + 1;
    //is paradox
    if (i == postE - 1) {
        flag = 0;
        setIn(preS + 1, preS + leftNum, postS, i);//default consider this is a right leaf
        in[t++] = pre[preS];
        return;
    }
    //build the in_order traversal sequence
    setIn(preS + 1, preS + leftNum, postS, i);
    in[t++] = pre[preS];
    setIn(preS + leftNum + 1, preE, i + 1, postE - 1);
}

setIn(0, n - 1, 0, n - 1);
```

- 后序 + 中序 $\rightarrow$ 判断有多少可能的树

```cpp
int cnt;

void calc(int preS, int preE, int postS, int postE) {
    if (preS >= preE) return;
    int i = postS;
    while (i <= postE - 1 && post[i] != pre[preS + 1]) i++;
    int ln = i - postS + 1;    //left_num
    if (i == postE - 1) cnt++;
    calc(preS + 1, preS + ln, postS, postS + ln - 1);
    calc(preS + ln + 1, preE, postS + ln, postE - 1);
}
```
在上文模板的基础上，在检测到有一组结点既可以当左子树，又可以当右子树时，`cnt++`（记录这样的结点出现的个数）。最后输出cnt的二次幂（假如有一个这样的结点，那就有左右两种形态。如果有两个，在控制左右形态的同时，左右又各有左右两种形态，一次类推，比图cnt=3 ,ans就等于8 ……）

$$ans=cnt^2$$

