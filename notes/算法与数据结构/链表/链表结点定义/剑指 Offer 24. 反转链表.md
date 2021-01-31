[剑指 Offer 24. 反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/)

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pp=None
        p=head
        while p:
            next=p.next
            p.next=pp
            pp=p
            p=next
        return pp
```