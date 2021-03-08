from structure import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head: return
        # 寻找链表中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 反转链表
        p = slow.next
        slow.next = None
        if p is None: return
        pre = None
        while p:
            aft = p.next
            p.next = pre
            pre = p
            p = aft
        # 合并链表
        a, b = head, pre
        while True:
            an = a.next
            bn = b.next if b else None
            a.next = b
            if b:
                b.next = an
            a = an
            b = bn
            if not b:
                break


node = ListNode.fromList([1])
Solution().reorderList(node)
print(node)
