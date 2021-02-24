from structure import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head: # 长度为0的情况
            return None
        slow = slow_pre = head
        fast = head
        while fast and fast.next:
            slow_pre = slow
            slow = slow.next
            fast = fast.next.next
        if fast is not None:  # 奇数情况
            slow = slow.next
            slow_pre = slow_pre.next
        if slow is None: # 长度为1的情况
            return head
        slow_pre.next = None
        p = slow
        pre = None
        while p:
            aft1 = p.next
            p.next = pre
            pre = p
            p = aft1
        p1 = head
        p2 = pre
        while p1 and p2:
            aft1 = p1.next
            aft2 = p2.next
            p1.next = p2
            p2.next = aft1
            p1 = aft1
            p2 = aft2


node = ListNode.fromList([1])
Solution().reorderList(node)
print(node)
