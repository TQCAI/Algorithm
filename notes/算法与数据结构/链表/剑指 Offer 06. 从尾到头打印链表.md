[剑指 Offer 06. 从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)

- 相当于后序遍历的递归

```python
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        return self.reversePrint(head.next) + [head.val]
```