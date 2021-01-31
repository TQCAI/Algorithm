[剑指 Offer 18. 删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)

```python
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        pre=None
        p=head
        if head.val==val:
            p=head.next
            head.next=None
            head=None
            return p
        while p:
            if p.val==val:
                pre.next=p.next
                p=None
                break
            pre=p
            p=p.next
        return head

```