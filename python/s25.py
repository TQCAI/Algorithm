from structure import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        a = b = head
        # 循环体写错
        for _ in range(k):
            if b is None:
                return head
            b = b.next
        new_head = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k) # b 写错
        return new_head

    def reverse(self, a, b):
        p = a
        pp = None
        while p != b:
            next = p.next
            p.next = pp
            pp = p
            p = next
        return pp


node = ListNode.fromList([1, 2, 3, 4, 5])
print(Solution().reverseKGroup(node, 3))
