[剑指 Offer 22. 链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)

```python
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if None:
            return None
        p=head
        pp=head
        while p and k:
            p=p.next
            k-=1
        while p:
            p=p.next
            pp=pp.next
        return pp if pp else None
```
