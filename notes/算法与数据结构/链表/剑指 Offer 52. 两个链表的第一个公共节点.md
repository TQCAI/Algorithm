[剑指 Offer 52. 两个链表的第一个公共节点](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/)

[图解 双指针法，浪漫相遇](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solution/shuang-zhi-zhen-fa-lang-man-xiang-yu-by-ml-zimingm/)

- 评论 1

太6了，我的理解： 两个链表长度分别为L1+C、L2+C， C为公共部分的长度，按照楼主的做法： 第一个人走了L1+C步后，回到第二个人起点走L2步；第2个人走了L2+C步后，回到第一个人起点走L1步。 当两个人走的步数都为L1+L2+C时就两个家伙就相爱了

- 评论 2

```python
node1 = node1.next if node1 else headB
```
而不是
```python
node1 = node1.next if node1.next else headB
```
可以理解为两条链表最后都指向了同一个 null （None）节点，代替了不相交的特殊情况。 非常的巧妙。

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        p2 = headB
        while p1 != p2: # 即使不相交，最后两个指针也会同时 == None
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
```

[两个链表的第一个公共节点【双指针法】详解](https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solution/liang-ge-lian-biao-de-di-yi-ge-gong-gong-l4vl/)

```python
class Solution:
    def getNodeLength(self, node: ListNode):
        ret = 0
        while node:
            node = node.next
            ret += 1
        return ret

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 1. 求长度
        l1 = self.getNodeLength(headA)
        l2 = self.getNodeLength(headB)
        # 2. 默认headA最短
        if l1 > l2:
            l1, l2 = l2, l1
            headA, headB = headB, headA
        sub = l2 - l1
        p1, p2 = headA, headB
        # 3. 校正p2
        while p2 and sub:
            p2 = p2.next
            sub -= 1
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
```



